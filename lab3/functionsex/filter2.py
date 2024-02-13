words = ["apple", "banana,", "grape", "kiwi", "orange", "pineapple"]

def longword(words):
      return len(words) > 5
  
long_words = filter(longword, words)

long_words_list = list(long_words)

print(long_words_list)