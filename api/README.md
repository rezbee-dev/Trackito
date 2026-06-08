# Trakito - FastAPI Backend

### Commands

Activate virtual environment
- `source .venv/bin/activate`

Install packages from `requirements.txt`
- `pip install -r requirements.txt`

Update `requirements.txt`
- `pip freeze > requirements.txt`

Run app
- `fastapi run`

Check for code issues:
- `ruff check`

Auto-fix lint errors: 
- `ruff check --fix`

Format your code: 
- `ruff format`

Docker Build:
- `docker build -t trackito-api-image .`

Docker Run:
- `docker run -d --name trackito-api -p 8080:8080 trackito-api-image`

Docker Stop Container:
- `docker stop fastapi-container`

Docker Start Container:
- Must run the dockerfile first, so container can be created
- `docker start fastapi-container`