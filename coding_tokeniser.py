# Sample data
corpus = [
    # Technical/Scientific
    "Machine learning algorithms require large datasets to train effectively. Deep neural networks with millions of parameters can learn complex patterns from data through backpropagation and gradient descent optimization.",
    "Quantum computing leverages quantum mechanical phenomena like superposition and entanglement to process information exponentially faster than classical computers for specific computational problems.",
    "CRISPR-Cas9 gene editing technology allows scientists to precisely modify DNA sequences, opening new possibilities for treating genetic diseases and advancing biotechnology research.",
    "Blockchain technology creates decentralized, immutable ledgers through cryptographic hashing and consensus mechanisms, enabling trustless transactions without intermediaries.",
    
    # Literature/Creative
    "The ancient oak tree stood majestically in the moonlit garden, its gnarled branches reaching toward the star-studded sky like weathered fingers grasping for forgotten dreams.",
    "She walked through the bustling marketplace, surrounded by the cacophony of vendors shouting, children laughing, and the rhythmic clanging of metalworkers crafting their wares.",
    "In the depths of the enchanted forest, mystical creatures danced around flickering campfires, their ethereal songs echoing through the misty valleys and shadowed groves.",
    "The detective examined the crime scene meticulously, searching for clues that might unravel the mysterious circumstances surrounding the peculiar disappearance.",
    
    # News/Journalism
    "Global climate summit delegates reached a groundbreaking agreement on carbon emissions reduction targets, with participating nations committing to ambitious renewable energy transition timelines.",
    "Economic indicators suggest continued inflation pressures despite central bank interventions, with consumer spending patterns showing resilience across multiple sectors.",
    "International space collaboration initiatives announced plans for sustainable lunar exploration missions, incorporating advanced propulsion systems and habitat construction technologies.",
    "Healthcare researchers published breakthrough findings on personalized medicine approaches, demonstrating improved patient outcomes through genetic biomarker analysis.",
    
    # Technology/Programming
    "Modern software development practices emphasize continuous integration, automated testing, and microservices architectures to improve scalability and maintainability.",
    "Cloud computing platforms provide on-demand resource allocation through virtualization technologies, enabling organizations to scale infrastructure dynamically based on computational requirements.",
    "Artificial intelligence applications in autonomous vehicles utilize computer vision, sensor fusion, and real-time decision-making algorithms for safe navigation in complex environments.",
    "Cybersecurity frameworks implement multi-layered defense strategies including encryption, authentication protocols, and intrusion detection systems to protect sensitive information.",
    
    # Conversational/Social
    "Hey there! How's your day going? I was thinking we could grab coffee later and catch up on everything that's been happening lately.",
    "Can you believe how quickly technology changes these days? It feels like every week there's some new gadget or app that everyone's talking about.",
    "I absolutely love traveling to different countries and experiencing diverse cultures, trying local cuisines, and meeting fascinating people from all walks of life.",
    "Working from home has definitely changed my daily routine, but I've learned to appreciate the flexibility and the extra time I save from not commuting.",
    
    # Science/Research
    "Neuroscientists discovered that meditation practices can significantly alter brain structure and function, particularly in regions associated with attention, emotional regulation, and memory formation.",
    "Archaeological excavations revealed evidence of sophisticated ancient civilizations with advanced mathematical knowledge, architectural engineering capabilities, and complex social organizational systems.",
    "Environmental biologists documented alarming biodiversity loss rates across multiple ecosystems, emphasizing the urgent need for comprehensive conservation strategies and habitat protection measures.",
    "Astrophysicists detected gravitational waves from distant galactic events, confirming Einstein's theoretical predictions and opening new observational windows into cosmic phenomena.",
    
    # Business/Economics
    "Startup entrepreneurs navigate competitive markets by developing innovative products, securing venture capital funding, and building sustainable business models for long-term growth.",
    "Supply chain optimization requires sophisticated logistics coordination, inventory management systems, and strategic partnerships to ensure efficient product distribution networks.",
    "Digital transformation initiatives help traditional companies modernize operations through cloud migration, data analytics implementation, and customer experience enhancement strategies.",
    "Investment portfolio diversification across asset classes, geographic regions, and market sectors helps minimize risk while maximizing potential returns for institutional investors.",
    
    # History/Culture
    "Ancient civilizations developed remarkable achievements in mathematics, astronomy, agriculture, and architectural engineering that continue to influence modern society and scientific understanding.",
    "Cultural traditions passed down through generations preserve important historical knowledge, artistic expressions, and community values that shape contemporary social identities.",
    "Renaissance period innovations in art, science, and philosophy fundamentally transformed European intellectual development and established foundations for modern humanistic thinking.",
    "Indigenous communities worldwide maintain unique linguistic diversity, traditional ecological knowledge, and sustainable resource management practices worthy of preservation and respect.",
    
    # Education/Learning
    "Educational technology platforms revolutionize learning experiences through interactive multimedia content, personalized instruction algorithms, and collaborative virtual classroom environments.",
    "Lifelong learning strategies help professionals adapt to rapidly changing job markets by continuously developing new skills, pursuing advanced certifications, and staying current with industry trends.",
    "Research methodologies in academic institutions emphasize rigorous experimental design, statistical analysis techniques, and peer review processes to ensure scientific validity and reproducibility.",
    "Critical thinking skills development involves analyzing complex problems, evaluating evidence objectively, and formulating logical arguments based on credible information sources.",
    
    # Multilingual Content
    "La technología de inteligencia artificial está transformando industrias enteras, desde la medicina hasta el transporte, creando nuevas oportunidades y desafíos únicos.",
    "Les innovations scientifiques modernes nécessitent une collaboration internationale pour résoudre des problèmes complexes comme le changement climatique et la durabilité environnementale.",
    "現代のテクノロジーは私たちの日常生活を大きく変えており、スマートフォンやインターネットなしの生活は想像できません。人工知能の発展により、さらなる変化が期待されています。",
    "人工智能和机器学习技术正在快速发展，在医疗诊断、自动驾驶、语言翻译等领域展现出巨大的应用潜力和社会价值。",
    
    # Creative/Artistic
    "Musicians blend traditional instruments with electronic synthesizers, creating innovative soundscapes that challenge conventional genre boundaries and inspire new artistic movements.",
    "Visual artists experiment with digital media, virtual reality installations, and interactive exhibitions to engage audiences in immersive, multisensory creative experiences.",
    "Literary authors explore contemporary themes through diverse narrative techniques, incorporating social commentary, psychological complexity, and innovative storytelling structures.",
    "Film directors utilize advanced cinematography technologies, computer-generated imagery, and sophisticated editing techniques to craft compelling visual narratives.",
    
    # Sports/Recreation
    "Professional athletes train rigorously using scientific methodologies, nutritional optimization, and performance analytics to achieve peak physical conditioning and competitive excellence.",
    "Outdoor recreation activities like hiking, rock climbing, and kayaking provide physical exercise, mental wellness benefits, and opportunities for environmental appreciation.",
    "Team sports development programs focus on skill building, strategic thinking, leadership qualities, and collaborative teamwork essential for both athletic and personal growth.",
    "Fitness technology innovations include wearable devices, mobile applications, and virtual training platforms that help individuals monitor progress and maintain healthy lifestyles.",
    
    # Philosophy/Ethics
    "Ethical considerations in technological development require careful evaluation of potential societal impacts, privacy implications, and equitable access to beneficial innovations.",
    "Philosophical inquiries into consciousness, free will, and human nature continue to challenge our understanding of existence and inform debates about artificial intelligence.",
    "Moral frameworks provide guidance for navigating complex ethical dilemmas in medical practice, environmental policy, and social justice initiatives across diverse cultural contexts.",
    "Democratic institutions depend on informed citizen participation, transparent governance processes, and constitutional protections for fundamental human rights and freedoms.",
    
    # Additional Technical Content
    "Distributed computing systems coordinate multiple processors across networks to solve computationally intensive problems through parallel processing and load balancing algorithms.",
    "Renewable energy technologies including solar panels, wind turbines, and battery storage systems are becoming increasingly cost-effective alternatives to fossil fuel dependence.",
    "Biotechnology applications in agriculture develop drought-resistant crops, improve nutritional content, and reduce pesticide requirements through genetic modification and selective breeding techniques.",
    "Telecommunications infrastructure evolution from analog to digital, wireless to fiber optic networks has revolutionized global communication capabilities and information accessibility."
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