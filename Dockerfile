# Use a smaller base image with dependencies for Python
FROM python:3.9-slim-buster

WORKDIR /app

# Copy only the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install system dependencies and pip dependencies
RUN apt-get update --fix-missing \
    && apt-get install -y build-essential libssl-dev libffi-dev python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  \
    && pip install --no-cache-dir -r requirements.txt

# Copy the remaining app files
COPY . /app/

EXPOSE 8501

# Set Streamlit server address and port as environment variables
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Command to run the application
CMD ["streamlit", "run", "app.py"]
