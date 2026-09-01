# MODULE 02 — CLASS ATTRIBUTES, INSTANCE ATTRIBUTES, AND THE THREE METHOD TYPES

# 1. INSTANCE ATTRIBUTES vs CLASS ATTRIBUTES
"""
Instance attributes (Module 1) live on `self` -> unique per object. Class attributes live on the CLASS
itself -> SHARED by every object, unless a specific instance overrides it.

Analogy: think of a class attribute as a "factory default setting" printed on the blueprint. 
Every object reads it from the blueprint UNLESS that specific object has been given its own override.
"""


class Model:
    # CLASS ATTRIBUTE — one shared value, defined outside any method,
    # directly in the class body.
    framework = "pytorch"

    def __init__(self, name):
        # INSTANCE ATTRIBUTE — each object gets its own.
        self.name = name


m1 = Model("resnet")
m2 = Model("bert")

print(m1.framework, m2.framework)  # pytorch pytorch  (shared)

# Change it via the CLASS -> every instance that hasn't overridden it sees the change:
Model.framework = "jax"
print(m1.framework, m2.framework)  # jax jax



# Change it via ONE INSTANCE -> creates a new instance attribute that SHADOWS the class attribute for that object only. 
# It does not touch the class attribute or any other instance.
m1.framework = "tensorflow"
print(m1.framework, m2.framework)  # tensorflow jax
print(Model.framework)             # jax  (class attribute untouched)




"""
This is a classic: `m1.framework = "tensorflow"` does NOT modify the shared class attribute. 
It creates a brand-new instance attribute on m1 that happens to have the same name and now hides the class one
whenever you look it up through m1.
"""



# MUTABLE class attributes are a real trap:
class BuggyRegistry:
    items = []  # DANGER: one list shared by ALL instances

    def add(self, item):
        # `self.items` is a READ, not a write. Python looks for `items` on
        # the instance first, finds nothing there, and falls back to the
        # CLASS attribute -- so this fetches the one shared list object.
        # `.append(item)` then mutates THAT SAME list in place.

        # Contrast this with `m1.framework = "tensorflow"` above: that was
        # an ASSIGNMENT through self, which always creates/overwrites an
        # INSTANCE attribute and never touches the class attribute.
        # `self.items.append(item)` never assigns to `self.items`, so no
        # instance attribute is ever created here -- every object keeps
        # reading and mutating the one list living on the class.
        self.items.append(item)


a = BuggyRegistry()
b = BuggyRegistry()
a.add("model_a")
b.add("model_b")
print(a.items)  # ['model_a', 'model_b']  <- b's item leaked into a!
print(a.items is b.items)  # True -- same list object in memory

"""
Fix: mutable defaults belong in __init__ as instance attributes so
each object gets its own fresh list/dict.
"""


class FixedRegistry:
    def __init__(self):
        self.items = []  # new list per instance

    def add(self, item):
        self.items.append(item)



# 2. THREE KINDS OF METHODS
"""
INSTANCE METHOD — normal case. First param `self`. Operates on one object.
CLASS METHOD — decorated @classmethod. First param `cls` (the class itself, not an instance). Operates on/about the class.
                    Common use: alternative constructors.
STATIC METHOD — decorated @staticmethod. No automatic first param at all. It's a plain function that happens to live inside
                    the class's namespace because it's thematically related.
"""


class Dataset:
    default_split = "train"

    def __init__(self, path, split):
        self.path = path
        self.split = split

    # INSTANCE METHOD: needs a specific object's data
    def describe(self):
        return f"Dataset({self.path}, split={self.split})"

    # CLASS METHOD: an alternative constructor. Doesn't need an
    # existing instance -- it BUILDS one, using `cls` instead of
    # hardcoding "Dataset" (so subclasses build the right type too).
    @classmethod
    def from_default_split(cls, path):
        return cls(path, split=cls.default_split)

    # CLASS METHOD used to WRITE a class attribute. `cls.default_split = ...`
    # is an assignment through `cls`, so -- just like `Model.framework = "jax"`
    @classmethod
    def set_default_split(cls, split):
        cls.default_split = split

    # STATIC METHOD: logically related to Dataset, but needs no
    # access to `self` or `cls` at all -- pure utility function.
    @staticmethod
    def is_valid_split(split):
        return split in ("train", "val", "test")


ds = Dataset.from_default_split("/data/coco")
print(ds.describe())                       # Dataset(/data/coco, split=train)
print(Dataset.is_valid_split("val"))       # True
print(Dataset.is_valid_split("banana"))    # False

Dataset.set_default_split("val")
ds2 = Dataset.from_default_split("/data/coco")
print(ds2.describe())                      # Dataset(/data/coco, split=val)
print(Dataset.default_split)               # val  (class attribute actually changed)

"""
Why `cls` instead of hardcoding the class name inside a classmethod?
If someone subclasses Dataset later (Module 4 territory), `cls` will
correctly refer to the SUBCLASS when called on the subclass, so
`from_default_split` keeps working correctly without modification.
This is a preview of why classmethods matter for extensible libraries
like HuggingFace's `from_pretrained()` — that's a classmethod pattern.

RULE OF THUMB for choosing:
  - Needs `self.something`? -> instance method
  - Needs to build/return an instance, or read/set class-level state? -> classmethod
  - Needs neither, just grouped for organization? -> staticmethod
"""

if __name__ == "__main__":
    print("\n--- Module 2 demo ---")
    r = FixedRegistry()
    r.add("x")
    print(r.items)
