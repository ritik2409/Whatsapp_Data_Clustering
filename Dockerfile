FROM python:3
WORKDIR /usr/local/server
COPY ./server ./
RUN chmod 644 app.py
RUN python3 -m pip install gensim sklearn flask werkzeug nltk
RUN python -m nltk.downloader 'punkt'
CMD python app.py