FROM google/python

MAINTAINER Justin Slattery <justin.slattery@mlssoccer.com>

WORKDIR /app
RUN virtualenv /env
RUN /env/bin/pip install boto
ADD ./security-group-presence.py /app/security-group-presence.py

CMD []
ENTRYPOINT ["/env/bin/python", "/app/security-group-presence.py"]
