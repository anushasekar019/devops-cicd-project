# devops-cicd-project

# DevOps CI/CD Pipeline Using Jenkins and Terraform

## Project Overview

This project demonstrates the implementation of a basic
CI/CD pipeline using Jenkins, GitHub, Docker and Terraform.

A Python Flask application is integrated with Jenkins to
automate source code checkout, dependency installation,
automated testing, Docker image building and deployment.

Terraform is used to provision Docker infrastructure
using Infrastructure as Code.

## Technologies Used

- Python Flask
- Git and GitHub
- Jenkins
- Docker
- Terraform
- Linux Fedora

## CI/CD Pipeline Stages

1. Source Code Checkout
2. Build
3. Automated Testing
4. Docker Image Build
5. Application Deployment
6. Deployment Verification

## Terraform Infrastructure

Terraform provisions:

- Docker Network
- Nginx Docker Image
- Nginx Docker Container

## Application URLs

- Flask Application: http://localhost:5000
- Health Check: http://localhost:5000/health
- Nginx Server: http://localhost:8081

## Execution

Run the Jenkins pipeline through the Jenkins dashboard.

For Terraform:

    cd terraform
    terraform init
    terraform validate
    terraform plan
    terraform apply

## Conclusion

The project demonstrates automated application
integration, testing, containerization and deployment
along with infrastructure provisioning using Terraform.
