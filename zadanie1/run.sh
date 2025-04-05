#!/bin/bash

docker build -t app .
docker run --rm -it app
