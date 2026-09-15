# Use official Python slim image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Train the model so the image is self-contained (model.pkl is not committed)
RUN python app/train.py

# Expose port 8000 (FastAPI default)
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]