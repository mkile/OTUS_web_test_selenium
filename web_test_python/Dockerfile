FROM python:3.9-alpine

WORKDIR app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "--url", "http://opencart", "--oc_adm_name", "user", "--oc_adm_pass", "bitnami", "-v"]
# CMD ["python3", "survey.py"]