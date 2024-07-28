def count_words(text):
    # Splits the input text into words using spaces as delimiters
    words = text.split()
    return len(words)

# Usage:
user_input = input("Enter a sentence or paragraph: ")
word_count = count_words(user_input)
print(f"Word count: {word_count}")