# Spark with Hive Metastore

## Intro
This repo builds an Apache Spark container image with Hive metastore built-in. The `docker-compose.yml` sets up all the required components to run a fully functional Spark with Hive metastore-enabled system. The Hive metastore data is persisted using a Postgres instance. 

Thanks to [big-data-europe](https://github.com/big-data-europe) since the base image is built from theirs.

Docker Hub link [here](https://hub.docker.com/repository/docker/gamberooni/spark-hive-metastore).

## Versions
1. Hadoop 3.2
2. Spark 3.1.1
3. Hive 3.1.2