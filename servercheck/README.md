# Servercheck Application

-------------------------

A CLI tool for testing a list of server's health 


## Installation

Install using `pip`:
```
pip install servercheck
```

## Usage

### 1. Read input from a configuration file
```
$ servercheck -f servers.json
Successful Connections
----------------------
IP1:port
IP2:port

Failed Connections
------------------
IP3:port
```

In this case the servers.json file is like:
```
[
    "IP1:port",
    "IP1:port2",
    "IP2:port"
]
```

### 2. Pass host/port combination
```
$ servercheck -s IP1:port -s IP2:port -s IP3:port
Successful Connections
----------------------
IP1:port
IP2:port

Failed Connections
------------------
IP3:port
```


