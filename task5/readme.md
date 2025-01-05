# Task 5 Documentation

In this task, Docker and talosctl has been used to demonstrate creating, managing, troubleshooting and potentially deploying a manual workload on Talos (a Linux kubernetes distribution).

To use Talos, you need to install Docker (assuming its installed) and talosctl command line. talosctl command line can be installed with:
- brew install siderolabs/tap/talosctl kubectl jq curl xz

To create the Talos cluster, you can simply write talosctl cluster create, which will remove much of the manual process if Docker is used directly.

After creating the cluster, you can get Talos API endpoint from talosctl config info:

## Current Context Details

| **Field**               | **Value**                 |
|--------------------------|---------------------------|
| Current context          | talos-default            |
| Nodes                    | not defined              |
| Endpoints                | 127.0.0.1:54077          |
| Roles                   | os:admin                 |
| Certificate expires      | 1 year from now (2026-01-05) |

Then, we can get cluster API endpoint with talosctl cluster show:

## Talos Cluster Details

### Cluster Overview

| **Field**              | **Value**                 |
|-------------------------|---------------------------|
| **PROVISIONER**         | docker                   |
| **NAME**                | talos-default            |
| **NETWORK NAME**        | talos-default            |
| **NETWORK CIDR**        | 10.5.0.0/24              |
| **NETWORK GATEWAY**     | (not defined)            |
| **NETWORK MTU**         | 1500                     |
| **KUBERNETES ENDPOINT** | https://127.0.0.1:54076  |

---

### Nodes

To get the nodes in a talos cluster, use kubectl get nodes

| **NAME**                       | **TYPE**       | **IP**       | **CPU** | **RAM**  | **DISK** |
|--------------------------------|----------------|--------------|---------|----------|----------|
| talos-default-controlplane-1   | controlplane   | 10.5.0.2     | 2.00    | 2.1 GB   | -        |
| talos-default-worker-1         | worker         | 10.5.0.3     | 2.00    | 2.1 GB   | -        |

To get the containers, run talosctl containers --nodes talos-default-controlplane-1,talos-default-worker-1 and in order to troubleshoot, we need to have container names beforehand

### Talos Cluster Containers and cluster management

| **NODE**                    | **NAMESPACE** | **ID**   | **IMAGE** | **PID** | **STATUS** |
|-----------------------------|---------------|----------|-----------|---------|------------|
| talos-default-worker-1       | system        | apid     | -         | 80      | RUNNING    |
| talos-default-controlplane-1 | system        | apid     | -         | 120     | RUNNING    |
| talos-default-controlplane-1 | system        | trustd   | -         | 121     | RUNNING    |

To get the services inside a specific cluster, run talosctl service --nodes <node-name>. This is an example for the worker node as talos doesn't mention all the services similar to kubectl.

| **NODE**                  | **SERVICE**     | **STATE** | **HEALTH** | **LAST CHANGE**    | **LAST EVENT**             |
|---------------------------|-----------------|-----------|------------|--------------------|---------------------------|
| talos-default-worker-1     | apid            | Running   | OK         | 2h25m50s ago       | Health check successful   |
| talos-default-worker-1     | containerd      | Running   | OK         | 2h25m42s ago       | Health check successful   |
| talos-default-worker-1     | cri             | Running   | OK         | 2h25m41s ago       | Health check successful   |
| talos-default-worker-1     | kubelet         | Running   | OK         | 2h25m42s ago       | Health check successful   |
| talos-default-worker-1     | machined        | Running   | OK         | 2h57m17s ago       | Health check successful   |

To create another cluster in talos, run talosctl cluster create --name <cluster-name> --cidr <cidr>

To destroy another cluster, run talosctl cluster destroy --name <cluster-name>

You can use --context flag to switch between clusters

- talosctl --context <cluster-name> version
- kubectl --context admin@<cluster-name> get nodes

To clean up the talos cluster, simply run talosctl cluster destroy


## Troubleshooting

Troubleshooting with a Talos cluster can be made with talosctl logs <node-name>. This will provide the logs to start troubleshooting process.

To stream the logs in real time, run talosctl logs <service> --nodes <node-name> --follow. 

Checking the dependencies of a particular node in talos can be done with talosctl inspect dependencies --nodes <node-name>