import ctypes
import sys

try:
	path_input = sys.argv[1]
except IndexError:
	print("Unable to start process due to path is incorrect or none")
	sys.exit()

result = ctypes.windll.shell32.ShellExecuteW(None, "runas", path_input, None, None, 1)
if result >= 42:
	print("Successfully started process {path_input}".format(path_input=path_input))
else:
	print("Unable to start process {path_input}".format(path_input=path_input))
