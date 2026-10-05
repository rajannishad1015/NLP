import string

def calculate(given_text):
    text = given_text.lower().translate(
        str.maketrans('', '', string.punctuation)
    )
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

text = input("Enter a few sentences with repeated words: ")
wfreq = calculate(text)
print("\nWord Frequency:\n")
for word, frequency in wfreq.items():
    print(word, ":", frequency)
