FROM python:3.13

WORKDIR '/app'

COPY ../../core ./core
COPY ../../orphanage ./orphanage
COPY ../../templates ./templates
COPY ../../manage.py .
COPY ../../requirements.txt .
COPY ./docker/orphanage/runserver.sh .

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["/app/runserver.sh"]