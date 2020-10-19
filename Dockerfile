FROM python:3.8

WORKDIR /web
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run backend
CMD [ "python3", "server.py" ]