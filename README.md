# Microservice on Consul Example

The purpose of this example is to test service client how to find multiple microservices on consul.
In this case, include 1 front-end web, and 2 type back-end services that provide users and talks data APIs.
In the real world, front-end web never knows every services' address, and docker can scale by the requirement. On the other hand, the consul just a service register it didn't provide a logic to decide which service is proper for caller.

## Architecture

* web: 1
* user API: 2 (that can scale by docker-compose argument)
* talk API: 2 (that can scale by docker-compose argument)
* consul: default
* registrator: 1

## Install

* install Docker on your computer
* git clone this project


## Run 

* docker-compose -f docker_compose.yml up --scale microuser=2 --scale microtalk=2
* open http://localhost:8500/ui
    * check docker run completed and services register on consul. like the picture(#servicepage).
* open http://localhost:8080/ui
    * page will auto load data from APIs
    * check KV on consul. like the picture(#kvpage).

### servicepage
![Consul Service Page](https://github.com/PrinsWu/consul_microweb/data/Consul_services.jpg)

### kvpage
![Consul KV Page](https://github.com/PrinsWu/consul_microweb/data/Consul_kv.jpg)


