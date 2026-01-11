#!/usr/bin/env python3
"""Call Orchestrator `/pipeline/run` endpoint.

Usage:
  python tools/run_pipeline.py --name content.article_production --params '{}'
"""
import os
import json
import argparse
from dotenv import load_dotenv
import requests

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

ORCH_HOST = os.getenv('ORCH_HOST', 'http://localhost:8000')


def run_pipeline(name: str, params: dict):
    url = f"{ORCH_HOST}/pipeline/run"
    payload = {"name": name, "params": params}
    resp = requests.post(url, json=payload)
    try:
        print(resp.status_code, resp.text)
    except Exception:
        print('Request failed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--params', default='{}')
    args = parser.parse_args()
    params = json.loads(args.params)
    run_pipeline(args.name, params)
