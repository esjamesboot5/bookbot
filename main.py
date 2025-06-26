from stats import count_words
from stats import char_count
from stats import new_list
from stats import list_sort
import sys


def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	bookprint = get_book_text(sys.argv[1])
	words = count_words(sys.argv[1])
	print("============ BOOKBOT ============")
	print("Analyzing book found at " + sys.argv[1] + "...")
	print("----------- Word Count ----------")
	print(f'Found {words} total words')
	print("--------- Character Count -------")
	fullDict = char_count(bookprint)
	ogList = new_list(fullDict)
	ogList.sort(reverse=True, key=list_sort)
	for item in ogList:
		if item["char"].isalpha():
			print(item["char"] + ": " + str(item["num"]))
main()
