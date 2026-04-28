from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Banco de dados temporário (lista na memória)
tarefas = []
proximo_id = 1

# Modelo de uma tarefa
class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False


# Listar todas as tarefas
@app.get("/tarefas")
def listar_tarefas():
    return tarefas


# Criar uma tarefa
@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    global proximo_id
    nova = {"id": proximo_id, "titulo": tarefa.titulo, "concluida": tarefa.concluida}
    tarefas.append(nova)
    proximo_id += 1
    return nova


# Atualizar uma tarefa
@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa):
    for t in tarefas:
        if t["id"] == tarefa_id:
            t["titulo"] = tarefa.titulo
            t["concluida"] = tarefa.concluida
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


# Deletar uma tarefa
@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    for i, t in enumerate(tarefas):
        if t["id"] == tarefa_id:
            tarefas.pop(i)
            return {"mensagem": "Tarefa deletada"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")