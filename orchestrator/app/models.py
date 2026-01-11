from sqlalchemy import Column, Integer, String, JSON, TIMESTAMP, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String(64), index=True, nullable=True)
    type = Column(String(64), index=True)
    status = Column(String(32), index=True)
    payload = Column(JSON)
    result = Column(JSON, nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))
    updated_at = Column(TIMESTAMP, server_default=text("NOW()"))

class Pipeline(Base):
    __tablename__ = "pipelines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True, index=True)
    description = Column(String)
    config = Column(JSON)
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))

class KPI(Base):
    __tablename__ = "kpi"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), index=True)
    value = Column(String)
    meta = Column('metadata', JSON)
    collected_at = Column(TIMESTAMP, server_default=text("NOW()"))

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(64))
    level = Column(String(16))
    message = Column(String)
    context = Column(JSON)
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))
