class BatchConfig:
    def __init__(self, batch_size):
        self.batch_size = batch_size

    @property
    def batch_size(self):
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"batch_size must be a positive int, got {value!r}")
        self._batch_size = value


class TokenBudget:
    def __init__(self, prompt_tokens, max_tokens):
        self.prompt_tokens = prompt_tokens
        self.max_tokens = max_tokens

    @property
    def remaining(self):
        return self.max_tokens - self.prompt_tokens


class Tokenizer:
    def __init__(self, vocab_size):
        self.vocab_size = vocab_size
        self._cache = {}

    def encode(self, token):
        if token not in self._cache:
            self._cache[token] = len(token)
        return self._cache[token]



if __name__ == "__main__":
    bc = BatchConfig(32)
    assert bc.batch_size == 32

    try:
        BatchConfig(-4)
        assert False, "should have raised"
    except ValueError:
        pass

    try:
        BatchConfig(2.5)
        assert False, "should have raised"
    except ValueError:
        pass


    tb = TokenBudget(prompt_tokens=100, max_tokens=4096)
    assert tb.remaining == 3996
    try:
        tb.remaining = 10
        assert False, "should have raised"
    except AttributeError:
        pass

    tb = TokenBudget(prompt_tokens=100, max_tokens=4096)
    assert tb.remaining == 3996
    try:
        tb.remaining = 10
        assert False
    except AttributeError:
        pass

    tok = Tokenizer(vocab_size=30000)
    assert tok.vocab_size == 30000
    assert tok.encode("hello") == 5
    assert "hello" in tok._cache



