def count_words(filepath):
        with open(filepath) as f:
                file_contents = f.read()
                word_list = file_contents.split()
                word_count = len(word_list)
                return word_count


def char_count(filetext):
	charDict = {}
	for contents in filetext:
		contents = contents.lower()
		if contents not in charDict:
			charDict[contents] = 1
		else:
			charDict[contents] += 1
	return charDict

def new_list(charDict):
	dictList = []
	for key, value in charDict.items():
		temp = {'char': key, 'num': value}
		dictList.append(temp)
	return dictList

def list_sort(dictList):
	return dictList["num"]
	

