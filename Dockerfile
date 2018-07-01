FROM python:latest
ADD . /whitefox-discord

RUN cd whitefox-discord && \
    pip install -r requirements.txt

CMD ["python3.6 /whitefox-discord/run.py"]