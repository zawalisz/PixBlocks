word = str(input("Write the word: "))

def is_palindrome(word):
    word_reversed = ''
    for i in word.lower():
        word_reversed = i + word_reversed

    if word.lower() == word_reversed:
        return('The word "' + word + '" is a palindrome')
    else:
        return('The word "' + word + '" is not a palindrome')

print(is_palindrome(word))