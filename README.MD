# 🎧 DJ Music System

Sistema web desenvolvido com **Python**, **Flask** e **JWT** para gerenciamento de músicas voltado para DJs.

## 📋 Sobre o Projeto

O DJ Music System é uma aplicação web que permite:

* Cadastro de usuários
* Autenticação utilizando JWT (JSON Web Token)
* Consulta de músicas protegida por autenticação
* Interface web simples utilizando HTML, CSS e JavaScript
* Estrutura organizada em camadas para facilitar manutenção e evolução do projeto

Este projeto foi desenvolvido com fins de estudo e prática de conceitos de desenvolvimento web, APIs REST e autenticação.

---

## 🚀 Tecnologias Utilizadas

### Backend

* Python 3
* Flask
* Flask-JWT-Extended
* Flask-CORS
* Python-Dotenv
* Gunicorn

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla JS)

---

## 📁 Estrutura do Projeto

```text
sistema-musica/
│
├── app/
│   ├── data/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   ├── config.py
│   └── __init__.py
│
├── run.py
├── requirements.txt
├── .env
└── README.md
```

### Organização

| Pasta     | Descrição                                   |
| --------- | ------------------------------------------- |
| routes    | Rotas da aplicação                          |
| services  | Regras de negócio                           |
| data      | Dados temporários utilizados pela aplicação |
| templates | Páginas HTML                                |
| config.py | Configurações da aplicação                  |
| run.py    | Arquivo principal da aplicação              |

---

## 🔐 Funcionalidades

### Cadastro de Usuários

Permite registrar novos usuários na aplicação.

### Login

Realiza autenticação do usuário e gera um token JWT.

### Listagem de Músicas

Retorna a lista de músicas cadastradas.

A rota é protegida por autenticação JWT.

---

## 🌐 Rotas Disponíveis

### Cadastro

```http
POST /register
```

Exemplo:

```json
{
  "email": "usuario@email.com",
  "password": "123456"
}
```

---

### Login

```http
POST /login
```

Exemplo:

```json
{
  "email": "usuario@email.com",
  "password": "123456"
}
```

Resposta:

```json
{
  "token": "jwt_token"
}
```

---

### Listar Músicas

```http
GET /musicas
```

Header:

```http
Authorization: Bearer SEU_TOKEN
```

Resposta:

```json
[
  {
    "id": 1,
    "titulo": "Música A",
    "artista": "DJ A"
  },
  {
    "id": 2,
    "titulo": "Música B",
    "artista": "DJ B"
  }
]
```

---

## ⚙️ Configuração do Ambiente

### Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/sistema-musica.git
cd sistema-musica
```

### Criar Ambiente Virtual

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Instalar Dependências

```bash
pip install -r requirements-dev.txt
```

O arquivo de desenvolvimento instala as dependências da aplicação e o Pytest.

### Executar os Testes

```bash
pytest -q
```

A suíte cobre os serviços de autenticação e músicas, as rotas HTTP (incluindo
acesso JWT ao catálogo) e a renderização dos formulários e controles da página
principal. Os dados de usuários são limpos entre os testes.

---

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
JWT_SECRET_KEY=sua-chave-secreta
```

---

## ▶️ Executando o Projeto

```bash
python run.py
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:5000
```

---

## ☁️ Deploy

O projeto pode ser hospedado no Render. Configure no serviço:

* Build Command: `pip install -r requirements.txt`
* Start Command: `gunicorn run:app`
* Variável de ambiente `JWT_SECRET_KEY` com uma chave secreta forte

### Integração Contínua e Deploy Automático

O workflow `.github/workflows/ci-cd.yml` executa em pull requests e pushes para
`main` ou `master`. Ele instala as dependências de desenvolvimento e roda
`pytest -q`. Em push para essas branches, o deploy no Render é acionado somente
se os testes passarem.

Para habilitar o deploy automático:

1. No Render, abra o serviço web, crie um Deploy Hook e copie a URL gerada.
2. No GitHub, abra `Settings > Secrets and variables > Actions > New repository secret`.
3. Crie o secret `RENDER_DEPLOY_HOOK_URL` e cole nele a URL do Deploy Hook.
4. Envie as alterações para a branch principal (`main` ou `master`). O resultado
  dos testes e do deploy ficará disponível na aba `Actions` do GitHub.

Não coloque a URL do Deploy Hook nem a chave JWT no código ou em arquivos versionados.

---

## 🔮 Melhorias Futuras

* Integração com PostgreSQL
* Cadastro de artistas
* Cadastro de playlists
* Upload de músicas
* Upload de capas
* Busca por BPM
* Busca por tonalidade musical
* Histórico de execuções
* Dashboard para DJs
* Controle de eventos e apresentações

---

## 👨‍💻 Autor

Desenvolvido por Iran Ferreira.

Curso: Sistemas para Internet - UERN

```
```