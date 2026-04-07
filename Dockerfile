# Layer 1: Base Image
# Refrigirated Containers? Containers with fans? Containers with a mat? 
# Sometimes they come in completely full!
FROM python:3.11-slim

# Layer 2: Workspace
# I need to put more stuff in it, where do I put it? 
WORKDIR /app

# Layer 3: Copy Files
# Put my stuff in the container!
COPY requirements.txt .
COPY app.py .

# Layer 4: Install Dependencies 
# Put more stuff in my container!
RUN pip install --no-cache-dir -r requirements.txt

# Layer 5: Startup
# Ship it :D
CMD ["python", "app.py"]
