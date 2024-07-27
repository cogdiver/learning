#!/bin/bash

docker compose up -d --build
docker exec -it neo4j_py_client bash
