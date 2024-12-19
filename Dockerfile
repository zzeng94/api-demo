# Start with a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that your application will run on
EXPOSE 8080

# Command to run the application using uvicorn (the production server for FastAPI)
# Adjust host and port as needed. Cloud Run expects the server to run on 0.0.0.0:8080
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8080"]