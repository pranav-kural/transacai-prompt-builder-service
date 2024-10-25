FROM python3
WORKDIR /app
COPY ./src /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "app.py"]