# Subnet Manager

![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-v4.5.2-purple.svg)
![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.18.2-blue.svg)
![Docker](https://img.shields.io/badge/Docker-v19.03.12-blue.svg)
![Minikube](https://img.shields.io/badge/Minikube-v1.11.0-orange.svg)
![Python](https://img.shields.io/badge/Python-v3.8.3-yellow.svg)

## French Documentation 🇫🇷

For the French version of the documentation, see [README_fr.md](README_fr.md).

## Introduction

Subnet Manager is a comprehensive web-based application designed to simplify the management of network subnets. It offers CRUD (Create, Read, Update, Delete) functionalities, enabling users to efficiently handle subnet data. The backend of the application is built using Flask, a lightweight WSGI web application framework in Python. For the frontend, Bootstrap is utilized to create a responsive and clean user interface. The application is containerized using Docker and deployed on a local Kubernetes cluster managed by Minikube, ensuring a robust and scalable deployment environment.

## Features

- **Create Subnet:** Add new subnets with a unique ID, name, and CIDR block.
- **View Subnets:** View a list of all created subnets in a structured table.
- **Update Subnet:** Edit the details of an existing subnet.
- **Delete Subnet:** Remove a subnet from the list.

## Project Structure

```plaintext
subnet-manager/
├── app.py
├── Dockerfile
├── deployment.yaml
├── README.md
├── requirements.txt
├── service.yaml
└── templates/
    └── index.html
```

- **app.py:** The main Flask application file that initializes the app and defines the routes for creating, reading, updating, and deleting subnets.
- **templates/index.html:** The HTML template for the frontend, styled with Bootstrap, which provides the UI for interacting with subnets.
- **Dockerfile:** The Docker configuration file for containerizing the application. It defines the environment and commands for building the Docker image.
- **deployment.yaml:** The Kubernetes deployment configuration for managing pods. It specifies how many replicas of the application should run and how they should be deployed.
- **service.yaml:** The Kubernetes service configuration for exposing the application. It defines how the application is exposed within the cluster and to external users.
- **requirements.txt:** List of Python dependencies required for the project. This file is used to install all necessary Python packages.
- **README.md:** This documentation file.

## Installation

### Prerequisites

- Python 3.x
- Docker
- Minikube
- Kubernetes CLI (kubectl)
- Git

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/hn0a/subnet-manager.git
   cd subnet-manager
   ```
   This command downloads the repository to your local machine and navigates into the project directory.

2. **Set up the virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
   These commands create and activate a virtual environment to manage the project's dependencies separately from your system's Python installation.

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   This command installs all the necessary Python packages listed in the `requirements.txt` file.

4. **Run the Flask application locally:**
   ```sh
   python3 app.py
   ```
   This command starts the Flask development server, allowing you to test the application locally.

5. **Containerize the application:**
   ```sh
   docker build -t subnet-manager .
   ```
   This command builds a Docker image for the application using the instructions in the `Dockerfile`.

6. **Deploy on Minikube:**
   ```sh
   minikube start
   minikube docker-env
   eval $(minikube -p minikube docker-env)
   docker build -t subnet-manager .
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   minikube service subnet-manager --url
   ```
   These commands start Minikube, set up the Docker environment within Minikube, build the Docker image inside Minikube, and deploy the application using Kubernetes configurations.

## Usage

### Adding a Subnet

To add a subnet, use the form on the main page. Enter the subnet ID, name, and CIDR, then click "Add Subnet". The new subnet will appear in the list below.

### Viewing Subnets

The main page displays a table of all subnets. Each row contains the subnet ID, name, CIDR, and action buttons.

### Updating a Subnet

Click the "Edit" button next to a subnet to update its details. Modify the information in the form and click "Update".

### Deleting a Subnet

Click the "Delete" button next to a subnet to remove it. The table will update automatically to reflect the change.

## Troubleshooting

### Common Issues

1. **Pods not running:**
   - **Cause:** The image might not be correctly built or deployed.
   - **Error Message:** 
     ```shell
     kubectl get pods
     ```
     Output:
     ```
     NAME                             READY   STATUS             RESTARTS   AGE
     subnet-manager-d84c64476-lf85x   0/1     ErrImagePull       0          3m14s
     subnet-manager-d84c64476-mrrlv   0/1     ImagePullBackOff   0          3m14s
     subnet-manager-d84c64476-slng8   0/1     ErrImagePull       0          3m14s
     ```
   - **Solution:** 
     ```sh
     kubectl describe pod <pod-name>
     ```
     This command helps diagnose the error by providing detailed information about the pod's state. Ensure the image is correctly built and accessible.

2. **Service unreachable:**
   - **Cause:** The service might not be correctly exposed.
   - **Error Message:** 
     ```shell
     minikube service subnet-manager --url
     ```
     Output:
     ```
     ❌  Exiting due to SVC_UNREACHABLE: service not available: no running pod for service subnet-manager found
     ```
   - **Solution:** 
     ```sh
     minikube service list
     ```
     Ensure the service is correctly exposed. This command lists all services running in Minikube and their URLs.

3. **Database not updating:**
   - **Cause:** There might be errors in the Flask application.
   - **Error Message:** Check console output for specific errors.
   - **Solution:** Verify that the Flask app is running without errors. Check the console output for any issues.

### Error Logs

Check the logs of the Flask application for any errors:
```sh
kubectl logs <pod-name>
```
This command retrieves the logs for a specific pod, which can help identify any issues within the application.

## Challenges and Solutions

### Image Pull Errors

**Issue:** We encountered issues with pulling the Docker image due to incorrect configurations.

**Error Message:**
```shell
kubectl get pods
```
Output:
```
ErrImagePull
```

**Solution:** To resolve this, we built the image directly inside Minikube:
```sh
eval $(minikube -p minikube docker-env)
docker build -t subnet-manager .
```
This approach ensures that the image is available in the Minikube environment and can be pulled by the Kubernetes pods.

### Kubernetes Deployment Issues

**Issue:** Several issues were encountered related to Kubernetes deployments, such as pods not starting due to image pull errors or misconfigurations in the deployment YAML files.

**Error Message:**
```shell
kubectl get pods
```
Output:
```
ImagePullBackOff
```

**Solution:** We fixed these issues by:
1. Ensuring the correct Docker image was used.
2. Applying the correct Kubernetes configurations.
3. Using `kubectl describe pod <pod-name>` to diagnose and resolve errors.

### Frontend Update Issues

**Issue:** The frontend initially did not update automatically after performing CRUD operations.

**Solution:** This was resolved by using JavaScript to dynamically fetch and update the subnet list. We implemented AJAX calls to refresh the subnet data without reloading the entire page.

## Conclusion

This project demonstrates a complete workflow from development to deployment of a web-based subnet management application. It covers containerization with Docker, orchestration with Kubernetes, and deployment on a local Minikube cluster. This project serves as a practical example for managing and deploying modern web applications.

Feel free to contribute to this project by opening issues and submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** This README is intended to provide a comprehensive overview of the Subnet Manager project, guiding users through installation, usage, troubleshooting, and contributing. By following the steps outlined, users can easily set up and deploy the application, and gain insights into the project's structure and functionality.
