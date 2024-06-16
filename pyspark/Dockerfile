FROM ubuntu:18.04

RUN mkdir /opt/ml
COPY requirements.txt feature_assembler.model reg_model.model string_indexer.model app.py WeightPredictor.py /opt/ml 

# ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
# ENV PYSPARK_SUBMIT_ARGS="--master local[2] pyspark-shell"

# #install java for pyspark
# RUN apt-get update \
#     # && add-apt-repository ppa:openjdk-r/ppa \
#     && apt-get install -y default-jre \
#     && apt-get install -y --no-install-recommends openjdk-11-jre-headless python3-pip \ 
#     && apt-get autoremove -yqq --purge \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# Install "software-properties-common" (for the "add-apt-repository")
RUN apt-get update && apt-get install -y \
    software-properties-common
# Add the "JAVA" ppa
RUN add-apt-repository -y \
    ppa:webupd8team/java

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer


# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
ENV PYSPARK_SUBMIT_ARGS="--master local[2] pyspark-shell"

#install python pip
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

#install requirements.txt
RUN pip3 install -r /opt/ml/requirements.txt

WORKDIR /opt/ml
CMD ["python3", "app.py"]
