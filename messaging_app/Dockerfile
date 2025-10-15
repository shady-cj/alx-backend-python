FROM python:3.10

WORKDIR /app

COPY requirements.txt .
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

