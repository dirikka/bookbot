import re
import sys
from stats import get_num_words
from stats import get_num_chars

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	f.close()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print(f"Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		num_words =get_num_words(get_book_text(sys.argv[1]))
		num_chars =get_num_chars(get_book_text(sys.argv[1]))
		txt = f"""============ BOOKBOT =============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
"""
		print(txt)
		txt2=f"============= END ==============="
		for k, v in num_chars:
			print(f"{k}: {v}")
		print(txt2)

main()
