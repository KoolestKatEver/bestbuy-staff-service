# Staff Management REST API Microservice

## Overview
The `bestbuy-staff-service` is a REST API microservice built using Flask, designed to provide  CRUD (Create, Read, Update, Delete) operations for managing staff admin data. It supports storing and retrieving information such as IDs, names, positions, departments, emails, and phone numbers. 

## Functionality
- **Create Staff Records**: Adds new staff members to an in-memory database.
- **Retrieve Records**: Fetches single or multiple staff member records.
- **Update Staff Information**: Updates existing staff details based on the unique ID.
- **Delete Staff Records**: Removes staff entries by their ID.
- **Containerized Deployment**: Utilizes Docker to containerize the application for consistent and portable deployments.
- **Kubernetes Deployment**: Supports high availability and scaling using Kubernetes, with defined deployment and service configurations.

## Dockerfile Features
- **Dependency Management**: Installs application dependencies using `pip` with `requirements.txt`.
- **Application Port Exposure**: Exposes port `5000` for the Flask application within the container.
- **Command Execution**: Runs the `bestbuy-staff-service.py` application as the container’s entry point.

## Kubernetes Deployment Features
- **Deployment**:
  - Configures a `Deployment` resource to manage the application pods.

 
- **Service**:
  - Exposes the application as a `LoadBalancer` service for external accessibility.
  - Routes traffic from port `80` on the LoadBalancer to port `5000` in the container.

## Adherence to Twelve-Factor App Principles
1. **Codebase**: Version-controlled in Git, enabling multi-environment deployments.
2. **Dependencies**: Explicitly declared in `requirements.txt` and managed in an isolated containerized environment.
3. **Config**: Environment variables stored in `.env`, keeping sensitive data secure.
4. **Backing Services**: Uses an in-memory data store treated as an attached resource.
5. **Port Binding**: Exposes the service via port binding through Docker and Kubernetes configurations.
6. **Processes**: Executes the app as a stateless process managed through Kubernetes pods.

### Adherence to Twelve-Factor App Principles

1. **Codebase**: The microservice is version-controlled in a Git repository, ensuring that one codebase is tracked and can be deployed across multiple environments.

2. **Dependencies**: Dependencies such as Flask and python-dotenv are explicitly declared in the `requirements.txt` file, and isolated within the containerized environment using Docker.

3. **Config**: All configuration, such as the port and debug settings, is stored in environment variables file .env. This file is also incldued in .gitignore. 

4. **Backing Services**: The microservice uses an in-memory data store, treated as an attached resource. External databases or services can be integrated with minimal changes.

5. **Build, Release, Run**: The application lifecycle is strictly separated into build (Docker image creation), release (tagging the image), and run (deployment to Kubernetes).

6. **Processes**: The microservice runs as a stateless process, with all data stored in-memory or external backing services, ensuring that processes can scale horizontally.

7. **Port Binding**: The Flask application explicitly binds to a port (`5000` by default), exposing the service as an HTTP endpoint.

8. **Concurrency**: The application supports scaling out via Kubernetes deployments, where multiple instances of the microservice can run concurrently.

9. **Disposability**: The service ensures fast startup and graceful shutdown, facilitated by the lightweight Flask framework and Kubernetes orchestration.

10. **Dev/Prod Parity**: Development, staging, and production environments are kept as similar as possible by using the same Docker image and deployment configurations.

11. **Logs**: Application logs are treated as event streams and can be redirected to centralized logging systems like Kubernetes logs or external monitoring tools.

12. **Admin Processes**: Administrative tasks, such as debugging or migrations, can be executed as one-off processes using the same containerized environment.


---

## How to Use the Microservice

### Base URL
By default, the microservice runs on:
```
http://localhost:5000
```

### Endpoints

#### 1. **Create a New Staff Member**
- **Endpoint**: `/staff`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "position": "Manager",
    "department": "Sales",
    "email": "johndoe@example.com",
    "phone": "123-456-7890"
  }
  ```
- **Response**:
  - **201 Created**: Staff member added successfully.
  - **400 Bad Request**: Missing or invalid fields.

#### 2. **Get All Staff Members**
- **Endpoint**: `/staff`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "position": "Manager",
      "department": "Sales",
      "email": "johndoe@example.com",
      "phone": "123-456-7890"
    }
  ]
  ```

#### 3. **Get a Specific Staff Member**
- **Endpoint**: `/staff/<id>`
- **Method**: `GET`
- **Response**:
  - **200 OK**: Returns the staff member's data.
  - **404 Not Found**: Staff member not found.

#### 4. **Update a Staff Member**
- **Endpoint**: `/staff/<id>`
- **Method**: `PUT`
- **Request Body** (partial or full update):
  ```json
  {
    "position": "Senior Manager"
  }
  ```
- **Response**:
  - **200 OK**: Returns the updated staff member.
  - **404 Not Found**: Staff member not found.

#### 5. **Delete a Staff Member**
- **Endpoint**: `/staff/<id>`
- **Method**: `DELETE`
- **Response**:
  - **204 No Content**: Staff member deleted successfully.
  - **404 Not Found**: Staff member not found.

---

## Testing the Application

To verify that the application is functioning correctly, use the following commands:

### 1. **Create a New Staff Member**:
```powershell
curl -Method POST -Uri http://<EXTERNAL-IP>/staff -ContentType "application/json" -Body '{
    "id": 1,
    "name": "John Doe",
    "position": "Manager",
    "department": "Sales",
    "email": "johndoe@example.com",
    "phone": "123-456-7890"
}'
```

### 2. **Retrieve All Staff Members**:
```powershell
curl -Method GET -Uri http://<EXTERNAL-IP>/staff
```

### 3. **Retrieve a Specific Staff Member**:
```powershell
curl -Method GET -Uri http://<EXTERNAL-IP>/staff/1
```

### 4. **Update a Staff Member**:
```powershell
curl -Method PUT -Uri http://<EXTERNAL-IP>/staff/1 -ContentType "application/json" -Body '{
    "position": "Senior Manager"
}'
```

### 5. **Delete a Staff Member**:
```powershell
curl -Method DELETE -Uri http://<EXTERNAL-IP>/staff/1
```

Replace `<EXTERNAL-IP>` with the actual external IP address of your deployed service.

---

## Completed Tasks
1. **Developed Staff-Service Microservice**:
   - Built a Flask application to handle CRUD operations for staff management.
   - Used in-memory storage to keep the solution simple and lightweight.
   - Validated JSON payloads to ensure required fields are included.

2. **Containerized the Service**:
   - Created a `Dockerfile` to containerize the application.
   - Pushed the Docker image to Docker Hub.

3. **Deployed on Azure Kubernetes Service (AKS)**:
   - Wrote a Kubernetes deployment YAML file to deploy the microservice.
   - Exposed the service using a LoadBalancer.

4. **Set Up CI/CD Pipeline**:
   - Configured GitHub Actions to build, test, and deploy the microservice automatically.

---

## Testing the CI/CD Pipeline

To test the CI/CD pipeline, follow these steps:

1. **Trigger the Workflow**:
   Make a small change to the repository, such as updating the `README.md` file:
   ```bash
   echo "Triggering CI/CD Workflow Test" >> README.md
   git add README.md
   git commit -m "Testing CI/CD pipeline"
   git push
   ```

2. **Monitor Workflow Progress**:
   - Go to the GitHub repository and click on the **Actions** tab.
   - Select the `Build, Test, and Deploy` workflow.
   - Verify the progress of individual jobs:
     - **Build**: Checks out code, installs dependencies, runs unit tests, and builds a Docker image.
     - **Test**: Executes integration tests.
     - **Release**: Promotes the `test` Docker image to the `latest` tag.
     - **Deploy**: Deploys the application to the AKS cluster.

3. **Expected Outcome**:
   - All jobs (Build, Test, Release, Deploy) should complete successfully.
   - The application should be deployed to the Kubernetes cluster and accessible via the LoadBalancer's external IP.

4. **Verify Deployment**:
   - Check the deployment status:
     ```bash
     kubectl get pods
     kubectl get svc
     ```
   - Access the application using the external IP:
     ```bash
     curl http://<EXTERNAL-IP>
     ```

