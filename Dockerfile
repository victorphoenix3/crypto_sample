# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /ContainerTask
WORKDIR /crypto_sample
COPY . /crypto_sample

# Install necessary tools
RUN apt-get update

# gcc is required to build pycrypto
RUN apt-get install -y gcc

# Install the necessary dependencies
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
