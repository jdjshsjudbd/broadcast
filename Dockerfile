FROM python:3.9
WORKDIR .
COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python3 -m main
