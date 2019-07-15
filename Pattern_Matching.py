def isCompatible(text, pattern):
	if len(text) == 0 and pattern != '*' * len(pattern):
		return False
	if len(pattern) == 0:
		print('No pattern given! Terminating...')
		raise ValueError
	if len(pattern) == 1:
		if pattern[0] == '*' or pattern[0] == '?' and len(text) == 1 or len(text) == 1 and pattern[0] == text[0]:
			return True
		else:
			return False

	if pattern[0] in 'abcdefghijklmnopqrstuvwxyz':
		if pattern[0] == text[0]:
			return isCompatible(text[1:], pattern[1:])
		else:
			return False
	elif pattern[0] == '?':
		return isCompatible(text[1:], pattern[1:])
	elif pattern[0] == '*':
		for i in range(len(text)):
			if isCompatible(text[i:], pattern[1:]):
				return True
		return False

if __name__=='__main__':
	text = input('Please enter the text: ')
	pattern = input('Please enter the pattern: ')
	if isCompatible(text, pattern):
		print('YES')
	else:
		print('NO')