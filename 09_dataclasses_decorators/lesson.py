# MODULE 09 — @dataclass AND CLASS DECORATORS


"""
By now you've written __init__, __repr__, and __eq__ by hand several
times. For classes that are mostly just "bags of related data" (very
common for configs, hyperparameters, records), Python's `dataclasses`
module generates all that boilerplate for you.
"""

# 1. THE BOILERPLATE PROBLEM
class ModelConfigManual:
    def __init__(self, name, lr, batch_size):
        self.name = name
        self.lr = lr
        self.batch_size = batch_size

    def __repr__(self):
        return f"ModelConfigManual(name={self.name!r}, lr={self.lr!r}, batch_size={self.batch_size!r})"

    def __eq__(self, other):
        if not isinstance(other, ModelConfigManual):
            return NotImplemented
        return (self.name, self.lr, self.batch_size) == (other.name, other.lr, other.batch_size)


"""
Three attributes, and already __init__/__repr__/__eq__ are all
hand-written and easy to get subtly wrong (typos, forgetting a field
in __eq__, etc). This is exactly the pattern @dataclass automates.
"""

# 2. @dataclass -- SAME RESULT, NO BOILERPLATE

from dataclasses import dataclass, field


@dataclass
class ModelConfig:
    name: str
    lr: float
    batch_size: int


cfg1 = ModelConfig("resnet", 0.01, 32)
cfg2 = ModelConfig("resnet", 0.01, 32)
print(cfg1)              # ModelConfig(name='resnet', lr=0.01, batch_size=32)
print(cfg1 == cfg2)      # True -- field-by-field equality, generated for you

"""
@dataclass reads the CLASS-LEVEL TYPE-ANNOTATED variables (name: str,
lr: float, batch_size: int) and auto-generates __init__, __repr__, and
__eq__ using exactly those fields, in that order. Note: the type
annotations (`: str`, `: float`) are NOT enforced at runtime by Python
itself -- they're documentation/tooling hints (useful for IDEs, mypy,
etc), not a validation mechanism.
"""
# 3. DEFAULT VALUES AND MUTABLE DEFAULTS

@dataclass
class TrainingRun:
    name: str
    epochs: int = 10                       # simple default -- fine directly
    tags: list = field(default_factory=list)  # MUTABLE default -- needs field()


run1 = TrainingRun("exp_a")
run2 = TrainingRun("exp_b")
run1.tags.append("baseline")
print(run1.tags, run2.tags)   # ['baseline'] []  -- correctly independent

"""
Recall Module 02's mutable-default trap for plain class attributes.
`@dataclass` has the SAME underlying danger for `list`/`dict` defaults
-- you CANNOT write `tags: list = []` directly (dataclass will even
raise an error at class-definition time to stop you). You must use
`field(default_factory=list)`, which tells dataclass "call list() FRESH
for every new instance" instead of sharing one list across all of them.

"""
# 4. frozen=True -- IMMUTABLE DATACLASSES
"""
For values that should never change after creation (a common goal for
configs, once loaded), `frozen=True` makes the dataclass immutable and
hashable.
"""


@dataclass(frozen=True)
class ImmutableConfig:
    lr: float
    seed: int


icfg = ImmutableConfig(0.01, 42)
try:
    icfg.lr = 0.5   # raises -- frozen instances can't be mutated
except Exception as e:
    print("Blocked mutation:", type(e).__name__, e)


# 5. WHAT'S ACTUALLY HAPPENING: @dataclass IS A CLASS DECORATOR

"""
`@dataclass` is a DECORATOR applied to a class (not just functions,
decorators work on classes too). Mechanically, `@dataclass` above
`class ModelConfig:` is EXACTLY equivalent to:

    class ModelConfig:
        ...
    ModelConfig = dataclass(ModelConfig)

The decorator takes your plain class, INSPECTS its type annotations,
and returns a MODIFIED version of the class with __init__/__repr__/
__eq__ injected in. This is the general pattern for any class
decorator: take a class in, return a class (possibly the same one,
modified) out.

A tiny custom class decorator, to make the mechanism concrete:
"""


def add_greeting(cls):
    cls.greet = lambda self: f"Hello from {self.__class__.__name__}"
    return cls


@add_greeting
class Agent:
    pass


print(Agent().greet())   # Hello from Agent


# 6. WHEN TO USE @dataclass vs A REGULAR CLASS

"""
Use @dataclass for: configs, records, simple data containers (DTOs)
  where the main job is holding a fixed set of typed fields.
Use a regular class when: the class has significant BEHAVIOR
  (methods doing real work), complex validation better expressed
  through @property setters, or needs custom __init__ logic that
  goes beyond "just store these fields".
Nothing stops you from ADDING methods to a @dataclass too, it's
still a normal class underneath, just with generated boilerplate.
"""

if __name__ == "__main__":
    print("\n--- Module 9 demo ---")
    print(ModelConfig("bert", 0.0001, 16))
