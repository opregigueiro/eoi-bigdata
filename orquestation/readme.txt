Crear el visualizador:

docker service create \
  --name=viz \
  --publish=8080:8080/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  dockersamples/visualizer

Crear el registro:  
docker service create --name registry --publish published=5000,target=5000 registry:2

Comprobar que los servicios están levantados:
docker service ls

Comprobar las imagenes en el registro:
curl http://localhost:5000/v2/_catalog

Desplegar docker-compose:
docker stack deploy --compose-file docker-compose.yml webapp

Añadir mas servicios:
docker service scale webapp_webpython=3

Añadir en el docker-compose.yml para iniciar con mas replicas por servicio:
      deploy:
        replicas: 2

Añadir un nombre a la imagen:
docker tag webapp:v2 127.0.0.1:5000/webapp:v2

Subir la imagen al registro:
docker push 127.0.0.1:5000/webapp:v2

Comprobar los servicios
docker stack services webapp

