import ctypes
import sys

try:
	path_input = sys.argv[1]
except IndexError:
	print("Unable to start process due to path is incorrect or none")
	sys.exit()

class disable_fsr():
	"""
	A class to disable file system redirection
	"""
	disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
	revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection

	def __enter__(self):
		self.old_value = ctypes.c_long()
		self.success = self.disable(ctypes.byref(self.old_value))

	def __exit__(self, type, value, traceback):
		if self.success:
			self.revert(self.old_value)

with disable_fsr():
	result = ctypes.windll.shell32.ShellExecuteW(None, "runas", path_input, None, None, 1)
	if result >= 42:
		print("Successfully started process {path_input}".format(path_input=path_input))
	else:
		print("Unable to start process {path_input}".format(path_input=path_input))
