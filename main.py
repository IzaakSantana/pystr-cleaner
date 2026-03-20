use_clipboard = False

try:
	import clipboard

	use_clipboard = True
except ModuleNotFoundError:
	print("Clipboard module not installed!")


raw_string = ''
final_string = ''
mode = ''
loop = True


def keep_letters(string):
	result = ''

	for char in string:
		if char.isalpha() or char.isspace():
			result += char

	return result


def keep_numbers(string):
	result = ''

	for char in string:
		if char.isnumeric():
			result += char

	return result


def keep_letters_and_numbers(string):
	result = ''

	for char in string:
		if char.isalnum() or char.isspace():
			result += char

	return result


def quit(_):
	exit()

options = {
	'0' : ['quit', quit],
	'1' : ['keep only letters', keep_letters],
	'2' : ['keep only numbers', keep_numbers],
	'3' : ['keep only letters and numbers', keep_letters_and_numbers]
}


if use_clipboard:
	raw_string = clipboard.paste()

	print(f'Your string:\n\n{raw_string}\n')
else:
	raw_string = str(input("Paste or type the string: ")).strip()

print('Choose an action:\n')

for key, value in options.items():
	print(f'{key} - {value[0]}')


while loop:
	mode = str(input('\n> '))

	if mode in options.keys():
		final_string = options[mode][1](raw_string)
		loop = False
	else:
		print(f"Wrong option! Try again. Valid options are [", end=' ')
		
		for key in options.keys():
			print(key, end=' ')

		print(']')

if use_clipboard:
	print(f'Final string copied to clipboard: \n\n{final_string}')
	clipboard.copy(final_string)
else:
	print(f'Final String:\n\n{final_string}')
