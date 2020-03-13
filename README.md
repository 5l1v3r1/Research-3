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
Parses all the running and stopped services that use SYSTEM account. The running services will be restarted and the stopped services will be started and stopped. This utility will assist you while using Process Monitors to monitor activity and behavior of a large scale of services, when a new Windows version has been released.

##### Usage:
```
python RestartAllServices.py
```

### RunAs.py
Create a high integrity process using Windows API call ShellExecuteW, UAC will prompt if set to highest level or if the target process can't auto elevate.

##### Usage:
```
python RunAs.py c:\windows\notepad.exe
```

### HijackClass.py
Hijack a HKCU registry class by providing class type and path to payload. 

##### Usage:
```
python HijackClass.py -c -t TestClass -v C:\\Windows\\notepad.exe -d True
python HijackClass.py -r -t TestClass
```
