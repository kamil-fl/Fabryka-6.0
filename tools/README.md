Tools
=====

Scripts to help interact with Orchestrator when services are running.

- `create_task.py` — insert a task directly into the database using the project's SQLAlchemy models.
- `run_pipeline.py` — POST to `/pipeline/run` on the Orchestrator.

Examples
--------

Load env and create task:

```bash
python tools/create_task.py --type content.article_production --payload '{"title":"My Article"}'
```

Call pipeline endpoint:

```bash
python tools/run_pipeline.py --name content.article_production --params '{}'
```

Notes
-----
- Both scripts read `.env` from the repository root. Ensure `DATABASE_URL` and `ORCH_HOST` are set.
- If Docker services are not running, `create_task.py` will fail to connect to Postgres; run it after starting Postgres or point `DATABASE_URL` to a reachable DB.
- `run_pipeline.py` needs the Orchestrator HTTP service running.
