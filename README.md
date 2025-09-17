# Ticket System

Sistema de gerenciamento de tickets desenvolvido como prática da disciplina de **Manutenção de Software**.

## Sobre o Projeto

Este projeto é uma API REST desenvolvida em Django para gerenciar um sistema de tickets de eventos, incluindo cadastro de clientes, eventos, vendas de ingressos e notificações.

## Tecnologias Utilizadas

- **Python 3.12**
- **Django 5.2**
- **Django REST Framework**
- **SQLite** (banco de dados padrão)

## Estrutura do Sistema

O sistema é composto por 4 aplicações principais:

### 📅 Events
- Gerenciamento de eventos
- Campos: nome, descrição, data, localização

### 👥 Customers  
- Cadastro de clientes
- Campos: nome, email

### 🎫 Tickets
- Venda de ingressos
- Relaciona eventos e clientes
- Campos: evento, cliente, data de compra

### 🔔 Notifications
- Sistema de notificações para clientes
- Campos: cliente, mensagem, data de criação

## Instalação e Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/alexrbss/ticket-system.git
cd ticket-system
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install django djangorestframework
```

4. **Execute as migrações:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Inicie o servidor:**
```bash
python manage.py runserver
```

## API Endpoints

### Events
- `GET/POST /api/events/` - Listar/Criar eventos
- `GET/PUT/DELETE /api/events/<id>/` - Ver/Editar/Excluir evento

### Customers
- `GET/POST /api/customers/` - Listar/Criar clientes  
- `GET/PUT/DELETE /api/customers/<id>/` - Ver/Editar/Excluir cliente

### Tickets
- `GET/POST /api/tickets/` - Listar/Criar tickets
- `GET/PUT/DELETE /api/tickets/<id>/` - Ver/Editar/Excluir ticket

### Notifications
- `GET/POST /api/notifications/` - Listar/Criar notificações
- `GET/PUT/DELETE /api/notifications/<id>/` - Ver/Editar/Excluir notificação

## Contexto Acadêmico

Este projeto foi desenvolvido como atividade prática da disciplina de **Manutenção de Software**, com foco em:

- Estruturação de projetos Django com Class-based Views (CBVs)
- Implementação de APIs REST
- Organização modular de aplicações

## Autor

**Rubens Alexandre de Sousa** - [alexrbss](https://github.com/alexrbss)

---

*Projeto desenvolvido para fins acadêmicos - Disciplina de Manutenção de Software*
