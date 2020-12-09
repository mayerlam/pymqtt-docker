# pymqtt-docker
An mqtt kit for python run in docker.

## Reference
Before use that. You need to install docker in you system. You can clik [Docker](https://www.docker.com "Open")  to see All detail 

## Install
`sh ./build.sh`

## Usage
`docker run --name mqtt -v {$YOUR_MOUNT_DIR}:/mqtt_main/data/ -itd mayerlam/mqtt`

Then in your mount directory have create a file Connector.py. You can edit this file. Than run by:

`docker exec -it mqtt sh run.sh `
