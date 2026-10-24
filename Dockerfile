FROM python:3.13-alpine
WORKDIR /app
COPY --chown=10001:10001 site/ /app/site/
USER 10001:10001
EXPOSE 8080
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 CMD ["python", "-c", "import urllib.request; r = urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2); assert r.status == 200 and r.read() == b'ok\\n'"]
CMD ["python", "-m", "http.server", "8080", "--bind", "0.0.0.0", "--directory", "/app/site"]
