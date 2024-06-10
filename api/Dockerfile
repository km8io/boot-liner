FROM cgr.dev/chainguard/python:latest-dev as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --user



FROM cgr.dev/chainguard/python:latest

LABEL org.opencontainers.image.source="https://github.com/km8io/boot-liner"

WORKDIR /app

# Make sure you update Python version in path
COPY --from=builder /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages

COPY main.py .

EXPOSE 8888/udp

ENTRYPOINT [ "python", "/app/main.py" ]
