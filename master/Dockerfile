FROM bde2020/spark-master:3.1.1-hadoop3.2

ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV PYSPARK_PYTHON=/usr/bin/python3

RUN rm $SPARK_HOME/jars/guava-14.0.1.jar	

# jars for s3
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.375/aws-java-sdk-bundle-1.11.375.jar \
    --output $SPARK_HOME/jars/aws-java-sdk-bundle-1.11.375.jar && \
    curl https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar \
    --output $SPARK_HOME/jars/hadoop-aws-3.2.0.jar && \
    curl https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.20/postgresql-42.2.20.jar \
    --output $SPARK_HOME/jars/postgresql-42.2.20.jar && \
    curl https://repo1.maven.org/maven2/com/google/guava/guava/27.0-jre/guava-27.0-jre.jar \
    --output $SPARK_HOME/jars/guava-27.0-jre.jar && \
    curl https://repo1.maven.org/maven2/net/java/dev/jets3t/jets3t/0.9.4/jets3t-0.9.4.jar \
    --output $SPARK_HOME/jars/jets3t-0.9.4.jar && \
    curl https://repo1.maven.org/maven2/io/delta/delta-core_2.12/1.0.0/delta-core_2.12-1.0.0.jar \
    --output $SPARK_HOME/jars/delta-core_2.12-1.0.0.jar

WORKDIR $SPARK_HOME
# COPY entrypoint.sh entrypoint.sh
COPY hive-site.xml conf/hive-site.xml

# Install Hive

# Allow buildtime config of HIVE_VERSION
ARG HIVE_VERSION
# Set HIVE_VERSION from arg if provided at build, env if provided at run, or default
# https://docs.docker.com/engine/reference/builder/#using-arg-variables
# https://docs.docker.com/engine/reference/builder/#environment-replacement
ENV HIVE_VERSION=${HIVE_VERSION:-3.1.2}

ENV HIVE_HOME /opt/hive
ENV PATH $HIVE_HOME/bin:$PATH

WORKDIR /opt

#Install Hive and PostgreSQL JDBC
RUN apk update && apk add wget procps && \
	wget https://archive.apache.org/dist/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz && \
	tar -xzvf apache-hive-$HIVE_VERSION-bin.tar.gz && \
	mv apache-hive-$HIVE_VERSION-bin hive && \
	wget https://jdbc.postgresql.org/download/postgresql-9.4.1212.jar -O $HIVE_HOME/lib/postgresql-jdbc.jar && \
	rm apache-hive-$HIVE_VERSION-bin.tar.gz && \
	apk del wget && \
	rm -rf /var/lib/apt/lists/*

# replace spark's hive and calcite jars with hive's to match versions
RUN rm $SPARK_HOME/jars/hive-* && \
    cp $HIVE_HOME/lib/hive-* $SPARK_HOME/jars/ && \
    cp $HIVE_HOME/lib/calcite-* $SPARK_HOME/jars/ && \
    rm -rf $HIVE_HOME

WORKDIR $SPARK_HOME
