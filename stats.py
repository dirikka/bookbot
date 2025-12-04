from collections import Counter

def get_num_words(toread):

        return len(toread.split())

def get_num_chars(toread):
	char_count = Counter(toread.lower())
	char =  [(l,k) for k,l in sorted([(j,i) for i,j in char_count.items() if i.isalpha()],reverse=True)]
	char_list = list(char)
	return char_list


