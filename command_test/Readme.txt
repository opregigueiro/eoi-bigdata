Ejecutar:

 docker build -t cmd_example -f Dockerfile-1 .

 docker build -t entrypoint_example -f Dockerfile-2 .

 docker build -t command_example -f Dockerfile-3 .

cmd_example usa CMD, entrypoint_example usa solo ENTRYPOINT y command_example usa ambos

Ejecutar:

 docker run --rm cmd_example
 docker run --rm entrypoint_example
 docker run --rm command_example

Comprobar que se ejecuta lo mismo en ambos casos.

Volver a ejecutar el docker run de cada imagen pero añadiendo parametros para comprobar su funcionamiento

Al finalizar, borrar las imagenes:

 docker rmi cmd_example entrypoint_example command_example
