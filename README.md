# Servercheck Application

-------------------------

A CLI tool for testing a list of server's health

> [Linux Academy Lab](https://app.linuxacademy.com/hands-on-labs/f3c76029-5d76-4256-ba87-10085f6be310?redirect_uri=https:%2F%2Flinuxacademy.com%2Fcp%2Fmodules%2Fview%2Fid%2F383) 

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

## Results
The application will return a dictionary containing the results devided in successful and failed tries, as shown below:

```
{
    'success': [
        'IP1:PORT1',
        'IP1:PORT2'
    ],
    'failure': {
        'IP1:PORT3',
        'IP2:PORT1'
    }
}
```


