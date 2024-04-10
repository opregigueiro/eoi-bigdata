Creamos dos contenedores y le asociamos el mismo volumen a los dos, pero en distintas rutas:

  docker run --rm -d --name testv1 -v test_v:/test      alpine tail -f /dev/null
  docker run --rm -d --name testv2 -v test_v:/workspace alpine tail -f /dev/null

Comprobamos los contenedores:

  docker ps

Entramos dentro del primer contenedor y creamos un fichero en la ruta donde hemos asociado el volumen:

 docker exec -it testv1 /bin/sh

 cd /test
 touch fichero_testv1

Comprobamos que hemos creado el fichero y salimos:

 ls
 exit

Entramos dentro del segundo contenedor y creamos un fichero en la ruta donde hemos asociado el volumen:

 docker exec -it testv2 /bin/sh

 cd /workspace
 touch fichero_testv2

Comprobamos que ficheros existen ahora en esa ruta y salimos:

 ls
 exit

Accedemos nuevamente el primer contenedor, comprobamos que existen los dos ficheros y salimos:

 docker exec -it testv1 /bin/sh

 cd /test
 ls
 exit

Matamos los dos contenedores:

  docker kill testv1 testv2

Creamos un nuevo contenedor asociando el volumen y comprobamos que siguen existiendo los dos ficheros:

 docker run --rm -it --name testv -v test_v:/comprobar alpine

 ls /comprobar

 exit

