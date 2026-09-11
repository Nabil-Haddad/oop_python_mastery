class Embedding:
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f"Embedding({self.values})"

    def __eq__(self, other):
        if not isinstance(other , Embedding):
            return False
        if self.values == other.values:
            return True


# EXERCISE 2: Dataset-style dunders (__len__, __getitem__, __iter__)

# Create class `TextDataset` wrapping a list of strings in __init__.
# Implement __len__, __getitem__(index), and __iter__.

class TextDataset:
    def __init__(self, data):
        self._data: list[str] = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)



class Scaler:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor





if __name__ == "__main__":
    e1 = Embedding([0.1, 0.2, 0.3])
    e2 = Embedding([0.1, 0.2, 0.3])
    e3 = Embedding([0.9, 0.9, 0.9])
    assert e1 == e2
    assert e1 != e3
    assert repr(e1) == "Embedding([0.1, 0.2, 0.3])"


    ds = TextDataset(["hello", "world", "foo"])
    assert len(ds) == 3
    assert ds[1] == "world"
    assert list(ds) == ["hello", "world", "foo"]


    scaler = Scaler(3)
    assert scaler(10) == 30