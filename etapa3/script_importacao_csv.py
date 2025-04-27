import csv
import psycopg2
import io
import unicodedata
import re

def clean_text(text):
    if not text:
        return ''
    text = unicodedata.normalize('NFKD', str(text))
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text.strip()

def parse_winner(value):
    if not value:
        return False
    value = str(value).strip().lower()
    return value in ['true', '1', 'yes', 'sim']

def clean_year(value):
    if not value:
        return None
    match = re.match(r'(\d{4})', value)
    if match:
        return int(match.group(1))
    return None

conn = psycopg2.connect(
    host="localhost",
    database="oscar",
    user="gabrielsousa",
    password="36531590"
)



diretorio_do_arquivo='/Users/gabrielsousa/Downloads/datasheet_oscars.csv'




cur = conn.cursor()

linhas_importadas = []
linhas_ignoradas = []

with open(diretorio_do_arquivo, 'r', encoding='utf-8') as f:
    content = f.read().replace('\t', ',')

csvfile = io.StringIO(content)
reader = csv.DictReader(csvfile, delimiter=',', restkey='EXTRA', quoting=csv.QUOTE_MINIMAL)

for row in reader:
    try:
        ceremony = int(row['Ceremony'].strip()) if row.get('Ceremony') else None
        year = clean_year(row['Year'].strip()) if row.get('Year') else None
        class_desc = clean_text(row.get('Class', ''))
        category_desc = clean_text(row.get('Category', ''))
        movie_title = clean_text(row.get('Movie', ''))

        if not ceremony or not year or not class_desc or not category_desc or not movie_title:
            linhas_ignoradas.append(row)
            continue

    except Exception as e:
        linhas_ignoradas.append(row)
        continue

    name = clean_text(row.get('Name', ''))
    nominees = clean_text(row.get('Nominees', ''))
    winner = parse_winner(row.get('Winner', ''))
    detail = clean_text(row.get('Detail', ''))
    note = clean_text(row.get('Note', ''))

    if 'EXTRA' in row:
        for extra_note in row['EXTRA']:
            note += ' ' + clean_text(extra_note)

    try:
        cur.execute("""
            INSERT INTO tbl_oscar (ceremony, year)
            VALUES (%s, %s)
            ON CONFLICT (ceremony) DO UPDATE SET year=EXCLUDED.year
            RETURNING id;
        """, (ceremony, year))
        oscar_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO tbl_class (description)
            VALUES (%s)
            ON CONFLICT (description) DO UPDATE SET description=EXCLUDED.description
            RETURNING id;
        """, (class_desc,))
        class_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO tbl_category (description)
            VALUES (%s)
            ON CONFLICT (description) DO UPDATE SET description=EXCLUDED.description
            RETURNING id;
        """, (category_desc,))
        category_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO tbl_movie (title)
            VALUES (%s)
            ON CONFLICT (title) DO UPDATE SET title=EXCLUDED.title
            RETURNING id;
        """, (movie_title,))
        movie_id = cur.fetchone()[0]

        cur.execute("""
            SELECT 1 FROM tbl_nominees
            WHERE oscar_id = %s AND class_id = %s AND category_id = %s
              AND movie_id = %s AND name = %s AND nominees = %s;
        """, (oscar_id, class_id, category_id, movie_id, name, nominees))

        if not cur.fetchone():
            cur.execute("""
                INSERT INTO tbl_nominees (
                    oscar_id, class_id, category_id, movie_id,
                    name, nominees, winner, detail, note
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (oscar_id, class_id, category_id, movie_id,
                  name, nominees, winner, detail, note))

        linhas_importadas.append(row)

    except Exception as e:
        print(f"Erro ao importar linha: {row}\nErro: {e}")
        linhas_ignoradas.append(row)
        continue

conn.commit()
cur.close()
conn.close()

print(f"\n✅ Total de linhas importadas: {len(linhas_importadas)}")
for linha in linhas_importadas:
    print(f"  - {linha}")

print(f"\n❌ Total de linhas ignoradas: {len(linhas_ignoradas)}")
for linha in linhas_ignoradas:
    print(f"  ⚠️ {linha}")
