FROM busybox

MAINTAINER Justin Slattery <justin.slattery@mlssoccer.com>

RUN mkdir -p /etc/ssl/certs
ADD ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
ADD ./security-group-presence /bin/security-group-presence

ENTRYPOINT ["/bin/security-group-presence"]
