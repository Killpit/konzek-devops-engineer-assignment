# Task 4 Documentation

This documentation covers the troubleshooting aspect of Kubernetes deployment with respect to logs and how the process is handled from deployment to problem resolution.

### Container Creation

- Open Docker desktop or if you are using virtual machines, you can start Docker using terminal commands. However, because I am using Docker desktop for this task.
- Go to simple-python app directory with cd task4/simple-python-app
- To build the container, write docker build -t atatekeli/simple-python-app:v1 . (never forget to change the username)
- Push the image to Docker registry or DockerHub with atatekeli/simple-python-app:v1 (never forget to change the username)
- Start the minikube cluster with minikube start (there is an assumption that minikube is installed)
- Deploy the manifest file with kubectl apply -f deployment.yml
- Watch the changes in real time with kubectl get pods -w
Here, we get CrashLoopBackOff and the aim is to troubleshoot with logs
NAME                         READY   STATUS             RESTARTS     AGE
flask-app-86cf874c46-575wl   0/1     CrashLoopBackOff   1 (7s ago)   41s
flask-app-86cf874c46-575wl   1/1     Running            2 (24s ago)   58s
flask-app-86cf874c46-575wl   0/1     Error              2 (29s ago)   63s
flask-app-86cf874c46-575wl   0/1     CrashLoopBackOff   2 (17s ago)   75s
STATUS                       REASON          MESSAGE
Failure                      InternalError   an error on the server ("unable to decode an event from the watch stream: http2: client connection lost") has prevented the request from succeeding

So we start by verifying the contexts by kubectl config get-contexts
          default/api-crc-testing:6443/kubeadmin                      api-crc-testing:6443                                        kubeadmin/api-crc-testing:6443                              default
          docker-desktop                                              docker-desktop                                              docker-desktop                                              
          gke_gcp-zero-to-hero-demos_us-central1_three-tier-demo      gke_gcp-zero-to-hero-demos_us-central1_three-tier-demo      gke_gcp-zero-to-hero-demos_us-central1_three-tier-demo      
          iam-root-account@demo-cluster.eu-north-1.eksctl.io          demo-cluster.eu-north-1.eksctl.io                           iam-root-account@demo-cluster.eu-north-1.eksctl.io          
          iam-root-account@eks-monitoring.eu-north-1.eksctl.io        eks-monitoring.eu-north-1.eksctl.io                         iam-root-account@eks-monitoring.eu-north-1.eksctl.io        
*         minikube                                                    minikube                                                    minikube                                                    default
          three-tier-demo                                             three-tier-demo                                             clusterUser_ecommerce-demo_three-tier-demo                  
However, we couldn't get anything from this command and now we will try to look at the logs to solve the problem with kubectl logs <pod-name> (replace the pod name after getting the pods' name by kubectl get pods), and after reaching out the logs, we find that we have mistaken the name of the application with:
python3: can't open file '/app/app1.py': [Errno 2] No such file or directory
So, we will fix our Dockerfile first and then start the building and pushing containers all over again, but before that, we can delete the deployment with kubectl delete deployment flask-app after getting the name of the deployment with kubectl get deployments.

To do the container building and pushing again, you can follow the steps in container creation with just replacing v1 to v2

