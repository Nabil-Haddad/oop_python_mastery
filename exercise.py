# MODULE 02 — EXERCISES




# EXERCISE 1: Class attribute as a shared counter

# Create a class `Experiment` that:
#   - has a CLASS attribute `total_created` starting at 0
#   - in __init__(self, name), stores self.name, and INCREMENTS
#     Experiment.total_created by 1 (access it via the class name,
#     not via self, to avoid the shadowing trap from the lesson)
#
# TODO: implement.


class Experiment:
    pass  # replace


e1 = Experiment("exp_a")
e2 = Experiment("exp_b")
e3 = Experiment("exp_c")
assert Experiment.total_created == 3



# EXERCISE 2: Classmethod as alternative constructor

# Add a classmethod `from_config_dict(cls, config)` to a new class
# `Trainer` that builds a Trainer from a dict like
# {"lr": 0.01, "epochs": 5}. Trainer.__init__ takes (self, lr, epochs).
#
# TODO: implement Trainer.


class Trainer:
    pass  # replace


# t = Trainer.from_config_dict({"lr": 0.01, "epochs": 5})
# assert t.lr == 0.01
# assert t.epochs == 5



# EXERCISE 3: Staticmethod utility

# Add a staticmethod `clip_lr(lr, max_lr=1.0)` to Trainer that returns
# min(lr, max_lr). It should NOT reference self or cls.
#
# TODO: implement inside Trainer above, then uncomment:

# assert Trainer.clip_lr(2.5) == 1.0
# assert Trainer.clip_lr(0.3) == 0.3



# EXERCISE 4: The mutable-default trap

# Below is a buggy class. Fix it so each instance gets its own
# independent `history` list (don't change the class name or method
# names, just fix the bug).

class RunLogger:
    history = []  # BUG

    def log(self, msg):
        self.history.append(msg)


# TODO: fix RunLogger above (this is the actual exercise -- edit it directly)

r1 = RunLogger()
r2 = RunLogger()
r1.log("started")
r2.log("started")
assert r1.history == ["started"]
assert r2.history == ["started"]
assert r1.history is not r2.history


if __name__ == "__main__":
    print("Exercise 1 and 4 checks passed if no AssertionError was raised.")
