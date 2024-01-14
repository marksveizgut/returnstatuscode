FROM python:3.11.7-slim-bullseye
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]