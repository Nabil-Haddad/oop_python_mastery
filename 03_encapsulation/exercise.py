# MODULE 03 — EXERCISES 



# EXERCISE 1: Validated property

# Create class `BatchConfig` with __init__(self, batch_size) that stores
# batch_size through a property setter which raises ValueError if
# batch_size is not a positive integer (use isinstance check for int,
# and check > 0).

class BatchConfig:
    pass  # replace


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



# EXERCISE 2: Read-only computed property

# Create class `TokenBudget` with __init__(self, prompt_tokens, max_tokens)
# and a READ-ONLY property `remaining` = max_tokens - prompt_tokens.
# Attempting to set .remaining directly must raise AttributeError.

class TokenBudget:
    pass  # replace


# tb = TokenBudget(prompt_tokens=100, max_tokens=4096)
# assert tb.remaining == 3996
# try:
#     tb.remaining = 10
#     assert False, "should have raised"
# except AttributeError:
#     pass



# EXERCISE 3: Protected vs public judgment call

# Create class `Tokenizer` with:
#   - public attribute `vocab_size` (set directly in __init__)
#   - protected attribute `_cache` (a dict, internal only, set in __init__)
#   - a public method `encode(self, token)` that checks _cache first,
#     and if missing, computes `len(token)` as a fake "id", stores it in
#     _cache, and returns it.

class Tokenizer:
    pass  # replace


# tok = Tokenizer(vocab_size=30000)
# assert tok.vocab_size == 30000
# assert tok.encode("hello") == 5
# assert "hello" in tok._cache


if __name__ == "__main__":
    print("Exercise 1 checks passed if no AssertionError raised above.")
