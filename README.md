## piper-compute

Piper-compute is piper's arm that is responsible for starting and stopping
services and running general compute services. It is meant to be agnostic to
different cloud platforms, although for now it's based off of AWS EC2.


### setup

Dependencies:
- packer: `$ brew install packer`


TODOS:

[ ] - set up basic packer image that can be started / stopped
[ ] - set up simple api gateway endpoint to start / stop resource
[ ] - set up simple api gateway endpoint to list current status
[ ] - set up 
