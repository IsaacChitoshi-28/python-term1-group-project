sentence = input("Enter a sentence: ")

# Split the sentence into a list of words
words = sentence.split()

# 1. Count the words
word_count = len(words)

# 2. Count characters (no spaces)
char_count = 0
for word in words:
    char_count = char_count + len(word)

# 3. Find the longest word
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Number of words:", word_count)
print("Number of characters:", char_count)
print("Longest word:", longest_word)
