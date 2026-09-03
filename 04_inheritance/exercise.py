# MODULE 04 — EXERCISES 



# EXERCISE 1: Basic inheritance + super().__init__

# Create base class `Optimizer` with __init__(self, lr) storing self.lr,
# and a method `step(self)` returning "generic step".
# Create subclass `SGD(Optimizer)` with __init__(self, lr, momentum) that
# calls super().__init__(lr), stores self.momentum, and overrides step()
# to return f"SGD step with momentum={self.momentum}".

class Optimizer:
    pass  # replace


class SGD(Optimizer):
    pass  # replace


opt = SGD(lr=0.01, momentum=0.9)
assert opt.lr == 0.01
assert opt.momentum == 0.9
assert opt.step() == "SGD step with momentum=0.9"
assert isinstance(opt, Optimizer)



# EXERCISE 2: Extending a parent method with super()

# Create base class `Callback` with method `on_epoch_end(self, epoch)`
# returning f"epoch {epoch} done".
# Create subclass `PrintingCallback(Callback)` overriding on_epoch_end
# to call the parent version via super() AND append " (printed)" to it.

class Callback:
    pass  # replace


class PrintingCallback(Callback):
    pass  # replace


# cb = PrintingCallback()
# assert cb.on_epoch_end(3) == "epoch 3 done (printed)"



# EXERCISE 3: Mixins / multiple inheritance

# Create two independent mixin classes:
#   `Timestamped` with method `stamp(self)` returning "stamped"
#   `Countable` with method `count(self)` returning "counted"
# Create class `LogEntry(Timestamped, Countable)` with no methods of
# its own -- it should inherit both.

class Timestamped:
    pass  # replace


class Countable:
    pass  # replace


class LogEntry(Timestamped, Countable):
    pass  # replace if needed (may not need any body change)


# entry = LogEntry()
# assert entry.stamp() == "stamped"
# assert entry.count() == "counted"


if __name__ == "__main__":
    print("Exercise 1 checks passed if no AssertionError raised above.")
