import os
import sys
import ctypes

class scanner:
	""" Class to scan and parse manifests inside a binary file """
	def __init__(self):
		self.result = []
		self.strings = ['level="requireAdministrator"', '<autoElevate>true</autoElevate>']

	def search(self, path):
		for root, dirs, files in os.walk(os.path.join(path)):
			for name in files:
				if os.path.join(root, name).endswith(".exe"):
					try:
						with open(os.path.join(root, name) , "rb") as file:
							data = str(file.read())
					except IOError:
						pass
					else:
						if self.strings[0] and self.strings[1] in data:
							self.result.append(os.path.join(root, name))
				else:
					pass

		return self.result

class process:
	""" Class to create processes """
	def create(self, path):
		result = ctypes.windll.shell32.ShellExecuteW(None, "open", path, None, None, 1)
		if result >= 42:
			return True
		else:
			return False

	def runas(self, path):
		result = ctypes.windll.shell32.ShellExecuteW(None, "runas", path, None, None, 1)
		if result >= 42:
			return True
		else:
			return False

if __name__ == "__main__":
	try:
		result = scanner().search(str(sys.argv[1]))
	except Exception as error:
		print("Unable to search for auto elevated applications due to path is incorrect or none")
	else:
		try:
			if sys.argv[2] == "runas":
				for path in result:
					if process().runas(path):
						print("Done - Runas - {path}".format(path=path))
			elif sys.argv[2] == "create":
				for path in result:
					if process().create(path):
						print("Done - Create - {path}".format(path=path))
		except IndexError:
			for path in result:
				print(path)
