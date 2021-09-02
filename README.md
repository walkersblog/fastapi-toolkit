# fastapi-toolkit
Simple application with tools from metrics and logging.

## Getting Started

On a Red Hat Enterpirse Linux 8 clinet, view the availble Python module streams:

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
