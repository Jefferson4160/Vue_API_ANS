## Teste de Nivelamento - API de Consulta de Operadoras

Este projeto é uma solução full-stack desenvolvida para a consulta de operadoras de saúde, utilizando os dados reais do CADOP da Agência Nacional de Saúde Suplementar (ANS). A aplicação permite que usuários busquem informações de operadoras de forma rápida e reativa através de uma interface web.

## Tecnologias Utilizadas

1. Backend:
  1.1 Python 3.12: Base para o processamento de dados e lógica de servidor.
  1.2 FastAPI: Framework moderno e de alta performance para a construção da API REST.
  1.3 Pandas: Biblioteca líder para manipulação e análise de dados, utilizada para filtrar o CSV.
  1.4 Uvicorn: Servidor para a execução da aplicação.

2. Frontend:
  2.1 Vue.js 3: Framework JavaScript reativo para a construção da interface de usuário.
  2.2 Axios: Cliente HTTP para a comunicação entre o navegador e o servidor Python.
  2.3 CSS3: Estilização externa.

## Decisões Técnicas e Tratamento de Dados

Integridade de Caracteres: O arquivo CSV é processado com o encoding utf-8-sig para garantir que acentos e cedilhas de cidades e razões sociais brasileiras sejam exibidos corretamente.

Programação Defensiva: Implementada a normalização automática dos nomes das colunas (remoção de espaços e conversão para minúsculas) para evitar erros de mapeamento de dados (KeyError).

Compatibilidade JSON: Utilizado o método .fillna("Não Informado") para converter valores nulos (NaN) em texto, prevenindo falhas de serialização na resposta JSON.

Otimização de Performance: A busca textual utiliza máscaras booleanas do Pandas (.str.contains) com o parâmetro case=False, garantindo que a pesquisa seja rápida e ignore diferenças entre maiúsculas e minúsculas.

Comunicação Assíncrona: O frontend utiliza a estrutura async/await do JavaScript, permitindo que a interface permaneça fluida enquanto aguarda o processamento dos dados no servidor.

