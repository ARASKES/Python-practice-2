letter = input()
sentence = input()

words = []
word = ""
for char in sentence:
    if char == " ":
        words.append(word)
        word = ""
    else:
        word += char
words.append(word)

for w in words:
    if w.lower().__contains__(letter):
        print(w)
