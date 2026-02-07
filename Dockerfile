# easy-1-ghost-login/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask flask-session
ENV FLAG=CTF{easy_ghost_login}
EXPOSE 5000
CMD ["python","app.py"]
