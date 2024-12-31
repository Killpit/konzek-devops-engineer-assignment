# Task 3 Documentation

### Deploying manifest files

- Go to cd manifests from task3 file
- For deployment file, write kubectl apply -f deployment.yaml
- For service file, write kubectl apply -f service.yaml
- For ingress, write kubectl apply -f ingress.yaml
- For ClusterIssuer, write kubectl apply -f clusterIssuer.yaml
- For cert-manager, write kubectl apply -f certManager.yaml

Before deploying ingress.yaml, it's highly recommended to deploy ClusterIssuer and certManager beforehand 

#### Checking the manifest files

- Use kubectl get pods to check whether the pods are working with the status
- For services, use kubectl get services to check whether the services are working
- Use kubectl get deployments to check deployments
- Use kubectl get ingress to check whether the ingress status
- 