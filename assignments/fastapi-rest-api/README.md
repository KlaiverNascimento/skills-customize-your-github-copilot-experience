# 📘 Atividade: Construindo uma API REST com FastAPI

## 🎯 Objetivo

Aprenda os fundamentos de APIs REST criando uma API para gerenciar tarefas com FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## Pré-requisitos e execução

Instale as dependências:

```bash
python -m pip install fastapi uvicorn
```

Na pasta da atividade, inicie o servidor:

```bash
uvicorn starter-code:app --reload
```

Abra `http://127.0.0.1:8000/docs` no navegador para testar os endpoints pela documentação interativa do FastAPI.

## 📝 Tarefas

### 🛠️ Criar e Consultar Tarefas

#### Descrição

Implemente os modelos de dados e as rotas para criar tarefas e consultar uma tarefa específica ou a lista completa.

#### Requisitos

O programa concluído deve:

- Usar modelos Pydantic para validar os dados de entrada e representar uma tarefa com `id`, `title`, `description` e `completed`.
- Implementar `GET /tasks` para retornar todas as tarefas.
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa pelo identificador ou responder com HTTP 404 quando ela não existir.
- Implementar `POST /tasks` para criar uma tarefa, atribuir um identificador e responder com HTTP 201.

### 🛠️ Atualizar e Remover Tarefas

#### Descrição

Complete a API implementando as operações para substituir e remover tarefas existentes, mantendo respostas HTTP consistentes.

#### Requisitos

O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente e responder com HTTP 404 quando o identificador não existir.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente e responder com HTTP 404 quando ela não existir.
- Responder ao `DELETE` bem-sucedido com HTTP 204 e sem corpo.
- Manter os dados em memória durante a execução do servidor; os dados podem ser reiniciados quando o servidor parar.
