FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app /app

# Expose port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
