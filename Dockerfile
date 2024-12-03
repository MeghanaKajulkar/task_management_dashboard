FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install system dependencies
RUN apt-get update --fix-missing \
    && apt-get install -y build-essential \
    && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

CMD ["streamlit", "run", "app.py"]
