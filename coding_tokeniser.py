import sys
import codecs

# Set stdout to utf-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

from corpus import corpus

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

import collections

def get_pair_stats(splits):
    """Counts the frequency of adjacet pairs in the word splits."""
    pair_counts = collections.defaultdict(int) #initialise a default dictionary with default values of int 0, to count pairs
    for word_tuple, freq in splits.items():
        symbols = list(word_tuple)
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i+1])
            pair_counts[pair] += freq # Add the frequency of the word to the pair count
    return pair_counts

# Helper function, Merge Pair
def merge_pair(pair_to_merge, splits):
    """Merges the specified word pair in the splits."""
    new_splits = {}
    (first, second) = pair_to_merge
    merged_token = first + second
    for word_tuple, freq in splits.items():
        symbols = list(word_tuple)
        new_symbols = []
        i = 0
        while i < len(symbols):
            # If the current symbol and next symbol match the pair to merge
            if i < len(symbols) - 1 and symbols[i] == first and symbols[i + 1] == second:
                new_symbols.append(merged_token)
                i += 2 # Skip the next symbol
            else:
                new_symbols.append(symbols[i])
                i += 1
        new_splits[tuple(new_symbols)] = freq # Use the updated symbols list as the key
    return new_splits

# Iterative BPE Merging Loop
# -- BPE Trainng Loop Initialisation --
num_merges = 1000 # 100 -> Basic starting point, 500 -> More sophisticated vocab, 1000 -> Rich subword representation
merges = {}
current_splits = word_splits.copy() # Start with the intial word splits

print("\n-- Starting BPE Merging Loop --")
print(f"Initial splits: {current_splits}")
print("-" * 30)

for i in range(num_merges):
    print(f"\nMerge Iteration {i+1}/{num_merges}")

    # 1. Calculate Pair Frequencies
    pair_stats = get_pair_stats(current_splits)
    if not pair_stats:
        print("No more pairs to merge.")
        break
    # Print top pairs for debugging
    top_pairs = sorted(pair_stats.items(), key=lambda item: item[1], reverse=True)
    print(f"Top 5 Pair Frequencies: {top_pairs[:5]}")

    # 2. Find the Most Frequent/Best Pair
    best_pair = max(pair_stats, key=pair_stats.get)
    best_freq = pair_stats[best_pair]
    print(f"Best Pair: {best_pair} with frequency {best_freq}")

    # 3. Merge the Best Pair
    current_splits = merge_pair(best_pair, current_splits)
    new_token = best_pair[0] + best_pair[1]
    print(f"Merging {best_pair} into '{new_token}'")
    print(f"Splits after merge: {current_splits}")

    # 4. Update Vocabulary
    vocab.append(new_token)
    print(f"Updated Vocabulary: {vocab}")

    # 5. Store Merge Rule
    merges[best_pair] = new_token
    print(f"Updated Merges: {merges}")

    print("-" * 30)

# Review Final Results
# -- BPE Merges Complete --
print("\n-- BPE Merges Complete --")
print(f"Final Vocabulary Size: {len(vocab)}")
print("\nLearned Merges (Pair -> New Token):")
for pair, token in merges.items():
    print(f"{pair} -> '{token}'")

print("\nFinal Word Splits after all merges:")
print(current_splits)

print("\nFinal Vocabulary (sorted)")
# Sort for consistent viewing
final_vocab_sorted = sorted(list(set(vocab))) # Use set to remove potential duplicates if any step introduced them
print(final_vocab_sorted)


def encode(text, merges):
    """Encodes a string into a list of tokens using the learned merges."""
    words = text.split(' ')
    all_tokens = []
    
    # Create a ranked list of merges
    merge_ranks = {pair: i for i, pair in enumerate(merges.keys())}

    for word in words:
        if not word:
            continue
        
        tokens = list(word) + [end_of_word]
        
        while True:
            # Find the pair with the lowest rank in the current tokens
            best_pair = None
            min_rank = float('inf')
            
            for i in range(len(tokens) - 1):
                pair = (tokens[i], tokens[i+1])
                if pair in merge_ranks and merge_ranks[pair] < min_rank:
                    min_rank = merge_ranks[pair]
                    best_pair = pair

            if best_pair is None:
                break

            # Merge the best pair
            first, second = best_pair
            new_tokens = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] == first and tokens[i+1] == second:
                    new_tokens.append(first + second)
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            tokens = new_tokens
            
        all_tokens.extend(tokens)
        
    return all_tokens

def decode(tokens):
    """Decodes a list of tokens back into a string."""
    text = "".join(tokens)
    text = text.replace(end_of_word, ' ')
    return text.strip()

# -- Example of Encoding and Decoding --
print("\n-- Encoding/Decoding Example --")
sample_text = "This is a test of the BPE tokeniser."
print(f"Original Text: {sample_text}")

encoded_output = encode(sample_text, merges)
print(f"Encoded Output: {encoded_output}")

decoded_output = decode(encoded_output)
print(f"Decoded Output: {decoded_output}")

another_sample = "deep learning"
print(f"\nOriginal Text: {another_sample}")
encoded_output = encode(another_sample, merges)
print(f"Encoded Output: {encoded_output}")
decoded_output = decode(encoded_output)
print(f"Decoded Output: {decoded_output}")