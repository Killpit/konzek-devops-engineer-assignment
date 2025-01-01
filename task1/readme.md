# Task 1 Documentation

- This documentation contains necessary knowledge about the application and instructions for deploying and verifying the service

### Contents

- Application code for Python HTTP server, a simple JSON file and simple HTTP code that shows an output if reached by localhost:3000
- Systemd unit file
- Instructions for deploying and verifying the service (in this readme file)

## Instructions for deploying and verifying the service

- Setup virtual environment for Python
- Test the application locally by using python3 main.py and opening a browser such as Chrome and writing localhost:3000 and getting a response
- Test the application with unit testing to further validate the application is working
Testing application is combined into another step as both of them cannot be tested independently from each other
- Writing the systemd and deploying the application using systemd and ensuring it starts automatically on boot

### Setup virtual environment for Python

- Go to task 1 directory with cd path/konzek-devops-engineer-assignment/task1 command
- Create the virtual environment with python3 -m venv venv
- Then go to venv directory with cd venv
- And then activate the virtual environment (venv) with source path/konzek-devops-engineer-assignment/task1/venv/bin/activate for Bash,
activating with Fish source path/konzek-devops-engineer-assignment/task1/venv/bin/activate.fish, or with 
PowerShell: source path/konzek-devops-engineer-assignment/task1/venv/bin/Activate.ps1
As an additional note, to activate the virtual environments, wither Fish, Bash or PowerShell should be installed and this task is made by using Bash in Linux
- venv is used as the virtual environment as the application expected at assignment was supposed to be a simple one

### Testing the application locally

- After following the instructions to activate the virtual environment, write python3 main.py to activate the HTTP Server and the open up a browser and write localhost:3000 or writing localhost:3000/books as an example to test the application locally

### Deploying Systemd Service and Automatically Starting on Boot

#### Enable the Service to Start on Boot

- Reload systemd to recognize the new unit file with sudo systemctl daemon-reload
- Enable the service to start on boot with sudo systemctl enable http-server
- Start the service with sudo systemctl start http-server
- Check the status of the service with sudo systemctl status http-server

#### Verify the Service

- cat /var/log/http-server.log (Standard Logs)
- cat /var/log/http-server-error.log (Error Logs)

Restarting machine to verify services are starting on boot:

- sudo reboot
