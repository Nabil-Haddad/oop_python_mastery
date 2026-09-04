class Optimizer:
    def __init__(self, lr):
        self.lr = lr

    def step(self):
        return "generic step"


class SGD(Optimizer):
    def __init__(self, lr, momentum):
        super().__init__(lr)
        self.momentum = momentum

    def step(self):
        return f"SGD step with momentum={self.momentum}"

class Callback:
    def on_epoch_end(self, epoch):
        return f"epoch {epoch} done"


class PrintingCallback(Callback):
    def on_epoch_end(self, epoch):
        return f"{super().on_epoch_end(epoch)} (printed)"



# Create two independent mixin classes:
#   `Timestamped` with method `stamp(self)` returning "stamped"
#   `Countable` with method `count(self)` returning "counted"
# Create class `LogEntry(Timestamped, Countable)` with no methods of
# its own -- it should inherit both.

class Timestamped:
    def stamp(self):
        return "stamped"


class Countable:
    def count(self):
        return "counted"


class LogEntry(Timestamped, Countable):
    pass 





if __name__ == "__main__":
    opt = SGD(lr=0.01, momentum=0.9)
    assert opt.lr == 0.01 and opt.momentum == 0.9
    assert opt.step() == "SGD step with momentum=0.9"
    assert isinstance(opt, Optimizer)

    cb = PrintingCallback()
    assert cb.on_epoch_end(3) == "epoch 3 done (printed)"

    entry = LogEntry()
    assert entry.stamp() == "stamped"
    assert entry.count() == "counted"

    print("All Module 4 checks passed.")