from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .db import get_db, engine
from .models import Base, Task

Base.metadata.create_all(bind=engine)

app = FastAPI()

class TaskCreate(BaseModel):
    type: str
    payload: dict

class PipelineRunRequest(BaseModel):
    name: str
    params: dict | None = None

@app.get("/")
def root():
    return {"status": "ok", "service": "fabryka_orchestrator"}

@app.post("/task/create")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(type=task.type, status="created", payload=task.payload)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"id": db_task.id, "status": db_task.status}

@app.get("/task/status/{task_id}")
def task_status(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        return {"error": "not_found"}
    return {"id": db_task.id, "status": db_task.status, "result": db_task.result}

@app.post("/pipeline/run")
def pipeline_run(req: PipelineRunRequest):
    # TODO: integracja z n8n (webhook)
    return {"status": "scheduled", "pipeline": req.name, "params": req.params}

@app.post("/meta-agent/notify")
def meta_agent_notify(event: dict):
    # TODO: zapis eventu jako Log
    return {"status": "received"}
