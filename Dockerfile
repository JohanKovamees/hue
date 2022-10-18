FROM ubuntu:latest

RUN apt update && apt install -y python3-pip

WORKDIR /app
COPY hue-web.py /app
COPY req.txt /app

RUN pip3 install -r req.txt 

ENV FLASK_APP=hue-web
ENV FLASK_ENV=production
ENV HUE_IP="10.0.1.195"
ENV FLASK_DEBUG=0

RUN chmod +x hue-web.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
