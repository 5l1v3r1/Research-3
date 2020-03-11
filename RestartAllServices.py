from __future__ import print_function
import sys
import time
import ctypes
import subprocess
import datetime

try:
	import psutil
except ImportError:
	sys.exit("[-] Import error, psutil is not installed")

class service:
	def __init__(self):
		self.name = None
		self.result = None
		self.running_services = []
		self.stopped_services = []

	def enum(self):
		""" Enum installed services and return running and stopped
		to arrays """
		for service in psutil.win_service_iter():
			status = psutil.win_service_get(service.name())

			if "running" in status.status():
				self.running_services.append(status.name())
			else:
				self.stopped_services.append(status.name())

		return(self.running_services, self.stopped_services)

	def query(self, name):
		""" Returns service information as dict """
		try:
			info = psutil.win_service_get(name)
		except psutil.NoSuchProcess:
			return False
		else:
			return(info.as_dict())

	def start(self, name):
		""" Start a service using built-in sc executable """
		try:
			self.result = subprocess.check_output(["cmd.exe", "/c sc start {name}".format(name=name)])
		except subprocess.CalledProcessError:
			return False
		else:
			return True

	def stop(self, name):
		""" Stop a service using built-in sc executable """
		try:
			self.result = subprocess.check_output(["cmd.exe", "/c sc stop {name}".format(name=name)])
		except subprocess.CalledProcessError:
			return False
		else:
			return True

def main():
	""" Simple elevation check using WinAPI """
	if not bool(ctypes.windll.shell32.IsUserAnAdmin()):
		print("{time} - [-] Debug - We are not running elevated, cannot proceed".format(time=datetime.datetime.now()))
		return False

	""" Stop and restore service to previous state """
	running = service().enum()[0]
	print("-" * 110)
	print("Running services: {running}".format(running=len(running)))
	print("-" * 110)
	for name in running:
		query = service().query(name)
		if query["username"] == "LocalSystem":
			status = service().stop(name)
			if status:
				print("{time} - [+] Debug - Successfully stopped service ({name}) return code ({code})".format(time=datetime.datetime.now(),
						name=name, code=status))
			else:
				print("{time} - [-] Debug - Unable to stop service ({name}) return code ({code})".format(time=datetime.datetime.now(),
						name=name, code=status))

			time.sleep(5)

			status = service().start(name)	
			if status:
				print("{time} - [+] Debug - Successfully started service ({name}) return code ({code})".format(time=datetime.datetime.now(),
						name=name, code=status))
			else:
				print("{time} - [-] Debug - Unable to start service ({name}) return code ({code})".format(time=datetime.datetime.now(),
						name=name, code=status))

	""" Start and restore service to previous state """
	stopped = service().enum()[1]
	print("-" * 110)
	print("Stopped services: {stopped}".format(stopped=len(stopped)))
	print("-" * 110)
	for name in stopped:
		status = service().start(name)
		if status:
			print("{time} - [+] Debug - Successfully started service ({name}) return code ({code})".format(time=datetime.datetime.now(),
					name=name, code=status))
		else:
			print("{time} - [-] Debug - Unable to start service ({name}) return code ({code})".format(time=datetime.datetime.now(),
					name=name, code=status))

		time.sleep(5)

		status = service().stop(name)
		if status:
			print("{time} - [+] Debug - Successfully stopped service ({name}) return code ({code})".format(time=datetime.datetime.now(),
					name=name, code=status))
		else:
			print("{time} - [-] Debug - Unable to stop service ({name}) return code ({code})".format(time=datetime.datetime.now(),
					name=name, code=status))

if __name__ == "__main__":
	main()
