# Step 1: Use an official, lightweight Python base image
FROM python:3.13-slim

# Step 2: Set environment variables for optimized Python execution
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr (critical for viewing bot logs instantly)
ENV PYTHONUNBUFFERED=1

# Step 3: Create a non-root user and group for security
RUN addgroup --system botgroup && adduser --system --group botuser

# Step 4: Set the working directory inside the container
WORKDIR /discord

# Step 5: Copy dependencies file first to leverage Docker build caching
COPY requirements.txt .

# Step 6: Install dependencies without storing the pip cache
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Step 7: Copy the actual bot code into the container
COPY ./app /discord/app

# Step 8: Transfer ownership of the directory to the non-root user
RUN chown -R botuser:botgroup /discord

# Step 9: Switch to the non-root user
USER botuser

# Step 10: Run the bot using the Exec form (enables graceful shutdown)
CMD ["python", "app/main.py"]