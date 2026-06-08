# Trakito

## Discord Bot

### Commands

Activate virtual environment
- `source .venv/bin/activate`

Install packages from `requirements.txt`
- `pip install -r requirements.txt`

Update `requirements.txt`
- `pip freeze > requirements.txt`

Run app
- `python app/main.py`

Check for code issues:
- `ruff check`

Auto-fix lint errors: 
- `ruff check --fix`

Format your code: 
- `ruff format`

Docker Build:
- `docker build -t trackito-bot-image .`

Docker Run:
 ```
    docker run -d \
    --name trackito-bot \
    -e DISCORD_TOKEN="your_actual_discord_bot_token_here" \
    --restart unless-stopped \
    trackito-bot-image
```