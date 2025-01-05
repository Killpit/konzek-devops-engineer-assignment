# Task 3 Documentation

### Setting up minikube cluster

This section assumes Minikube is installed. We use minikube due to local deployment and testing and it should not be used in production environments.

**To start minikube**:

- ```minikube start```
- And then use ```minikube addons enable ingress``` to allow ingress in this cluster

### Deploying resources by applying manifests

Apply manifests with:

- First, access the directory with ```cd K8S```
- ```kubectl apply -f deployment.yaml```
- ```kubectl apply -f service.yaml```
- ```kubectl apply -f ingress.yaml```
- Alternatively, you can run all the manifest files with ```kubectl apply -f .``` to avoid writing multiple command line prompts and keep things simpler

### Verify resources

Checking pods with:

- ```kubectl get pods``` (use -w to check them in real time)

Verify service and ingress with:

Service: ```kubectl get service```
Ingress: ```kubectl get ingress```

### Access the application

Update the application image with:

- ```kubectl set image deployment/http-server-deployment http-server=atatekeli/simple-python-app:v2``` (for updating the image)
- ```kubectl rollout status deployment/http-server-deployment``` (for monitoring rollout status)