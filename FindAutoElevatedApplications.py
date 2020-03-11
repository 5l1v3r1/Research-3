import os
import sys

def manifests(payload):
	strings = ["<autoElevate>true</autoElevate>",
				"<autoElevate xmlns=\"http://schemas.microsoft.com/SMI/2005/WindowsSettings\">true</autoElevate>"]
	
	try:
		manifest = open(os.path.join(payload), "rb").read()
	except Exception as error:
		return False

	for string in strings:
		if (str(string) in str(manifest)):
			return True
		else:
			return False

def main():
	results = []
	parsed = []

	try:
		path_input = sys.argv[1]
	except IndexError:
		print("Unable to search for auto elevated applications due to path is incorrect or none")
		sys.exit()

	for dir, sub, file_list in os.walk(os.path.join(path_input)):
		for file in file_list:
			if file.endswith(".exe"):
				if (os.path.isfile(os.path.join(dir,file)) == True):
					results.append(os.path.join(dir,file))
				else:
					pass
			else:
				pass

	for exe in results:
		if (manifests(exe) == True):
			parsed.append(exe)
		else:
			pass

	print("\nResults:")
	for path in parsed:
		print("\t* {path}".format(path=path))

if __name__ == "__main__":
	main()
