# lab05_birds

Starter project for the Birds / PostgreSQL / FastAPI assignment.

## Included
- `compose.db.yaml` with PostgreSQL + Adminer
- `.env` with database settings
- SQLModel models for Species, Bird and Birdspotting
- Repositories and routers
- `sql/manual_setup.sql` with manual SQL setup and the 3 assignment queries

## Run database
```bash
docker compose -f compose.db.yaml up -d
```

Adminer:
- URL: http://127.0.0.1:8080

Suggested Adminer connection values:
- System: PostgreSQL
- Server: postgres
- Username: user
- Password: password
- Database: bird_api

## Python setup
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run API
```bash
fastapi dev main.py
```

Open:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
