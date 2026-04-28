# 📝 Todo API

API REST de lista de tarefas desenvolvida com Python e FastAPI.

## 🚀 Tecnologias
- Python 3.14.4
- FastAPI
- Uvicorn

## ⚙️ Como rodar localmente

1. Clone o repositório
```bash
   git clone https://github.com/theuxz/todo-api.git
   cd todo-api
```

2. Crie e ative o ambiente virtual
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Instale as dependências
```bash
   pip install fastapi uvicorn
```

4. Rode a API
```bash
   uvicorn main:app --reload
```

5. Acesse a documentação em: http://127.0.0.1:8000/docs

## 📌 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tarefas` | Lista todas as tarefas |
| POST | `/tarefas` | Cria uma nova tarefa |
| PUT | `/tarefas/{id}` | Atualiza uma tarefa |
| DELETE | `/tarefas/{id}` | Deleta uma tarefa |