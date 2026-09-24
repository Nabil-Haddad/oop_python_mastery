# MODULE 10 — DESCRIPTORS: WHAT @property ACTUALLY IS UNDER THE HOOD

"""
Module 03 used @property as a black box: "it lets a method act like an
attribute." This module opens that box. Understanding descriptors is
what lets you understand HOW @property, @staticmethod, @classmethod,
and even how instance methods themselves actually work internally.
"""

# 1. WHAT IS A DESCRIPTOR?
"""
A descriptor is any object whose class defines __get__ (and optionally
__set__ / __delete__), and which is stored as a CLASS attribute. When
Python looks up that attribute on an INSTANCE, it detects the
descriptor protocol and calls __get__/__set__ instead of just handing
back the raw value.
"""


class LoggedAttribute:
    # A reusable descriptor: logs every read and write.

    def __init__(self, name):
        self.name = name  # the attribute name we're managing

    def __get__(self, instance, owner):
        # instance = the object being accessed (e.g. the Model instance)
        # owner    = the class itself (e.g. Model)
        print(f"GET {self.name}")
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        print(f"SET {self.name} = {value}")
        instance.__dict__[self.name] = value


class Model:
    lr = LoggedAttribute("lr")  # a descriptor, assigned as a CLASS attribute

    def __init__(self, lr):
        self.lr = lr   # this line triggers LoggedAttribute.__set__


m = Model(0.01)     # prints: SET lr = 0.01
print(m.lr)          # prints: GET lr  , then 0.01

"""
This is the SAME mechanism @property uses internally. In fact,
`property` is just a BUILT-IN descriptor class that Python provides so
you don't have to write __get__/__set__ by hand every time. Recall
Module 03:

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        ...

`property(fget, fset)` builds a descriptor object behind the scenes,
using your getter/setter functions as its __get__/__set__.
"""

# 2. WHY THIS MATTERS: REUSABLE VALIDATION LOGIC
"""
The power of writing your OWN descriptor (instead of @property) is
REUSE: one descriptor class can validate MANY different attributes,
across MANY different classes, without repeating the validation logic
each time.
"""


class PositiveNumber:
    # A reusable validated-number descriptor.

    def __set_name__(self, owner, name):
        # Automatically called by Python at class-creation time,
        # telling the descriptor which attribute name it was assigned to.
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.private_name} must be positive, got {value}")
        setattr(instance, self.private_name, value)


class TrainingConfig:
    lr = PositiveNumber()
    batch_size = PositiveNumber()

    def __init__(self, lr, batch_size):
        self.lr = lr
        self.batch_size = batch_size


class InferenceConfig:
    temperature = PositiveNumber()  # SAME descriptor, reused on a different class

    def __init__(self, temperature):
        self.temperature = temperature


tc = TrainingConfig(lr=0.01, batch_size=32)
print(tc.lr, tc.batch_size)
try:
    tc.batch_size = -8
except ValueError as e:
    print("Rejected:", e)

ic = InferenceConfig(temperature=0.7)
print(ic.temperature)

"""
Compare to Module 03's approach: there, EVERY validated attribute
needed its OWN hand-written @property + setter pair, repeating the
`if value <= 0: raise ValueError` check every time. Here, ONE
`PositiveNumber` descriptor class is written ONCE and reused across
`lr`, `batch_size`, `temperature`, and any future field, on any class.

"""
# 3. DATA vs NON-DATA DESCRIPTORS (brief, for awareness)
"""

- A descriptor with __set__ (or __delete__) is a "data descriptor" --
  it takes priority even over an instance's own __dict__ entry.
- A descriptor with ONLY __get__ (no __set__) is a "non-data
  descriptor" -- an instance attribute of the same name can override it.
This is exactly why FUNCTIONS defined in a class body work as methods:
a plain function is itself a non-data descriptor (via its __get__),
which is how `instance.method` automatically becomes a "bound method"
with `self` already filled in. You don't need to memorize this deeply
-- just know it's the same underlying protocol powering methods,
@property, @staticmethod, and @classmethod, uniformly.
"""

# 4. WHEN TO REACH FOR A CUSTOM DESCRIPTOR
"""
- @property: one-off validated attribute on a SINGLE class. Use this
  by default -- it's simpler and more common.
- Custom descriptor class: the SAME validation/behavior needs to be
  reused across MANY attributes and/or MANY classes. This is the
  "don't repeat yourself" upgrade once @property duplication piles up.
"""

if __name__ == "__main__":
    print("\n--- Module 10 demo ---")
    cfg = TrainingConfig(lr=0.001, batch_size=64)
    print(cfg.lr, cfg.batch_size)
