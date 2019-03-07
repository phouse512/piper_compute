## piper-compute

Piper-compute is piper's arm that is responsible for starting and stopping
services and running general compute services. It is meant to be agnostic to
different cloud platforms, although for now it's based off of AWS EC2.


### setup

Dependencies:
- packer: `$ brew install packer`


Setting up AWS X509 certificates for creating custom ami images:

```
$ openssl genrsa 2048 > private-key.pem
$ openssl req -new -x509 -nodes -sha256 -days 365 -key private-key.pem -outform
PEM -out certificate.pem

# upload to aws
$ aws iam upload-signing-certificate --username piper_compute_dev --certificate-body
file://certificate.pem
```



TODOS:

[ ] - set up basic packer image that can be started / stopped
[ ] - set up simple api gateway endpoint to start / stop resource
[ ] - set up simple api gateway endpoint to list current status
[ ] - set up 
