Ejecutar:
   
 docker build -t size_test1 -f Dockerfile-1 . 

 docker build -t size_test2 -f Dockerfile-2 . 

 docker build -t size_test3 -f Dockerfile-3 . 

Usando:
 
 docker images

Comprobar el tamaño de las 3 imagenes.

Al finalizar, borrar las 3 imagenes:

docker rmi size_test1 size_test2 size_test3 
