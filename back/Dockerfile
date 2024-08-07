FROM python:latest

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Bundle app source
COPY . .

# Install app dependencies
RUN pip install -r requirements.txt
RUN python /reguser/manage.py migrate

# Expose port
EXPOSE 8000

