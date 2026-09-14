# MODULE 08 — SOLUTIONS


class Tokenizer:
    def tokenize(self, text):
        return text.split()


class Embedder:
    def embed(self, tokens):
        return [len(t) for t in tokens]


class UppercaseCountEmbedder:
    def embed(self, tokens):
        return [sum(1 for c in t if c.isupper()) for t in tokens]


class EncodingPipeline:
    def __init__(self, tokenizer, embedder):
        self.tokenizer = tokenizer
        self.embedder = embedder

    def encode(self, text):
        tokens = self.tokenizer.tokenize(text)
        return self.embedder.embed(tokens)


if __name__ == "__main__":
    pipeline = EncodingPipeline(Tokenizer(), Embedder())
    assert pipeline.encode("hi there friend") == [2, 5, 6]

    pipeline.embedder = UppercaseCountEmbedder()
    assert pipeline.encode("Hi THERE friend") == [1, 5, 0]

    print("All Module 8 checks passed.")
