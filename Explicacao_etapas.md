Projeto: Importação de Dados do Oscar para PostgreSQL





--> Descrição

Este projeto tem como objetivo importar e tratar dados do arquivo 'datasheet_oscars.csv' para um banco de dados PostgreSQL, garantindo a integridade dos dados e o correto relacionamento entre as tabelas.

Foram aplicadas técnicas de limpeza, validação e normalização dos dados para atender aos requisitos do desafio proposto pela TSMX para a posição de Analista de Dados.

 
 




--> Estrutura do Projeto

- 'schema_db.sql' → Script para criação das tabelas no banco de dados. (Dentro da pasta dados_para_a_atividade)
- 'datasheet_oscars.csv' → Base de dados contendo informações sobre indicações e vencedores do Oscar.(Dentro da pasta dados_para_a_atividade)
- 'etapa1' → Processo para criar o database
- 'etapa2'  →  Processo de criar as tabelas no banco conforme o arquivo 'schema_db.sql'
- 'etapa3 → Script de importação e resultado dos dados importados ou não.
- 'etapa4/consultas_sql/lista_de_consultas.txt' → Consultas solicitadas no desafio.
- 'etapa4/consultas_sql/pergunta_1,pergunta_2 e pergunta_3' → Contém a query utilizada para cada consulta e o resultado.








--> Tecnologias Utilizadas

- Python 3
- PostgreSQL
- psycopg2, io, re e o modulo csv









--> Como Executar o Projeto

1. Instale o PostgreSQL no servidor.
2. Crie o banco de dados chamado 'oscar'.
3. Execute o script 'schema_db.sql' para criar as tabelas.
4. Configuracao scrip python para importar os dados em csv.








--> Tratamento de Inconsistências

Durante a importação, foram identificados e tratados os seguintes problemas:
- Valores incorretos na coluna 'Year' .
- Valores não booleanos na coluna 'Winner'.
- Presença de caracteres especiais em campos de texto.
- Linhas com campos obrigatórios ('Ceremony', 'Year', 'Class', 'Category', 'Movie') vazios foram ignoradas.








--> Consultas SQL

1. Listar filmes indicados na categoria "Best Picture" por ano e cerimônia.
2. Categorias em que o filme "Toy Story 3" foi indicado e resultado (vencedor ou não).
3. Atores e atrizes com mais de 3 indicações ao Oscar.

Todas as queries estão documentadas em 'etapa4/consultas_sql/pergunta_1,pergunta_2 e pergunta_3'.





Autor: Gabriel Sousa  
Desenvolvido para a entrevista prática - Analista de Dados TSMX.
