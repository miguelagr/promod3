#!/bin/bash

echo "instalando base de datos"

apt-get install postgresql -y

apt-get install python-pip -y

pip install psycopg2-binary

echo "psql -f database.sql" | su postgres

export PATH=$PATH:$(pwd)
