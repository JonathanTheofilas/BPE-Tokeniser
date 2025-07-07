# Sample data
corpus = [
    "Byte Pair Encoding (BPE) is a subword tokenisation algorithm that iteratively merges the most frequent pair of consecutive bytes or characters. Originally used for text compression, it's now widely used in NLP for tokenisation in models like GPT.",
    "The quick brown fox jumps over the lazy dog. This sentence contains all letters in the English alphabet, making it perfect for testing tokenisation algorithms and text processing systems.",
    "気の向くままに好きな音楽を聞きながら、コーヒーを飲んで過ごす週末が最高だ。日本語の文章もBPEでトークナイズできるだろうか。",
]

print("\nSample corpus:")
for doc in corpus:
    print(doc)

# Initisalise Vocabulary and Pre-Tokenise

# Initialise the vocabulary with all unique characters in the corpus
unique_chars = set()
for doc in corpus:
    for char in doc:
        unique_chars.add(char)

vocab = list(unique_chars)
vocab.sort() # Sort to maintain a consistent order, making the vocabulary list predictable

# Add a special token for the end of a word, end-of-word token
end_of_word = "</w>"
vocab.append(end_of_word)

print("\nInitial vocabulary:")
print(vocab)
print(f"Vocabulary Size: {len(vocab)}")

# Pre-tokenize the corpus: Split into words and then characters
# Split by space for simplicity and add the end-of-word token
word_splits = {}
for doc in corpus:
    words = doc.split(' ')
    for word in words:
        if word:
            char_list = list(word) + [end_of_word]
            # Convert the list of characters to a tuple for immutability
            word_tuple = tuple(char_list)
            if word_tuple not in word_splits:
                word_splits[word_tuple] = 0
            word_splits[word_tuple] += 1 # Count occurrences of each initial word split

print("\nPre-tokenised Word Frequencies:")
print(word_splits)

