#!/bin/bash

# Build and run the Docker container
docker build -t todo-app .
docker run -p 5000:5000 todo-app
