# MODULE 11 — METACLASSES

"""
Fair warning up front: metaclasses are the single most "advanced" topic
in this curriculum, and in real production code you will use them
RARELY. The goal here isn't for you to start writing metaclasses every
week , it's for you to understand what's going on when you encounter
them in library internals (they show up in some ORM libraries, in
certain plugin/registry systems, and occasionally in ML framework
internals), so they don't feel like impenetrable magic.


1. "CLASSES ARE OBJECTS TOO"

Everything in Python is an object , including classes themselves. If
a class is an object, then that object must have been CREATED by
something. That "something" is called a METACLASS. The default
metaclass for every class you've written so far, whether you knew it
or not, is `type`.
"""


class Dog:
    pass


print(type(Dog))          # <class 'type'>   -- Dog's "class" is `type`
print(type(Dog()))         # <class '__main__.Dog'>  -- an instance's class is Dog
print(isinstance(Dog, type))  # True

"""
So the relationship chain is:
    an instance  -> is created by ->  its class
    a class -> is created by ->  its metaclass (usually `type`)

Just like a class is a blueprint for instances, a METACLASS is a
blueprint for CLASSES. `type` itself is the default metaclass that
knows how to build ordinary classes.

"""
# 2. `type()` CAN CREATE CLASSES DIRECTLY, WITHOUT THE `class` KEYWORD


"""
This makes the mechanism concrete: the `class` keyword is really just
convenient syntax sugar for calling `type(name, bases, namespace)`.
"""

Cat = type(
    "Cat",                                    # class name
    (object,),                                 # base classes (a tuple)
    {"sound": "meow", "speak": lambda self: self.sound},  # namespace (methods/attrs)
)

c = Cat()
print(c.speak())   # meow
print(type(Cat))    # <class 'type'>

"""
`class Cat: ...` and the `type(...)` call above produce equivalent
classes. Python's `class` statement is doing exactly this under the
hood: gathering up the name, base classes, and body into a namespace
dict, then calling the metaclass (by default, `type`) to build the
actual class object.


3. WRITING A CUSTOM METACLASS

A custom metaclass lets you hook into CLASS CREATION itself -- run
code every time a NEW CLASS (not instance) is defined. You do this by
subclassing `type` and overriding `__new__` or `__init__`.
"""


class RegisteringMeta(type):
    registry = {}  # shared across every class using this metaclass

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if name != "Plugin":  # don't register the base class itself
            RegisteringMeta.registry[name] = cls
        return cls


class Plugin(metaclass=RegisteringMeta):
    pass


class RetrieverPlugin(Plugin):
    pass


class GeneratorPlugin(Plugin):
    pass


print(RegisteringMeta.registry)
# {'RetrieverPlugin': <class '...'>, 'GeneratorPlugin': <class '...'>}

"""
Notice: we never had to manually call
`RegisteringMeta.registry["RetrieverPlugin"] = RetrieverPlugin`
anywhere. The metaclass automatically registered EVERY subclass the
moment it was DEFINED, just by virtue of inheriting from Plugin. This
"auto-registering plugin system" is one of the few genuinely common
real-world uses of metaclasses.

"""
# 4. WHY YOU RARELY NEED THIS: __init_subclass__ IS OFTEN ENOUGH
"""
For MANY use cases people reach for metaclasses (like the registry
example above), Python offers a simpler hook: `__init_subclass__`,
defined directly on a normal base class, no metaclass required.
"""


class SimplePlugin:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        SimplePlugin.registry[cls.__name__] = cls


class Retriever(SimplePlugin):
    pass


class Generator(SimplePlugin):
    pass


print(SimplePlugin.registry)
# {'Retriever': <class '...'>, 'Generator': <class '...'>}

"""
Same registry behavior, ZERO metaclass ceremony. `__init_subclass__`
covers the vast majority of "I want to hook into subclass creation"
needs. Reach for a full custom metaclass only when you need to control
things __init_subclass__ genuinely can't reach (e.g. altering the
namespace dict itself before the class is built, or needing multiple
independent, swappable class-creation behaviors).

"""
# 5. TAKEAWAY
"""
You will most likely never WRITE a metaclass in typical AI-engineering
work. But now, when you see `metaclass=ABCMeta` (that's literally how
Module 06's `abc.ABC` enforces abstract methods internally!) or
encounter one in a library's source code, you'll recognize exactly
what's happening: it's a class that controls how OTHER classes get built.
"""

if __name__ == "__main__":
    print("\n--- Module 11 demo ---")
    print(SimplePlugin.registry)
