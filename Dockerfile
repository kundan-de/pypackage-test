FROM python:3.12-slim

RUN pip install uv

WORKDIR /app

COPY . /app

RUN uv pip install .[dev] --no-cache-dir --system

EXPOSE 80

CMD ["uv", "run", "python", "main.py"]