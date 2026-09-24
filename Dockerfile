FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/fizzbuzz/ ./fizzbuzz/
COPY src/demo.py ./

CMD ["python", "-m", "fizzbuzz"]
CMD ["python",  "demo.py"]
