#Write a function that takes an array of words and smashes them together intro a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

words = ["this","is","a","really","long","sentence"]

def smash(words):
    smash_words = " ".join(words)
    return smash_words

print(smash(words))