#!/usr/bin/env python3
"""Insert a task into the Orchestrator DB using SQLAlchemy models.

Usage:
  python tools/create_task.py --type content.article_production --payload '{"title":"Test"}'

This script reads DATABASE_URL from the environment (load from .env if present).
"""
import os
import json
import argparse
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

from sqlalchemy.orm import Session

# Import app DB and models
from orchestrator.app.db import engine, SessionLocal
from orchestrator.app.models import Base, Task

Base.metadata.create_all(bind=engine)


def create_task(task_type: str, payload: dict):
    db: Session = SessionLocal()
    try:
        db_task = Task(type=task_type, status="created", payload=payload)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        print(json.dumps({"id": db_task.id, "status": db_task.status}))
    finally:
        db.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', required=True)
    parser.add_argument('--payload', default='{}')
    args = parser.parse_args()
    payload = json.loads(args.payload)
    create_task(args.type, payload)
