# MODULE 11 — EXERCISES



# EXERCISE 1: type() basics

# Without using the `class` keyword at all, use type(name, bases, ns)
# to build a class `Bird` with:
#   - a class attribute `can_fly = True`
#   - a method `speak(self)` returning "tweet"
# Assign the result to a variable named Bird.

# TODO: build Bird via type(...) directly.

# b = Bird()
# assert b.can_fly is True
# assert b.speak() == "tweet"



# EXERCISE 2: __init_subclass__ registry

# Create a base class `Component` with a class attribute
# `registry = {}` and __init_subclass__ that registers every subclass
# by name (like the lesson's SimplePlugin). Create two subclasses,
# `EmbedderComponent` and `RerankerComponent`, with no body needed.

class Component:
    pass  # replace


class EmbedderComponent(Component):
    pass  # replace if needed


class RerankerComponent(Component):
    pass  # replace if needed


# assert "EmbedderComponent" in Component.registry
# assert "RerankerComponent" in Component.registry
# assert Component.registry["EmbedderComponent"] is EmbedderComponent


if __name__ == "__main__":
    print("Uncomment assertions above as you implement each exercise.")
