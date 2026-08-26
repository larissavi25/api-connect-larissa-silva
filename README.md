# API Connect

## Objetivo

A API Connect é uma API REST desenvolvida em Python utilizando o framework Flask. O projeto foi desenvolvido como um MVP para demonstrar conceitos de desenvolvimento back-end, APIs HTTP, operações CRUD, validação de dados, organização de código e separação de responsabilidades.

A aplicação permite realizar operações relacionadas ao cadastro de usuários, incluindo criação, listagem, consulta por ID, atualização e remoção de registros.

Durante esta etapa do projeto, os dados são armazenados temporariamente em uma estrutura em memória. Dessa forma, os registros permanecem disponíveis enquanto o servidor estiver em execução.

## Tecnologias utilizadas

- Python 3
- Flask
- Git
- GitHub
- API REST
- JSON
- HTTP

## Estrutura do projeto

```text
api-connect/
├── controllers/
│   └── connect_controller.py
├── data/
│   └── connect_data.py
├── routes/
│   └── connect_routes.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
Responsabilidade dos principais arquivos
app.py
Arquivo principal da aplicação. Inicializa o Flask, registra as rotas e configura o servidor.

routes/connect_routes.py
Define as rotas HTTP da API e encaminha as requisições para os respectivos controladores.

controllers/connect_controller.py
Contém os controladores responsáveis por receber as requisições, validar os dados e executar as operações solicitadas.

data/connect_data.py
Contém a estrutura utilizada para simular a persistência dos usuários em memória e a geração dos IDs.

requirements.txt
Lista as dependências Python utilizadas pelo projeto.

.gitignore
Define arquivos e diretórios que não devem ser enviados para o repositório, como o ambiente virtual venv.

Pré-requisitos
Para executar o projeto localmente, é necessário ter instalado:

Python 3
Git
Também é recomendado utilizar um ambiente virtual Python para isolar as dependências do projeto.

Instalação e execução
1. Clonar o repositório
git clone https://github.com/larissavi25/api-connect-larissa-silva.git
Depois, entre na pasta do projeto:
cd api-connect-larissa-silva

2. Criar o ambiente virtual
No Windows:
python -m venv venv
No Linux ou Codespaces:
python3 -m venv venv

3. Ativar o ambiente virtual
No Windows:
venv\Scripts\activate
No Linux, macOS ou Codespaces:
source venv/bin/activate

4. Instalar as dependências
pip install -r requirements.txt

5. Executar a aplicação
python app.py
O servidor será iniciado na porta 5000:
http://localhost:5000

Endpoint principal
Verificar funcionamento da API
GET /
Retorna uma mensagem informando que a API está funcionando.
Exemplo:
GET /
Resposta:
{
  "message": "API Connect funcionando!"
}
Status esperado:
200 OK

Endpoints de usuários
Método	Endpoint	Descrição	Status esperado
GET	/	Verifica se a API está funcionando	200
POST	/usuarios	Cadastra um novo usuário	201
GET	/usuarios	Lista todos os usuários	200
GET	/usuarios/<id>	Consulta um usuário pelo ID	200 ou 404
PUT	/usuarios/<id>	Atualiza os dados de um usuário	200 ou 404
DELETE	/usuarios/<id>	Remove um usuário	204 ou 404

Exemplos de requisições
Criar usuário
POST /usuarios

Corpo da requisição:
{
  "nome": "Amanda",
  "email": "amanda@email.com"
}
Resposta esperada:
{
  "data": {
    "id": 1,
    "nome": "Amanda",
    "email": "amanda@email.com"
  }
}
Status:
201 Created

Criar usuário sem e-mail
POST /usuarios
Corpo da requisição:
{
  "nome": "Carlos"
}

Como o campo email é obrigatório, a API retorna erro.
Resposta:
{
  "error": "O campo email é obrigatório."
}
Status:
400 Bad Request

Listar usuários
GET /usuarios
Exemplo de resposta:
[
  {
    "id": 1,
    "nome": "Amanda",
    "email": "amanda@email.com"
  }
]
Status:
200 OK

Buscar usuário por ID
GET /usuarios/1
Exemplo de resposta:
{
  "id": 1,
  "nome": "Amanda",
  "email": "amanda@email.com"
}
Status:
200 OK

Quando o ID não existe:
GET /usuarios/999
Resposta:
{
  "erro": "Usuário não encontrado."
}
Status:
404 Not Found

Atualizar usuário
PUT /usuarios/1
Corpo da requisição:
{
  "nome": "Amanda Silva",
  "email": "amanda.silva@email.com"
}
Resposta:
{
  "id": 1,
  "nome": "Amanda Silva",
  "email": "amanda.silva@email.com"
}
Status:
200 OK
Caso o ID não exista:
404 Not Found

Remover usuário
DELETE /usuarios/1
Quando o usuário existe, o registro é removido.
Status:
204 No Content
Caso o ID não exista:
404 Not Found

Validação
A API realiza validações básicas durante o cadastro de usuários.
Os campos nome e email são obrigatórios. Quando algum desses campos não é informado, a API interrompe o cadastro e retorna o status HTTP 400 Bad Request.
Exemplo:
{
  "nome": "Carlos"
}
Resposta:
{
  "error": "O campo email é obrigatório."
}

Persistência dos dados
Nesta versão do projeto, a persistência é simulada por meio de uma lista Python armazenada em memória.

Os usuários são armazenados enquanto o servidor estiver em execução. Como não foi utilizado um banco de dados nesta etapa do MVP, os dados são perdidos quando a aplicação é encerrada ou reiniciada.

Essa abordagem foi utilizada para manter o foco inicial no desenvolvimento das rotas, requisições HTTP, respostas, validações e organização da arquitetura.

Códigos HTTP utilizados
A API utiliza códigos de status HTTP para representar o resultado das operações:

200 OK — requisição processada com sucesso.
201 Created — novo usuário criado com sucesso.
204 No Content — usuário removido com sucesso, sem conteúdo na resposta.
400 Bad Request — dados obrigatórios não informados ou requisição inválida.
404 Not Found — usuário não encontrado.
Testes realizados
Durante o desenvolvimento foram realizados testes dos principais cenários da API:

Cadastro de usuário com nome e e-mail, retornando 201 Created.
Tentativa de cadastro sem e-mail, retornando 400 Bad Request.
Listagem dos usuários cadastrados, retornando 200 OK.
Busca de usuário com ID inexistente, retornando 404 Not Found.
Os testes foram realizados por meio de requisições HTTP enviadas ao servidor Flask.

Considerações finais
A API Connect foi desenvolvida com o objetivo de aplicar conceitos de desenvolvimento back-end e arquitetura de software em uma aplicação prática.

A separação entre rotas, controladores e camada de dados contribui para uma organização mais modular, facilitando a manutenção e a evolução do sistema. A estrutura também permite que a persistência em memória seja posteriormente substituída por um banco de dados sem a necessidade de concentrar todas as responsabilidades em um único arquivo.

Como evolução futura, o projeto poderá incorporar banco de dados, autenticação, tratamento de erros mais abrangente, testes automatizados e outras funcionalidades necessárias para transformar o MVP em uma aplicação mais completa.
