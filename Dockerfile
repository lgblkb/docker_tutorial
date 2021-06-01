FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_APP=main

#COPY main.py .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
