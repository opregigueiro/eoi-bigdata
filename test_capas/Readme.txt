Dockerfile-1 y Dockerfile-2 solo difieren en la linea 9

Ejecutar:

 docker build -t capa_1 -f Dockerfile-1 .

Comprobar el tiempo que tarda en crearse la imagen "capa_1"

Ejecutar:

 docker build -t capa_2 -f Dockerfile-2 .

Comprobar el tiempo que tarda en crearse la imagen "capa_2"

¿Cual es la diferencia con respecto a la creación de capa_1?

Ejecutar:

 docker history capa_1
 docker history capa_2

Comprobar los IDs de las capas que se muestran en cada imagen

Ejecutar:

 docker rmi capa_1

Comprobar las capas que se borran con respecto a las capas que se han mostrado en "history"
(hay capas intermedias que no se muestran en el history)

Ejecutar:

  docker rmi capa_2

Comprobar las capas que se han borrado con las mostradas en "history" y con respecto a las borradas con la imagen capa_1
