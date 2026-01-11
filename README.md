# Fabryka 6.0

Fabryka 6.0 to wielowarstwowy system do automatycznej produkcji treści, produktów i kampanii,
oparty o Orchestratora (FastAPI + Postgres), n8n, agentów i Meta-Agenta.

## Szybki start

### 1. Lokalne przygotowanie (MacBook)

1. Sklonuj repozytorium lub utwórz je z tych plików.
2. Skopiuj `.env.example` do `.env` i uzupełnij `ACME_EMAIL`.
3. Wypchnij repozytorium na GitHuba.

### 2. Serwer produkcyjny (Mikrus 3.5)

Na Mikrusie 3.5 (Ubuntu 24.04):

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y ca-certificates curl git

# instalacja Docker + compose
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  noble stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
# wyloguj/zaloguj się, jeśli trzeba

cd /srv
git clone git@github.com:kamil-fl/Fabryka-6.0.git fabryka-systemu-6.0
cd fabryka-systemu-6.0
cp .env.example .env  # lub skopiuj gotowe .env z MacBooka
docker compose up -d
docker compose ps

```
# Fabryka 6.0 – WARSTWA 1 (Infrastruktura)
