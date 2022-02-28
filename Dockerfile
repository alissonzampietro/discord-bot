FROM python:3

WORKDIR /usr/src/app
COPY . .
RUN apt update
RUN apt install ffmpeg -y
RUN apt install cron -y
RUN chmod +x -R audios/
RUN chmod +x runCron.sh
RUN chmod +x start.sh
RUN cp runCron.sh /usr/bin/runCron.sh
RUN cp cron /etc/cron.d/bot-cron
RUN pip install --no-cache-dir -r requirements.txt
RUN crontab /etc/cron.d/bot-cron
CMD ["bash", "./start.sh"]