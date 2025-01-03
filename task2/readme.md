# Task 2 Documentation

- This documentation contains necessary knowledge about the application and instructions for deploying and verifying the service

### Contents

- Application code for Python HTTP server, a simple JSON file and simple HTTP code that shows an output if reached by localhost:3000
- Systemd unit file
- Instructions for deploying and verifying the service

## Instructions for Docker-Based Application Deployment

#### Running the Dockerfile for Local Testing

- docker build -t task2-app .
- docker run -d -p 8000:8000 task2-app (for testing)
- docker push task-2-app

#### Testing and deploying with Docker Compose

- docker-compose up --scale app=3 (Starting services)
- Verify the application with http://localhost
- Check running containers with docker ps
- Check logs with docker-compose logs
- Test replica distribution with curl http://localhost
- Stop one replica manually with docker stop <container-id>
