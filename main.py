try:
	import clipboard

	use_clipboard = True
except ModuleNotFoundError:
	use_clipboard = False
	print("Clipboard module not installed!")


class StringCleaner:
	def __init__(self):
		self.raw_string = ''
		self.final_string = ''

		self.options = {
			'0' : ['quit', self.quit],
			'1' : ['keep only letters', self.keep_letters],
			'2' : ['keep only numbers', self.keep_numbers],
			'3' : ['keep only letters and numbers', self.keep_letters_and_numbers]
		}

	def print_options(self):
		for key, value in self.options.items():
			print(f'{key} - {value[0]}')


	def keep_letters(self, string):
		result = ''

		for char in string:
			if char.isalpha() or char.isspace():
				result += char

		return result


	def keep_numbers(self, string):
		result = ''

		for char in string:
			if char.isnumeric():
				result += char

		return result


	def keep_letters_and_numbers(self, string):
		result = ''

		for char in string:
			if char.isalnum() or char.isspace():
				result += char

		return result

	
	def start(self):
		loop = True



		if use_clipboard:
			self.raw_string = clipboard.paste()

			print(f'Your string:\n\n{self.raw_string}\n')
		else:
			self.raw_string = str(input("Paste or type the string: ")).strip()

		print('Choose an action:\n')

		self.print_options()


		while loop:
			action = str(input('\n> '))

			if action in self.options.keys():
				self.final_string = self.options[action][1](self.raw_string)
				loop = False
			else:
				print(f"Wrong option! Try again. Valid options are:\n")
				self.print_options()

		if use_clipboard:
			print(f'Final string copied to clipboard: \n\n{self.final_string}')
			clipboard.copy(self.final_string)
		else:
			print(f'Final String:\n\n{self.final_string}')


	def quit(self, _):
		exit()


string_cleaner = StringCleaner()
string_cleaner.start()
