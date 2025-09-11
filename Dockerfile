FROM python:3.12-slim

RUN pip install uv

WORKDIR /app

COPY . /app

RUN uv pip install . --no-cache-dir --system

CMD ["uv", "run", "python", "-m", "demo.main"]
