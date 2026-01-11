# Agenci Fabryki — YouTube

Tutaj będą agenci odpowiedzialni za:
- przygotowanie metadanych wideo,
- optymalizację tytułów i opisów,
- upload i harmonogram,
- analizę czasu oglądania i zaangażowania.

Struktura agenta (przykład):

- `prompt.md`
- `schema.json`
- `handler.py`
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