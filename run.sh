#!/usr/bin/env bash

script_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
rebuild=$1
arch="$(uname -m)"

python $script_path/helpers/arch.py -a $arch

if [ "$rebuild" = "-r" ]; then
    docker-compose -f $script_path/docker-compose.yml up --build
else
    docker-compose -f $script_path/docker-compose.yml up
fi