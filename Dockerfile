# Layer 1: Base Image
FROM python:3.11-slim

# Layer 2: Workspace
WORKDIR /app

# Layer 3: Copy Files
COPY requirements.txt .
COPY app.py .

# Layer 4: Install Dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Layer 5: Startup
CMD ["python", "app.py"]
