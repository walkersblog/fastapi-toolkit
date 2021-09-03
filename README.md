# fastapi-toolkit
Simple application with tools from metrics and logging.

## Getting Started

On a Red Hat Enterpirse Linux 8 client, view the availble Python module streams:

```
sudo dnf module list | grep -i python
```

Install your prefered Python version:

```
sudo dnf module install python39 -y
```

Clone this repo:

```
git clone https://github.com/walkersblog/fastapi-toolkit.git
cd fastapi-toolkit
```

Install a Python virtual environment:

```
python3.9 -m venv venv
```

Activate it:

```
source venv/bin/activate
```

Upgrade `pip` and install the project requirements:

```
pip install --upgrade pip
pip install -r requirements.txt
```

Run the application:

```
python main.py
```

## Podman

Install Podman and friends:

```
sudo dnf install podman buildah skopeo -y
```

Build a container image, from root of the project directory:

```
buildah bud -t walkersblog.net/fast-api-toolkit .
```

Create a pod for the app:

```
podman pod create -p 8000:8000 -n app-pod
```

Run the container:

```
podman run --name app-container --pod app-pod -d walkersblog.net/fast-api-toolkit:latest
```

## OpenShift

Get client tools:

```
wget https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/openshift-client-linux.tar.gz
sudo tar -xvf openshift-client-linux.tar.gz -C /usr/local/bin
oc version
```

Log into the OpenShift:

```
oc login -u richard -p <PASS> https://api.cluster.lab.home:6443
```

The log in to the OpenShift registry with Podman:

```
podman login -u richard -p $(oc whoami -t) --tls-verify=false default-route-openshift-image-registry.apps.cluster.lab.home:443
```

Create new project:

```
oc new-project fastapi
```

Create new image stream:

```
oc create is toolkit
```

Tag your local image with the OpenSHift <REGISTRY>/<PROJECT>/<IMAGE_STREAM>:<VERSION>

```
podman tag walkersblog.net/fast-api-toolkit:latest default-route-openshift-image-registry.apps.cluster.lab.home/fastapi/fast-api-toolkit:latest
```

Push the image:

```
podman push --tls-verify=false default-route-openshift-image-registry.apps.cluster.lab.home/fastapi/fast-api-toolkit:latest
```




