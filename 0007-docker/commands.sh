docker run --name firsh-hello hello-world
docker inspect <container-id>
docker rename firsh-hello second-hello
docker rm second-hello
# borra todos los contenedores que no se están usando
docker container prune
# metodo interactivo
docker run -it <container-image>
# renombrar contenedor, ejecutarlo en background y mandar un comando
docker run --name <container-name> -d ubuntu tail -f /dev/null
# ejecutar un contenedor que está corriendo actualmente
docker exec -it <container-name> bash
# veo el main process del ubuntu
docker inspect --format '{{.State.Pid}}' <container-name>
# matar el process del contenedor
kill -9 number
# exponer puertos
docker run --name proxy -d -p 8080:80 nginx -d
# viendo los logs
docker logs <container-name>
# para manteneres enchufado a los logs
docker logs -f <container-name>
# par ano traer todos los logs sino los utlimos
docker logs --tail 10 -f <container-name>
# sincronizar una carpeta del contenedor con la maquina local
docker run -d --name db -v <local-folder>:<container-folder> mongo
# lista de los volumenes
docker volume ls
# crear un volumen
docker volume create <volume-name>
# montar un volumen
docker run -d --name db --mount src=<volume-name>,dst=<container-folder> mongo
# copiar archivos a un contenedor
docker cp <file-name> <container-name>:<container-path>
docker cp <container-name>:<container-path> <file-name>
# listar imagenes
docker image ls
# traer una imagen especificando version en el tag
docker pull <image-name>:<version>
# Dockerfile para crear una imagen
# login local
docker login
# ver la estructura de creación de la imagen
docker history <image-name>
# https://github.com/wagoodman/dive
# borrar el container cuando se detenga
docker run --rm ...
# listar las conecciones
docker network ls
# creo la red
docker network create --atachable plazinet
# veo toda la definición de la red creada
docker inspect plazinet
# creo el contenedor de la BBDD
docker run -d --name db mongo
# conecto el contenedor “db” a la red “platzinet”
docker network connect plazinet db
# corro el contenedor “app” y le paso una variable
docker run -d -name app -p 3000:3000 --env MONGO_URL=mondodb://db:27017/test platzi
# conecto el contenedor “app” a la red “plazinet”
docker network connect plazinet app
# limitar los recursos
--memory 1g
docker stast