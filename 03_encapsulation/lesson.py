# MODULE 03 — ENCAPSULATION

"""
Encapsulation = controlling access to an object's internal data, so the
object can protect its own invariants (rules that must always hold true)
instead of trusting outside code to be careful.
"""


# 1. PYTHON HAS NO TRUE "PRIVATE" -- ONLY CONVENTIONS
"""
Unlike Java/C++, Python doesn't enforce access control at the language
level. Instead it uses NAMING CONVENTIONS everyone agrees to respect:

    self.name -> PUBLIC: part of the intended interface, use freely
    self._name -> PROTECTED (by convention only): "internal detail,
                          don't touch from outside, but subclasses may need it"
    self.__name -> NAME-MANGLED: Python rewrites this to
                          self._ClassName__name internally, which makes
                          accidental access/collision from subclasses hard
                          (not impossible, just inconvenient enough to discourage it)
"""

class Model:
    def __init__(self, name):
        self.name = name  # public
        self._cach = {}    # Procted 
        self.__api_key = "secret" # Name-Mangeled


m = Model("resnet")
print(m.name)
print(m._cach)
# print(m.__api_key)  # AttributeError
print(m._Model__api_key)


"""
So __ isn't real privacy, it's a collision-avoidance mechanism, mainly
useful so subclasses don't accidentally clobber a base class's internal
attribute with the same name. Treat single underscore as the everyday
"this is internal" signal in your own code.
"""


# 2. WHY HIDE DATA AT ALL? -- PROTECTING INVARIANTS

"""
Say a training config must always have a POSITIVE learning rate. If we
expose `learning_rate` as a raw public attribute, nothing stops:

    cfg.learning_rate = -5   # nonsensical, but Python won't stop you

We want validation to run EVERY time the value is set, not just at
construction. That's what @property is for.
"""



# 3. @property : CONTROLLED ACCESS THAT LOOKS LIKE A PLAIN ATTRIBUTE\

class TrainingConfig:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    @property
    def learning_rate(self):
        # The getter. Runs whenever someone reads cfg.learning_rate
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        # The setter. Runs whenever someone writes cfg.learning_rate = x
        if value <= 0:
            raise ValueError(f"learning_rate must be positive, got {value}")
        self._learning_rate = value


cfg = TrainingConfig(0.01)
print(cfg.learning_rate)     
cfg.learning_rate = 0.5     
print(cfg.learning_rate)

try:
    cfg.learning_rate = -1
except ValueError as e:
    print("Rejected:", e)

"""
Notice the calling code (`cfg.learning_rate = 0.5`) looks IDENTICAL to
a plain public attribute assignment. That's the whole point: consumers
of your class never need to know whether they're touching a raw
attribute or a validated property. This means you can START a class
with plain public attributes, and LATER upgrade one to a property with
validation, WITHOUT breaking any code that uses your class. That's a
huge deal in real codebases and libraries.
"""


# 4. READ-ONLY PROPERTIES (no setter at all)

class Dataset:
    def __init__(self, samples):
        self._samples = samples

    @property
    def size(self):
        # Computed on the fly, and impossible to overwrite from outside.
        return len(self._samples)


ds = Dataset([1, 2, 3, 4])
print(ds.size)     # 4

try:
    ds.size = 100   # AttributeError: can't set attribute (no setter defined)
except AttributeError as e:
    print("Rejected:", e)



# 5. ENCAPSULATION IS ABOUT INTERFACE STABILITY, NOT SECRECY
"""
The goal isn't to hide things -- it's to draw a clear
line between:
  - the PUBLIC INTERFACE (what other code should rely on)
  - the INTERNAL IMPLEMENTATION (details you're free to change later without breaking
    anyone, including future-you)

A well-encapsulated class lets you rewrite its internals completely while every external
caller keeps working unchanged.
"""


if __name__ == "__main__":
    print("\n--- Module 3 demo ---")
    c = TrainingConfig(0.001)
    print(c.learning_rate)