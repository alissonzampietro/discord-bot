FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN apt update
RUN apt install ffmpeg -y
RUN chmod +x -R audios/
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]