# MODULE 04 — INHERITANCE

"""
Inheritance lets a class (the "child"/"subclass") reuse and extend the behavior of another class
(the "parent"/"superclass"), instead of copy-pasting code. This is EXACTLY the mechanism behind
`class MyModel(nn.Module):` in PyTorch, `class MyClassifier(BaseEstimator):` in scikit-learn, etc.
"""


# 1. BASIC INHERITANCE

class Layer:
    def __init__(self, name):
        self.name = name

    def forward(self, x):
        raise NotImplementedError("Subclasses must implement forward()")

    def describe(self):
        return f"Layer(name={self.name})"


class ReLU(Layer):    # ReLU INHERITS from Layer
    def forward(self, x):
        return max(0, x)  # ReLU-specific behavior


relu = ReLU("relu1")
print(relu.name)    
print(relu.describe())  
print(relu.forward(-5))

"""
Wait -- `relu.name` worked even though ReLU never wrote its own
__init__? That's because ReLU didn't define __init__ at all, so Python falls back to the PARENT's
__init__ automatically.
This is the essence of inheritance: anything the child doesn't define, it inherits as-is.
"""

# 2. OVERRIDING __init__ AND super()
"""
Usually a subclass DOES need its own __init__ (to add new attributes), but still wants the parent's
setup logic to run too. `super()` gives you a handle to the parent class so you can call its methods
explicitly instead of rewriting them.
"""


class Conv2D(Layer):
    def __init__(self, name, in_channels, out_channels, kernel_size):
        super().__init__(name)  # runs Layer.__init__(self, name) for us
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size

    def forward(self, x):
        return f"convolved({x}) with {self.out_channels} filters"

    def describe(self):
        # Extend the parent's describe() rather than fully replacing it
        base = super().describe()
        return f"{base}, in={self.in_channels}, out={self.out_channels}, k={self.kernel_size}"


conv = Conv2D("conv1", in_channels=3, out_channels=64, kernel_size=3)
print(conv.describe())    # Layer(name=conv1), in=3, out=64, k=3

"""
Without super().__init__(name), you'd have to manually rewrite `self.name = name` yourself, 
fine for one attribute, painful (and error-prone) for a parent with a complex setup routine. `super()`
keeps the parent's setup logic in exactly ONE place.
"""



# 3. isinstance vs type -- WHY IT MATTERS

print(isinstance(conv, Conv2D))  # True
print(isinstance(conv, Layer))   # True -- a Conv2D IS-A Layer
print(type(conv) is Layer)       # False -- exact type is Conv2D, not Layer

"""
Use isinstance() when you want to know "can I treat this object as a Layer?" (the common case).
Use type() only when you specifically need the EXACT class, ignoring the whole inheritance chain
rare, and usually a sign you should reconsider the design.
"""



#4. MULTIPLE INHERITANCE AND MRO (Method Resolution Order)
"""
Python allows a class to inherit from more than one parent. When several parents define the same
method name, Python needs a deterministic rule for which one wins: the MRO (a specific left-to-right,
depth-first-ish algorithm called C3 linearization). You can always inspect it directly.
"""


class Loggable:
    def log(self):
        return f"[LOG] {self.__class__.__name__}"

    def summary(self):
        return "summary from Loggable"


class Serializable:
    def to_dict(self):
        return self.__dict__

    def summary(self):
        return "summary from Serializable"


class ExperimentRun(Loggable, Serializable):
    def __init__(self, name):
        self.name = name


run = ExperimentRun("exp1")

print(run.log())        # from Loggable -- no conflict, only Loggable has it
print(run.to_dict())     # from Serializable -- no conflict, only Serializable has it

print(run.summary())     # CONFLICT: both define summary(). Who wins?
print(ExperimentRun.__mro__)    # (ExperimentRun, Loggable, Serializable, object)

# Python walks this list left to right looking for summary(). # ExperimentRun doesn't define it -> check Loggable -> FOUND IT, stop.
# Serializable's summary() is never even reached.

"""
Proof it's really about ORDER, not which class is "more important": swap the parent order and the winner flips.
"""


class ExperimentRunFlipped(Serializable, Loggable):  # order swapped
    def __init__(self, name):
        self.name = name


run2 = ExperimentRunFlipped("exp2")
print(run2.summary())           # now Serializable wins, since it's listed first
print(ExperimentRunFlipped.__mro__)

"""
Practical guidance: reach for multiple inheritance mainly for small, focused "mixin" classes like
Loggable/Serializable above -- each adding ONE independent capability, with no overlapping method 
names. Avoid deep, tangled multi-parent hierarchies; they get hard to reason
about fast. (Composition, Module 08, is often a cleaner alternative.)


"""
# 5. "IS-A" TEST
"""

Before inheriting, ask: is a Conv2D truly A Layer? Yes -- use inheritance.
Is a Trainer truly A Model? No -- a Trainer HAS-A model. Misusing inheritance where composition 
belongs is one of the most common real-world OOP design mistakes.
"""

if __name__ == "__main__":
    print("\n--- Module 4 demo ---")
    print(conv.forward("tensor_x"))
