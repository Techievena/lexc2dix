import dicttoxml

def main():
	is_file_open = False
	file_name = r/''/
	try:
		my_file = open(file_name, mode = "a")
		is_file_open = True
	except FileNotFoundError:
		print("File not found!")
	except IOError:
		print("IOError!")
	except:
		print("Weird!!")

	sdef_module_generator()

def sdefs_module_generator():
	"""The module to generate <sdefs> section"""
	print("Sdefs module")

if __name__ == '__main__':
	main()
