import os
class file:
	def __init__(self, var, filepath):
		self.var = var
		self.filepath = filepath
		print(f"DEBUG: var - {var} / filepath - {filepath}")
	def write(contents, filepath):
		with open(contents, "w") as f:
			f.write(contents)
	def read(filepath):
		with open(filepath) as f:
			return f.read()
user = file("Local", ".local/50383.str")
command_filepath = file(None, ".local/10320.list")
commands_list = file.read(command_filepath.filepath)
infofile = file(None, ".local/10000.info")
information = file.read(infofile.filepath)

class OPERATIONS():
	def calc():
		global user
		operations = "1. Addition\n2. Subtraction\n3. Mulipalcation\n4. Division"
		print(operations)
		command = input(f"(Operations.calc) {user.var} > ")
		if command == "1":
			num1 = input(f"(Operations.calc) Insert Num1 {user.var} > ")
			num2 = input(f"(Operations.calc) Insert Num2 {user.var} > ")
			try:
				int(num1)
			except ValueError:
				print("ERROR: Num1 Invailed")
			try:
				int(num2)
			except ValueError:
				print("ERROR: Num2 Invailed")
			print(int(num1) + int(num2))
		elif command == "2":
			num1 = input(f"(Operations.calc) Insert Num1 {user.var} > ")
			num2 = input(f"(Operations.calc) Insert Num2 {user.var} > ")
			try:
				int(num1)
			except ValueError:
				print("ERROR: Num1 Invailed")
			try:
				int(num2)
			except ValueError:
				print("ERROR: Num2 Invailed")
			print(int(num1) - int(num2))
		elif command == "3":
			num1 = input(f"(Operations.calc) Insert Num1 {user.var} > ")
			num2 = input(f"(Operations.calc) Insert Num2 {user.var} > ")
			try:
				int(num1)
			except ValueError:
				print("ERROR: Num1 Invailed")
			try:
				int(num2)
			except ValueError:
				print("ERROR: Num2 Invailed")
			print(int(num1) * int(num2))
		elif command == "4":
			num1 = input(f"(Operations.calc) Insert Num1 {user.var} > ")
			num2 = input(f"(Operations.calc) Insert Num2 {user.var} > ")
			try:
				int(num1)
			except ValueError:
				print("ERROR: Num1 Invailed")
			try:
				int(num2)
			except ValueError:
				print("ERROR: Num2 Invailed")
			try:
				print(int(num1) / int(num2))
			except ZeroDivisionError:
				print("ERROR: ZeroDivisionError")
		else:
			print("ERROR: Command Invailed")

	class FileManager:
		def create():
			print("Insert a file name or path")
			command = input(f"(Operations.FileManager.create) {user.var} > ")
			f = open(command, "x")
		def delete():
			print("Insert a file name or path")
			command = input(f"(Operations.FileManager.delete) {user.var} > ")
			if command == ".local":
				print("ERROR: Required program folder")
			if os.path.exists(command):
				os.remove(command)
			else:
				print("ERROR: File or filepath doesn't exist")

while True:
	command = input(f"{user.var} > ")
	if command == "help":
		print()
		print(commands_list)
	elif command == "quit":
		quit()
	elif command == "INFORMATION":
		print(information)
	elif command == "calc":
		OPERATIONS.calc()
	elif command == "file":
		print("1. Create\n2. Delete")
		command = input(f"(Operations.FileManager) {user.var} > ")
		if command == "1":
			OPERATIONS.FileManager.create()
		elif command == "2":
			OPERATIONS.FileManager.delete()
		else:
			print("ERROR: Invailed Command")
	elif command == "dir":
		os.system("dir")
	else:
		print("ERROR: Invailed Command\nHint - Type help")
