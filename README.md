# BPE Tokeniser

A Python implementation of Byte Pair Encoding (BPE), a subword tokenisation algorithm widely used in modern NLP models like GPT, BERT, and others.

## Overview

Byte Pair Encoding (BPE) is a data compression technique adapted for natural language processing. It works by iteratively merging the most frequent pairs of adjacent symbols (characters or subwords) in a corpus, building a vocabulary of subword units that can efficiently represent text while handling out-of-vocabulary words.

## Features

- ✅ **Character-level initialisation**: Builds vocabulary from unique characters in corpus
- ✅ **Multilingual support**: Handles English, Japanese, and other languages
- ✅ **Configurable merges**: Adjustable number of merge operations
- ✅ **End-of-word tokens**: Proper word boundary handling with `</w>` tokens
- ✅ **Frequency-based merging**: Selects most frequent character/subword pairs
- ✅ **Detailed logging**: Step-by-step merge process visualisation

## How It Works

1. **Vocabulary Initialisation**: Extract all unique characters from the corpus
2. **Pre-tokenisation**: Split text into words and add end-of-word tokens
3. **Iterative Merging**: 
   - Count frequencies of adjacent symbol pairs
   - Merge the most frequent pair into a new subword token
   - Update vocabulary and word representations
   - Repeat for specified number of iterations

## Usage

Simply run the main script:

```bash
python coding_tokeniser.py
```

**Note**: With 1000 merge iterations and detailed logging, execution takes several minutes. The script outputs progress for each merge iteration, showing the learning process in real-time.

The script includes a comprehensive corpus with 44 diverse documents and is configured for 1000 merge iterations. You can modify the corpus or adjust `num_merges` in the code:

```python
# Current configuration
num_merges = 1000 # 100 -> Basic starting point, 500 -> More sophisticated vocab, 1000 -> Rich subword representation
```

## Example Output

### Initial State
```
Initial vocabulary: [' ', '!', '(', ')', ',', '-', '.', ':', ';', '?', 'A', 'B', 'C', ...]
Vocabulary Size: 95
```

### During Training (1000 iterations)
```
Merge Iteration 1/1000
Top 5 Pair Frequencies: [(('e', 'r'), 42), (('i', 'n'), 38), (('t', 'h'), 35), ...]
Best Pair: ('e', 'r') with frequency 42
Merging ('e', 'r') into 'er'
```

### Final Results
```
Final Vocabulary Size: 1095
Learned Merges:
('e', 'r') -> 'er'
('i', 'n') -> 'in'
('t', 'h') -> 'th'
('a', 'nd') -> 'and'
('t', 'ion') -> 'tion'
...
```

## File Structure

```
bpe-tokeniser/
├── coding_tokeniser.py    # Complete BPE implementation
├── corpus.py              # Corpus data
├── LICENSE                # Project license
└── README.md             # This documentation
```

## Key Components

### Core Functions

- `get_pair_stats(splits)`: Counts frequencies of adjacent symbol pairs.
- `merge_pair(pair_to_merge, splits)`: Merges a specified pair in the word splits.
- `encode(text, merges)`: Encodes a new string into tokens using the learned merges.
- `decode(tokens)`: Decodes a list of tokens back into a string.
- Main training loop: Iteratively finds and merges the most frequent pairs.

### Data Structures

- `vocab`: List of all tokens (characters + learned subwords)
- `word_splits`: Dictionary mapping word tuples to frequencies
- `merges`: Dictionary storing learned merge rules
- `current_splits`: Working copy of word splits during training

## Configuration Options

The implementation includes several configurable parameters:

- **`num_merges`**: Set to 1000 for comprehensive subword learning (modifiable in code)
- **`end_of_word`**: Special token marking word boundaries (default: `</w>`)
- **Corpus**: 44 diverse documents embedded in `coding_tokeniser.py` covering:
  - Technical/Scientific content
  - Literature and creative writing  
  - News and journalism
  - Technology and programming
  - Multilingual text (English, Spanish, French, Japanese, Chinese)
  - Business, history, education, philosophy, and more

## Technical Notes

- **Corpus Statistics**: 44 documents, ~45,000 characters, ~7,500 words
- **Multilingual Support**: Handles English, Spanish, French, Japanese, and Chinese text
- Uses tuples for immutable word representations
- Maintains frequency counts for efficient pair selection  
- Sorts vocabulary for consistent output
- Memory-efficient implementation suitable for educational purposes
- Detailed iteration logging shows BPE learning progression

## Applications

This BPE implementation demonstrates the core algorithm used in:
- **GPT models**: Subword tokenisation for language generation
- **Machine Translation**: Handling rare and compound words
- **Text Compression**: Original BPE application
- **Multilingual NLP**: Cross-lingual vocabulary sharing

## Encoding and Decoding

The script now includes `encode()` and `decode()` functions to apply the learned BPE model to new text.

### `encode(text, merges)`
- **Input**: A string of text and the learned `merges` dictionary.
- **Output**: A list of BPE tokens.

### `decode(tokens)`
- **Input**: A list of BPE tokens.
- **Output**: The reconstructed string.

Example usage is included at the end of `coding_tokeniser.py`:
```python
# -- Example of Encoding and Decoding --
print("
-- Encoding/Decoding Example --")
sample_text = "This is a test of the BPE tokeniser."
print(f"Original Text: {sample_text}")

encoded_output = encode(sample_text, merges)
print(f"Encoded Output: {encoded_output}")

decoded_output = decode(encoded_output)
print(f"Decoded Output: {decoded_output}")
```

## Future Enhancements

- [x] Encode/decode functions for applying learned BPE to new text
- [ ] Save/load trained models
- [ ] Performance optimisations for larger corpora
- [ ] Regex-based pre-tokenisation improvements
- [ ] Comparison with other tokenisation methods


---

*This implementation is designed for educational purposes to understand BPE mechanics. For production use, consider optimised libraries like Hugging Face Tokenisers or SentencePiece.*