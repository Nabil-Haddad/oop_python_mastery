# MODULE 07 — MAGIC / DUNDER METHODS
"""
"Dunder" = Double UNDERscore. These are special methods Python calls
AUTOMATICALLY in response to built-in syntax (print(), len(), ==, +,
for-loops, calling an object like a function, etc). You've already
used __init__, the most famous dunder. This module covers the rest of
the ones you'll actually use as an AI engineer.


"""
# 1. __repr__ and __str__ -- HOW OBJECTS ARE DISPLAYED


"""

__repr__ : unambiguous, developer-facing. Goal: could you (ideally)
           recreate the object from this string? Shown in the REPL,
           inside lists/dicts, and by print() if __str__ is absent.
__str__  : human-readable, user-facing. What print(obj) shows if defined.
"""


class Tensor:
    def __init__(self, shape):
        self.shape = shape

    def __repr__(self):
        return f"Tensor(shape={self.shape})"

    def __str__(self):
        return f"<a tensor of shape {self.shape}>"


t = Tensor((32, 128))
print(t)          # uses __str__ -> <a tensor of shape (32, 128)>
print(repr(t))    # uses __repr__ -> Tensor(shape=(32, 128))
print([t, t])     # lists always use __repr__ for their elements

"""
Without ANY __repr__ defined, printing an object gives you the
famously useless `<__main__.Tensor object at 0x7f...>`. ALWAYS define
at least __repr__ on your classes -- it pays for itself the first time
you debug with a print statement or in a debugger.
"""
# 2. __eq__ and __hash__ -- CUSTOM EQUALITY


"""

By default, `==` compares OBJECT IDENTITY (same as `is`) unless you
override it. Two Tensor objects with identical shapes are NOT equal by
default -- often not what you want.
"""


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


p1, p2 = Point(1, 2), Point(1, 2)
print(p1 == p2)   # True now (would be False without __eq__)
print(p1 is p2)   # False -- still two different objects in memory

"""
Gotcha: once you define __eq__, Python sets __hash__ to None
automatically (the object becomes UNHASHABLE -- you can't put it in a
set or use it as a dict key), because a mutable object with custom
equality is a footgun as a hash key. If you need both, define
__hash__ explicitly (usually only for genuinely immutable objects).
"""


# 3. __len__, __getitem__, __iter__ -- CONTAINER-LIKE BEHAVIOR


"""
These let YOUR object work with len(), indexing [], and for-loops,
exactly like a built-in list or dict.
"""


class Batch:
    def __init__(self, samples):
        self._samples = samples

    def __len__(self):
        return len(self._samples)

    def __getitem__(self, index):
        return self._samples[index]

    def __iter__(self):
        return iter(self._samples)


b = Batch(["cat.png", "dog.png", "bird.png"])
print(len(b))          # 3  -- uses __len__
print(b[1])             # dog.png -- uses __getitem__
for sample in b:        # uses __iter__
    print("sample:", sample)

"""
This is EXACTLY the mechanism a PyTorch `Dataset` relies on:
`__len__` and `__getitem__` are the two methods PyTorch's DataLoader
calls internally to know how many samples exist and how to fetch one
by index. Understanding dunders means `torch.utils.data.Dataset`
stops looking like special magic and just looks like... two methods.
"""

# 4. __call__ -- MAKING AN OBJECT CALLABLE LIKE A FUNCTION

class Doubler:
    def __call__(self, x):
        return x * 2


double = Doubler()
print(double(21))   # 42 -- calling the OBJECT itself like a function!

"""
This is precisely why in PyTorch you write `output = layer(x)` instead
of `output = layer.forward(x)` even though you defined `forward`, not
`__call__`. `nn.Module.__call__` is defined by PyTorch to internally
invoke your `forward()` (plus some bookkeeping like hooks) -- so
calling the object directly is the intended, idiomatic usage.
"""
# 5. ARITHMETIC DUNDERS: __add__, __sub__, etc.

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v = Vector(1, 2) + Vector(3, 4)
print(v)   # Vector(4, 6)   -- `+` triggered __add__ automatically

"""

QUICK REFERENCE TABLE
    len(obj)  -> __len__
    obj[i]  -> __getitem__ / __setitem__ / __delitem__
    for x in obj -> __iter__ (and __next__ on the returned iterator)
    obj1 == obj2 -> __eq__
    obj1 < obj2 -> __lt__
    obj1 + obj2 -> __add__
    str(obj) -> __str__
    repr(obj) -> __repr__
    obj(...) -> __call__
    with obj: ... -> __enter__ / __exit__  (context managers)
    bool(obj) -> __bool__
"""

if __name__ == "__main__":
    print("\n--- Module 7 demo ---")
    print(list(Batch(["a", "b", "c"])))
