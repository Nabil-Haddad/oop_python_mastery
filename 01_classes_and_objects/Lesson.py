# MODULE 01 — CLASSES & OBJECTS: THE ABSOLUTE BASICS



# 1. WHAT IS A CLASS?


"""
A class is a BLUEPRINT. It does not hold data itself, it describes
what data (attributes) and behavior (methods) objects made from it
will have.

An OBJECT (a.k.a. an "instance") is a concrete thing built from that
blueprint, living in memory, with its own actual values.

    Blueprint  -> class Dog
    Actual dog -> my_dog = Dog()
"""

# The class
class Dog:
    pass

# The objects
d1 = Dog()
d2 = Dog()

print(type(d1))
print(d1 is d2)
print(isinstance(d1, Dog))


# 2. ADDING ATTRIBUTES TO AN OBJECT (the messy, manual way first)

d1.name = "rex"
d1.breed = "Labrador"
print(d1.name, d1.breed)

"""
This works, but it's fragile: d2 has no .name at all. If you tried `print(d2.name)` right now you'd 
get an AttributeError. We need a way to GUARANTEE that every object built from the class starts 
with the attributes it needs. That's what the constructor is for.
"""



# 3. THE CONSTRUCTOR: __init__

"""
`__init__` is a special method (a "dunder" method) that Python automatically 
calls the moment an objectis created. Its job is to set up the object's starting state.

`self` is the FIRST parameter of every instance method, including
__init__. It is a reference to "the specific object being built /acted upon right now".
Python passes it automatically.
You never type it in when you actually construct the object.
"""

class Dataset:
    def __init__(self, name, num_samples):
        self.name = name 
        self.num_samples = num_samples

train_set = Dataset("imagenet-train", 1_281_167)
val_set = Dataset("imagenet-val", 50_000)

print(train_set.name, train_set.num_samples)
print(val_set.name, val_set.num_samples)


"""
Trace through exactly what happened when you wrote `Dataset("imagenet-train", 1281167)`:

1. Python allocates a new, empty object in memory.
2. Python calls Dataset.__init__(that_new_object, "imagenet-train", 1281167)
3. Inside __init__, `self` IS that_new_object.
4. `self.name = name` attaches "imagenet-train" onto that specific object.
5. The now-initialized object is handed back and assigned to `train_set`.

`self` is NOT a keyword. You could technically call it anything
(`this`, `obj`, `me`) — but every Python developer on Earth uses `self`
by convention, and you should too. Consistency across a codebase
matters more than personal preference here.
"""

# 5. ATTRIBUTES vs METHODS
"""
- ATTRIBUTE = a variable that belongs to an object (data)
- METHOD = a function that belongs to a class (behavior), always takes `self` as its first parameter so it can
                read/modify that object's attributes.
"""

class Dataset2:
    def __init__(self, name, num_samples):
        self.name = name
        self.num_samples = num_samples

    def describe(self):
        return f"{self.name}: {self.num_samples} samples"

    def is_large(self, threshold=100_000):
        return self.num_samples > threshold


ds = Dataset2("coco",330_000)
print(ds.describe())        
print(ds.is_large())       
print(ds.is_large(500_000)) 


"""
Important mechanical detail: when you write `ds.describe()`, Python translates this internally 
to `Dataset2.describe(ds)`. The dot-call syntax is just sugar for "call this function and automatically
pass the object on the left as the first argument".
This is precisely why `self` shows up as a parameter in the method definition but you never
pass it explicitly when calling.
"""



# 6. WHY BOTHER? (the payoff)
"""
Without classes, you'd track a dataset as loose variables:

    dataset_name = "coco"
    dataset_num_samples = 330000
    dataset_name2 = "imagenet"
    dataset_num_samples2 = 1281167

This scales horribly — no natural grouping, easy to mix up which number belongs to which name, 
and no way to attach shared behavior (like `.describe()`) without writing free-floating functions that take
five loose parameters each. Classes give you:

    1. Bundling: data + behavior traveling together, one clean object.
    2. Namespacing: ds.num_samples can never be confused with someone else's num_samples variable.
    3. Reusability:  the SAME blueprint stamps out unlimited objects.
    4. A foundation for everything else in this curriculum (inheritance, polymorphism, etc. all build on this).
"""



if __name__ == "__main__":
    print("\n--- Module 1 demo run ---")
    ds = Dataset2("mnist", 60_000)
    print(ds.describe())
    print("Large dataset?", ds.is_large())

