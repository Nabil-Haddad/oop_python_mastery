# MODULE 02 — SOLUTIONS

class Experiment:
    total_created = 0

    def __init__(self, name):
        self.name = name
        Experiment.total_created += 1



class Trainer:

    def __init__(self, lr , epochs):
        self.lr = lr
        self.epochs = epochs


    @classmethod
    def from_config_dict(cls, config):
        return cls(lr = config["lr"], epochs = config["epochs"])

    @staticmethod
    def clip_lr(lr, max_lr = 1.0):
        return min(lr, max_lr)



class RunLogger:

    def __init__(self):
        self.history = []

    def log(self, msg):
        self.history.append(msg)





if __name__ == "__main__":
    e1 = Experiment("exp_a")
    e2 = Experiment("exp_b")
    e3 = Experiment("exp_c")
    assert Experiment.total_created == 3

    t = Trainer.from_config_dict({"lr": 0.01, "epochs": 5})
    assert t.lr == 0.01
    assert t.epochs == 5

    assert Trainer.clip_lr(2.5) == 1.0
    assert Trainer.clip_lr(0.3) == 0.3


    r1 = RunLogger()
    r2 = RunLogger()
    r1.log("started")
    r2.log("started")
    assert r1.history == ["started"]
    assert r2.history == ["started"]
    assert r1.history is not r2.history

