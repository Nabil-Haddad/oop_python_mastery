# MODULE 08 — EXERCISES



# EXERCISE 1: Build via composition, not inheritance

# Create class `Tokenizer` with method `tokenize(self, text)` returning
# text.split().
# Create class `Embedder` with method `embed(self, tokens)` returning
# [len(t) for t in tokens] (fake embedding: length of each token).
# Create class `EncodingPipeline` that HAS-A tokenizer and HAS-A
# embedder (passed into __init__), with method `encode(self, text)`
# that tokenizes then embeds.

class Tokenizer:
    pass  # replace


class Embedder:
    pass  # replace


class EncodingPipeline:
    pass  # replace


# pipeline = EncodingPipeline(Tokenizer(), Embedder())
# assert pipeline.encode("hi there friend") == [2, 5, 6]



# EXERCISE 2: Swappable components at runtime

# Create an alternate embedder `UppercaseCountEmbedder` with the same
# `embed(self, tokens)` interface, returning the count of uppercase
# characters per token instead. Prove you can swap it into an existing
# EncodingPipeline instance WITHOUT creating a new pipeline object.

class UppercaseCountEmbedder:
    pass  # replace


# pipeline = EncodingPipeline(Tokenizer(), Embedder())
# pipeline.embedder = UppercaseCountEmbedder()   # swap at runtime
# assert pipeline.encode("Hi THERE friend") == [1, 5, 0]


if __name__ == "__main__":
    print("Uncomment assertions above as you implement each class.")
