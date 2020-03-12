# Research

![xd](https://img.shields.io/badge/Python-3-blue.svg "Python 3")

Tools and scripts to use while hunting bugs and potential vulnerabilities

#### FindAutoElevatedApplications.py
Search for auto elevated applications by providing path to directory. Create processes using the results from the search, either create or runas verb can be invoked.

#### RestartAllServices.py
Parses all the running and stopped services that use SYSTEM account. The running services will be restarted and the stopped services will be started and stopped.

#### RunAs.py
Create a high integrity process using Windows API call ShellExecuteW, UAC will prompt if activated.
