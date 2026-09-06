# MODULE 07 — EXERCISES


# EXERCISE 1: __repr__ and __eq__

# Create class `Embedding` storing a list of floats `self.values` in
# __init__. Implement:
#   __repr__ -> f"Embedding({self.values})"
#   __eq__   -> True if both are Embedding and values lists are equal

class Embedding:
    pass  # replace


e1 = Embedding([0.1, 0.2, 0.3])
e2 = Embedding([0.1, 0.2, 0.3])
e3 = Embedding([0.9, 0.9, 0.9])
assert e1 == e2
assert e1 != e3
assert repr(e1) == "Embedding([0.1, 0.2, 0.3])"



# EXERCISE 2: Dataset-style dunders (__len__, __getitem__, __iter__)

# Create class `TextDataset` wrapping a list of strings in __init__.
# Implement __len__, __getitem__(index), and __iter__.

class TextDataset:
    pass  # replace


# ds = TextDataset(["hello", "world", "foo"])
# assert len(ds) == 3
# assert ds[1] == "world"
# assert list(ds) == ["hello", "world", "foo"]



# EXERCISE 3: __call__

# Create class `Scaler` with __init__(self, factor) storing self.factor,
# and __call__(self, x) returning x * self.factor. It should be usable
# as `scaler(5)`, NOT `scaler.call(5)`.

class Scaler:
    pass  # replace

# scaler = Scaler(3)
# assert scaler(10) == 30


if __name__ == "__main__":
    print("Exercise 1 checks passed if no AssertionError raised above.")
