# MODULE 05 — EXERCISES



# EXERCISE 1: Polymorphism via a shared base class

# Create base class `LossFunction` with method `compute(self, pred, target)`
# raising NotImplementedError.
# Create subclasses `MSE` and `MAE`, each overriding compute():
#   MSE: (pred - target) ** 2
#   MAE: abs(pred - target)
# Then write a function `evaluate(loss_fn, pred, target)` that just
# calls loss_fn.compute(pred, target) -- it must not use isinstance
# or check types at all.

class LossFunction:
    pass  # replace


class MSE(LossFunction):
    pass  # replace


class MAE(LossFunction):
    pass  # replace


def evaluate(loss_fn, pred, target):
    pass  # replace


assert evaluate(MSE(), 5, 2) == 9
assert evaluate(MAE(), 5, 2) == 3



# EXERCISE 2: Pure duck typing (no shared base class)

# Create TWO totally unrelated classes (no inheritance between them,
# no shared base), each with a method `preprocess(self, text)`:
#   `LowercaseCleaner.preprocess` -> text.lower()
#   `StripCleaner.preprocess`     -> text.strip()
# Write a function `run_pipeline(cleaners, text)` that applies each
# cleaner in `cleaners` (a list) to `text` in order, returning the
# final result. It should work with ANY object having .preprocess().

class LowercaseCleaner:
    pass  # replace


class StripCleaner:
    pass  # replace


def run_pipeline(cleaners, text):
    pass  # replace


# result = run_pipeline([StripCleaner(), LowercaseCleaner()], "  HELLO  ")
# assert result == "hello"


if __name__ == "__main__":
    print("Exercise 1 checks passed if no AssertionError raised above.")
