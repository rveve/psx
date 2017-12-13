FROM  python:3
RUN pip install flask
EXPOSE 5000
ADD server.py /server.py
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
