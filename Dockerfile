FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make run.sh executable
RUN chmod +x run.sh

RUN apt-get update -y \
 && apt-get upgrade -y pip \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

# Expose port 9092 to the outside world
EXPOSE 9092

# Run run.sh when the container launches
CMD ["./run.sh"]