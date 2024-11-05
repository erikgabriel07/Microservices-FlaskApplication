![Static Badge](https://img.shields.io/badge/python-green)
![Last Commit](https://img.shields.io/github/last-commit/erikgabriel07/Microservices-FlaskApplication)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/erikgabriel07/Microservices-FlaskApplication)
![Contributors](https://img.shields.io/github/contributors/erikgabriel07/Microservices-FlaskApplication)

# Microsserviço para Processamento de Dados com FastAPI e Flask

## Tabela de conteúdo
- [Introdução](#introdução)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Rotas da API](#rotas-da-api)
- [Colaboradores](#colaboradores)

**Acesse e baixe o repositório [FastAPI](https://github.com/erikgabriel07/Microservices-FastAPI) para complementar esse projeto.**

## Introdução

Esse projeto é um microserviço criado utilizando FastAPI e Flask, onde as duas aplicações \
se comunicam entre si com o objetivo de processar arquivos de dados e realizar operações, \
como criar arquivo, inserir dados e deletar dados realizando operações no banco de dados.

## Tecnologias Utilizadas
- **FastAPI**: Utiliza FastAPI como API principal para o recebimento e processamento dos arquivos;

- **Flask**: Utilizado de forma complementar para realizar operações no banco de dados.

- **SQLAlchemy**: Biblioteca utilizada para a conexão e manipulação do banco de dados.

## Instalação
### 1. Clonar repositório
```bash
git clone https://github.com/erikgabriel07/Microservices-FlaskApplication
```

### 2. Criar ambiente virtual
#### Windows
```bash
cd Microservices-FlaskApplication
python -m venv venv
venv\Scripts\activate
```
#### Linux
```bash
cd Microservices-FlaskApplication
python -m venv venv
venv\bin\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
Execute as duas aplicações em terminais diferentes após concluir a instalação. \
A aplicação FastAPI estará disponível em `http://localhost:8000` enquanto que
a aplicação Flask estará disponível em `http://localhost:5000`.

## Rotas da API
### FastAPI
- **POST**: Envia um arquivo CSV para ser processado.
- **GET**: Obtém os dados armazenados no banco de dados.

### Flask
- **POST**: Cria um novo arquivo de dados.
- **PATCH**: Define dados do banco de dados como excluído ou duplicado.

## Subindo o docker
Para criar o container da aplicação, execute: ```docker-compose up -d``` \
O container estará servindo na porta `5000` para o Flask.

## Colaboradores

Agradecimentos aos colaboradores desse projeto:

<p align="left">
  <a href="https://github.com/erikgabriel07" style="margin-right: 20px; text-align: center;">
    <img src="https://github.com/erikgabriel07.png?size=100" alt="Erik Gabriel" width="100" />
  </a>
  <a href="https://github.com/jrdiasdev" style="margin-right: 20px; text-align: center;">
    <img src="https://github.com/jrdiasdev.png?size=100" alt="Jr. Dias" width="100" />
  </a>
  <a href="https://github.com/ryanricardoo" style="margin-right: 20px; text-align: center;">
    <img src="https://github.com/ryanricardoo.png?size=100" alt="Ryan Ricardo" width="100" />
  </a>
  <a href="https://github.com/bispoalef" style="margin-right: 20px; text-align: center;">
    <img src="https://github.com/bispoalef.png?size=100" alt="Bispo Alef" width="100" />
  </a>
  <a href="https://github.com/LucasFaars" style="margin-right: 20px; text-align: center;">
    <img src="https://github.com/LucasFaars.png?size=100" alt="Lucas Farias" width="100" />
  </a>
</p>

## License
This project is licensed under the [GNU License](LICENSE).
