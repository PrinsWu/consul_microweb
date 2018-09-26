*** Docker Stop All Containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq) 


****** This is work ******
docker run -d -p 8500:8500 consul consul agent -data-dir=/consul/data -config-dir=/consul/config -dev -client=0.0.0.0 -bind=0.0.0.0
docker run -d -p 8501:8500 consul consul agent -data-dir=/consul/data -config-dir=/consul/config -dev -client=0.0.0.0 -bind=0.0.0.0 -join 172.17.0.2
docker run -d -p 8502:8500 consul consul agent -data-dir=/consul/data -config-dir=/consul/config -dev -client=0.0.0.0 -bind=0.0.0.0 -join 172.17.0.2

------------------------------------------------------------
# https://www.cnblogs.com/zhangdk/archive/2018/07/25/ms1.html
# server 1
docker run -d --name server1 consul agent -server -node=server1 -bootstrap-expect=3
JOIN_IP="$(sudo docker inspect -f '{{.NetworkSettings.IPAddress}}' server1)"
# server 2
docker run -d --name server2 consul agent -server -node=server2 -join $JOIN_IP
# server 3
docker run -d --name server3 consul agent -server -node=server3 -join $JOIN_IP
# client 1
docker run -d --name client1 consul agent -node=client1 -join $JOIN_IP
# client 2
docker run -d --name client2 -p 8400:8400 -p 8500:8500 -p 8600:53/udp  consul agent -ui -node=client2 -client=0.0.0.0 -join $JOIN_IP

#Registrator
docker run -d --name registrator --net host --volume=/var/run/docker.sock:/tmp/docker.sock gliderlabs/registrator -internal consul://172.17.0.9:8500



** Docker Registrator
docker run -d --name=registrator --net=host --volume=/var/run/docker.sock:/tmp/docker.sock gliderlabs/registrator:latest consul://127.0.0.1:8500







** Service Register
curl --request PUT --data @payload.json http://localhost:8500/v1/agent/service/register

curl --request POST --data @query.json http://localhost:8500/v1/query
curl http://localhost:8500/v1/query


curl http://localhost:8500/v1/agent/services

curl http://localhost:8500/v1/catalog/services

curl http://localhost:8500/v1/health/checks/microuser

curl http://localhost:8500/v1/health/connect

** Consul Prepare Query
curl --request POST --data @prepare_query.json http://localhost:8500/v1/query
"ID": 3d8da2e5-4837-d95a-fb8d-b6d6db0ab7f9

** Consul Update Prepare Query
curl --request PUT --data @prepare_query.json http://127.0.0.1:8500/v1/query/faa52b08-a295-b20c-5d01-b237a46c9a2d
curl --request PUT --data @query.prefix.json http://127.0.0.1:8500/v1/query/19b62647-85c6-7390-0bcd-ef8ab6e025f7


** Consul Create Query
curl --request POST --data @query.json http://127.0.0.1:8500/v1/query
"ID": 0b6d8bc8-eea6-3072-40de-8ef6622526e1

curl --request POST --data @query_mt.json http://127.0.0.1:8500/v1/query
"ID": ccba8ab8-ffe7-7d7c-67d2-3ef5b239b582

curl --request POST --data @query_mu.json http://127.0.0.1:8500/v1/query
"ID": bcfceb40-2546-72ed-0ff7-27f0b8059e2c

curl --request POST --data @query_prefix.json http://127.0.0.1:8500/v1/query
"ID": f8db14b3-b040-aca2-4ca1-f461fbeff139


** Consul Update Query
curl --request PUT --data @query_prefix.json http://127.0.0.1:8500/v1/query/f8db14b3-b040-aca2-4ca1-f461fbeff139


** Consul Execute Query
curl http://127.0.0.1:8500/v1/query/prefix_search/execute?near=_agent

curl http://127.0.0.1:8500/v1/query/my-query-mt/execute?near=_agent

curl http://127.0.0.1:8500/v1/query/my-query-mu/execute?near=_agent

curl http://127.0.0.1:8500/v1/query/query_prefix/execute?near=_agent

curl http://127.0.0.1:8500/v1/query/name_prefix_match/execute?near=_agent

curl http://127.0.0.1:8500/v1/query/servicename_prefix_search/execute?near=_agent
curl http://127.0.0.1:8500/v1/query/3d8da2e5-4837-d95a-fb8d-b6d6db0ab7f9/execute?near=_agent

curl http://127.0.0.1:8500/v1/query/faa52b08-a295-b20c-5d01-b237a46c9a2d/execute?near=_agent

curl http://127.0.0.1:8500/v1/query/f8db14b3-b040-aca2-4ca1-f461fbeff139/execute?near=_agent


** Consul Delete Prepare Query
curl --request DELETE http://127.0.0.1:8500/v1/query/faa52b08-a295-b20c-5d01-b237a46c9a2d
curl --request DELETE http://127.0.0.1:8500/v1/query/19b62647-85c6-7390-0bcd-ef8ab6e025f7
curl --request DELETE http://127.0.0.1:8500/v1/query/f8db14b3-b040-aca2-4ca1-f461fbeff139



curl http://localhost:8500/v1/query
curl http://localhost:8500/v1/query/3d8da2e5-4837-d95a-fb8d-b6d6db0ab7f9
curl http://localhost:8500/v1/query/d701d04a-5205-f493-0848-7f00ebd71a70
curl http://localhost:8500/v1/query/faa52b08-a295-b20c-5d01-b237a46c9a2d
curl http://localhost:8500/v1/query/f8db14b3-b040-aca2-4ca1-f461fbeff139

