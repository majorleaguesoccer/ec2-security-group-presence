FROM busybox

MAINTAINER Justin Slattery <justin.slattery@mlssoccer.com>

RUN mkdir -p /etc/ssl/certs
ADD ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

RUN mkdir -p /etc/boto
ADD endpoints.json /etc/boto/endpoints.json
ADD boto.cfg /etc/boto.cfg

ADD ./security-group-presence /bin/security-group-presence

ENTRYPOINT ["/bin/security-group-presence"]
