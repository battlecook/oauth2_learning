FROM python:3

RUN pip install --upgrade pip
RUN pip install flask requests

WORKDIR /opt/project

COPY . .
CMD ["run.py"]
ENTRYPOINT ["python3"]