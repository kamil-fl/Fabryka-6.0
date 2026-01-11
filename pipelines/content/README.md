# Pipelines Fabryki — Content Pipeline

Pipeline do automatyzacji procesu tworzenia i publikacji treści:
- tworzenie i research,
- optymalizacja SEO,
- publikacja na docelowych kanałach,
- monitorowanie i zbieranie metryk.

Struktura pipeline (przykład):

- `workflow.yml` / `workflow.json`
- `nodes/`
- `scripts/`
- `tests/`

Metryki przykładowe:
[
	{ "name": "organic_traffic", "source": "GA4", "goal": "max" },
	{ "name": "youtube_watch_time", "source": "YouTube", "goal": "max" },
	{ "name": "email_open_rate", "source": "MailerLite", "goal": "max" },
	{ "name": "sales_conversion", "source": "Shop", "goal": "max" }
]

# Proxy

Reverse proxy i certyfikaty obsługiwane są przez:
- obraz `nginxproxy/nginx-proxy`
- obraz `nginxproxy/acme-companion`

Konfiguracja odbywa się przez labele w `docker-compose.yml`.
Nie ma potrzeby tworzenia własnego `nginx.conf`.