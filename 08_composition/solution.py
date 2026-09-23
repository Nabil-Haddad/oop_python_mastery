# MODULE 08 — SOLUTIONS


class Tokenizer:
    def tokenize(self, text):
        return text.split()

class Embedder:
    def embed(self, tockens):
        return [len(t) for t in tockens]

class EncodingPipeline:
    def __init__(self, tockenizer, embedder):
        self.tockenizer = tockenizer
        self.embedder = embedder

    def encode(self, text):
        tockenized_text = self.tockenizer.tokenize(text)
        return self.embedder.embed(tockenized_text)


class UppercaseCountEmbedder:
    def embed(self, tockens):
        return [sum(1 for ch in t if ch.isupper()) for t in tockens]


if __name__ == "__main__":
    pipeline = EncodingPipeline(Tokenizer(), Embedder())
    assert pipeline.encode("hi there friend") == [2, 5, 6]

    pipeline = EncodingPipeline(Tokenizer(), Embedder())
    pipeline.embedder = UppercaseCountEmbedder()   # swap at runtime
    assert pipeline.encode("Hi THERE friend") == [1, 5, 0]


