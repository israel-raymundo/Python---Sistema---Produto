# 🛒 Sistema de Gestão de Pedidos

Projeto desenvolvido em Python com SQLite simulando um sistema de gestão de pedidos com controle de estoque.

## 📌 Funcionalidades

- Cadastro de produtos
- Controle de estoque
- Cadastro de clientes
- Criação de pedidos
- Cancelamento de pedidos com devolução automática ao estoque
- Histórico de pedidos mantido no banco de dados
- Validação de regras de negócio (ex: quantidade não pode ser zero)

## 🏗️ Arquitetura

O projeto foi organizado utilizando separação por responsabilidade:

- `main.py` → Interface e fluxo do sistema
- `database/` → Conexão e criação das tabelas
- `repositories/` → Camada de acesso ao banco de dados

Essa organização simula uma estrutura utilizada em projetos backend reais.

## 💾 Tecnologias Utilizadas

- Python 3
- SQLite3

## ▶️ Como executar

1. Clone o repositório
2. Execute:

```bash
python main.py
