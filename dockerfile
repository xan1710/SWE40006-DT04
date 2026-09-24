FROM python:3.13.5-slim
WORKDIR /app
COPY processor.py .
RUN useradd -m appuser && \
    mkdir -p /data/input /data/output && \
    chown -R appuser:appuser /data
USER appuser
CMD ["python", "processor.py"]