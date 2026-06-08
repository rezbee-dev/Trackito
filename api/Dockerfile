# Step 1: Use an official, lightweight Python base image
FROM python:3.13-slim

# Step 2: Set environment variables for optimized Python execution
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr (useful for logging)
ENV PYTHONUNBUFFERED=1

# Step 3: Create a non-root user for security
RUN addgroup --system appgroup && adduser --system --group appuser

# Step 4: Set the working directory inside the container
WORKDIR /api

# Step 5: Copy only dependencies first to leverage Docker build caching
COPY requirements.txt .

# Step 6: Install dependencies without storing the pip cache
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Step 7: Copy the rest of the application code
COPY ./app /api/app

# Step 8: Transfer ownership of the directory to the non-root user
RUN chown -R appuser:appgroup /api

# Step 9: Switch to the non-root user
USER appuser

# Step 10: Expose the port the application will run on
EXPOSE 8000

# Step 11: Execute the application using the Exec form
CMD ["fastapi", "run", "app/main.py", "--port", "8080"]