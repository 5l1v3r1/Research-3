# Research

![xd](https://img.shields.io/badge/Python-3-blue.svg "Python 3")

Tools and scripts to use while hunting bugs and potential vulnerabilities

### FindAutoElevatedApplications.py
Scan the given directory for auto elevated applications. Pass parameter "runas" or "create" to use the results to create a process with the create or runas verb.

##### Usage:
```
python FindAutoElevatedApplications.py C:\Windows
python FindAutoElevatedApplications.py C:\Windows runas
python FindAutoElevatedApplications.py C:\Windows create
```

### RestartAllServices.py
Parses all the running and stopped services that use SYSTEM account. The running services will be restarted and the stopped services will be started and stopped.

##### Usage:
```
python RestartAllServices.py
```

### RunAs.py
Create a high integrity process using Windows API call ShellExecuteW, UAC will prompt if activated.

##### Usage:
```
python RunAs.py c:\windows\notepad.exe
```
