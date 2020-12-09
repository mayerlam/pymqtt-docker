FROM python
RUN pip install paho-mqtt 
COPY template.py /etc/tmp/
COPY init.sh /
COPY run.sh /
CMD sh init.sh