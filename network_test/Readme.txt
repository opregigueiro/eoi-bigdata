Prueba 1:
Creamos 1 contenedor en la red por defecto y sin nombre para intentar conectarnos a él desde otro contenedor

Para crear el contenedor ejecutamos:

 docker run --rm -d alpine tail -f /dev/null

Comprobamos el nombre con:

 docker ps

Creamos un segundo contenedor y accedemos a él:

 docker run --rm -it alpine

Dentro del contenedor ejecutamos:

 ping -c 4 $nombre1

Donde $nombre1 es el nombre del primer contenedor que obtuvimos con "docker ps"

Al finalizar, salimos del segundo contenedor y matamos el primero:

 exit 

 docker kill $nombre1

Prueba 2:
Creamos 1 contenedor en la red por defecto y le especificamos un nombre para intentar conectarnos a él desde otro contenedor

Para crear el contenedor ejecutamos:

 docker run --rm -d --name test_net alpine tail -f /dev/null

Comprobamos que ahora el contenedor tiene el nombre que le hemos indicado:

 docker ps

Creamos un segundo contenedor y accedemos a él:

 docker run --rm -it alpine

Dentro del contenedor ejecutamos:

 ping -c 4 test_net

Al finalizar, salimos del segundo contenedor y matamos el primero:

 exit 

 docker kill test_net

 
Prueba 3:
Creamos una nueva red, y creamos un contenedor dentro de esta red sin indicar un nombre para el contenedor e intentamos conectarnos a él desde otro contenedor

Para crear la red:

 docker network create test_network

Para crear el contenedor ejecutamos:

 docker run --rm --network test_network -d alpine tail -f /dev/null

Comprobamos el nombre con:

 docker ps

Creamos un segundo contenedor y accedemos a él:

 docker run --rm --network test_network -it alpine

Dentro del contenedor ejecutamos:

 ping -c 4 $nombre1

Donde $nombre1 es el nombre del primer contenedor que obtuvimos con "docker ps"

Al finalizar, salimos del segundo contenedor, matamos el primero y borramos la red:

 exit 

 docker kill $nombre1

 docker network rm test_network

Prueba 4:
Creamos una nueva red, y creamos un contenedor dentro de esta red especificando un nombre para intentar conectarnos a él desde otro contenedor

Para crear la red:

 docker network create test_network

Para crear el contenedor ejecutamos:

 docker run --rm -d --network test_network --name test_net alpine tail -f /dev/null

Comprobamos que ahora el contenedor tiene el nombre que le hemos indicado:

 docker ps

Creamos un segundo contenedor y accedemos a él:

 docker run --rm --network test_network -it alpine

Dentro del contenedor ejecutamos:

 ping -c 4 test_net

Al finalizar, salimos del segundo contenedor, matamos el primero y eliminamos la red:

 exit 

 docker kill test_net

 docker network rm test_network
