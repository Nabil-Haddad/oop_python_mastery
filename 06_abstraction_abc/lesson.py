# MODULE 06 — ABSTRACTION: ENFORCING CONTRACTS WITH `abc`

"""
In Module 05 we wrote base classes like `Layer` whose `forward()` just
raised NotImplementedError. That's a CONVENTION, not an ENFORCED rule --
nothing stops someone from instantiating `Layer()` directly and
crashing at CALL time instead of at CREATION time. The `abc` module
(Abstract Base Classes) lets Python enforce the contract for you.

"""

# 1. THE PROBLEM WITH "RAISE NotImplementedError"


class LayerLoose:
    def forward(self, x):
        raise NotImplementedError


layer = LayerLoose()  # <-- this succeeds! No error yet.
try:
    layer.forward(5)  # only NOW does it blow up
except NotImplementedError:
    print("Failed late, at call time -- not ideal.")




# 2. ABC + @abstractmethod -- FAIL FAST, AT INSTANTIATION TIME

from abc import ABC, abstractmethod


class Layer(ABC):  # inherit from ABC to make this class abstract
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def forward(self, x):
          #Every concrete subclass MUST implement this."""
          # the body is irrelevant, it's never actually run
          pass

    def describe(self):
        # Regular (non-abstract) methods work exactly as normal --
        # abstract classes can still provide real, shared behavior.
        return f"Layer({self.name})"


try:
    l = Layer("generic")  # <-- fails IMMEDIATELY, before any .forward() call
except TypeError as e:
    print("Blocked at instantiation:", e)


class ReLU(Layer):
    def forward(self, x):
        return max(0, x)


relu = ReLU("relu1")   # fine -- ReLU implemented the required method
print(relu.describe())
print(relu.forward(-3))


class BrokenLayer(Layer):
    # Forgot to implement forward() at all!
    pass


try:
    b = BrokenLayer("oops")
except TypeError as e:
    print("Blocked -- missing forward():", e)

"""
This is a MUCH better failure mode: you find out about a missing
implementation the moment someone tries to construct the broken class,
not buried three function calls deep during a training run at 2am.
"""

# 3. ABSTRACT CLASSES CAN MIX ABSTRACT + CONCRETE METHODS



"""
As shown above, `describe()` on Layer is a completely normal, fully
implemented method. Abstract classes are not "empty templates" -- they
can hold as much shared, working logic as you want. Only the methods
you explicitly mark @abstractmethod are mandatory for subclasses to
fill in. This is exactly how PyTorch's own `nn.Module` isn't abstract
via `abc` (it uses a different mechanism), but the DESIGN PATTERN is
identical to how libraries like scikit-learn's `BaseEstimator` and
HuggingFace's `PreTrainedModel` define required methods subclasses
must fill in while providing tons of shared machinery for free.
"""

# 4. WHEN TO USE ABC vs PLAIN DUCK TYPING
"""
Use abc when:
  - You're building a library/framework other people (or future-you)
    will subclass, and you want to GUARANTEE a contract is honored.
  - Getting it wrong should fail loudly and immediately, not silently
    or late.

Stick with plain duck typing (Module 05) when:
  - You're writing quick, flexible, small-scale code where formality
    isn't worth the ceremony.
  - You genuinely want ANY object with the right method to work,
    without forcing a shared inheritance hierarchy at all.
"""

if __name__ == "__main__":
    print("\n--- Module 6 demo ---")
    print(ReLU("r").forward(10))
