FROM apache/airflow:2.5.1

USER root

# Install Kafka dependencies
RUN apt-get update && \
    apt-get install -y default-jre && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Kafka Python package
RUN pip install kafka-python

USER airflow
