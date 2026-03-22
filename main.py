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

		options = {
			'0' : ['quit', self.quit],
			'1' : ['keep only letters', self.keep_letters],
			'2' : ['keep only numbers', self.keep_numbers],
			'3' : ['keep only letters and numbers', self.keep_letters_and_numbers]
		}

		if use_clipboard:
			self.raw_string = clipboard.paste()

			print(f'Your string:\n\n{self.raw_string}\n')
		else:
			self.raw_string = str(input("Paste or type the string: ")).strip()

		print('Choose an action:\n')

		for key, value in options.items():
			print(f'{key} - {value[0]}')


		while loop:
			action = str(input('\n> '))

			if action in options.keys():
				self.final_string = options[action][1](self.raw_string)
				loop = False
			else:
				print(f"Wrong option! Try again. Valid options are [", end=' ')
				
				for key in options.keys():
					print(key, end=' ')

				print(']')

		if use_clipboard:
			print(f'Final string copied to clipboard: \n\n{self.final_string}')
			clipboard.copy(self.final_string)
		else:
			print(f'Final String:\n\n{self.final_string}')


	def quit(self, _):
		exit()


string_cleaner = StringCleaner()
string_cleaner.start()
