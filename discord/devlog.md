# Development Log

**May 25, 2026 - Monday - rezbee**
- Project setup
  - `pyenv install 3.14.5`
  - Created project folder then CD'd into there
  - `pyenv local 3.14.5`
    - set python version for the folder
    - it created/ placed .python-version file automatically
  - `python -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install discord.py python-dotenv ruff`
  - `pip freeze > requirements.txt`
- Created discord bot token
- Add discord bot to server
- Initialized project and confirmed bot was connected

**May 29, 2026 - Friday**
- FastAPI setup
  - `pyenv local 3.14.5`
  - `python -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install "fastapi[standard]"`
  - `pip freeze > requirements.txt`
  - copied over `.gitignore` file from `discord` folder
  - create `main.py` with "hello world" GET route