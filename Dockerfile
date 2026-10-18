From python:3.10-slim

Workdir /app

RUN pip install --no-cache-dir flask

Copy app.py .

Expose 5000

CMD ["python", "app.py"]