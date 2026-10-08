#MODULE 10 — SOLUTIONS


class RangeBound:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f"{self.private_name} must be within [{self.min_value}, {self.max_value}], got {value}"
            )
        setattr(instance, self.private_name, value)


class SamplingConfig:
    temperature = RangeBound(0.0, 2.0)
    top_p = RangeBound(0.0, 1.0)

    def __init__(self, temperature, top_p):
        self.temperature = temperature
        self.top_p = top_p


class AudioConfig:
    volume = RangeBound(0.0, 1.0)

    def __init__(self, volume):
        self.volume = volume


if __name__ == "__main__":
    cfg = SamplingConfig(temperature=0.7, top_p=0.9)
    assert cfg.temperature == 0.7
    try:
        cfg.top_p = 1.5
        assert False
    except ValueError:
        pass

    ac = AudioConfig(volume=0.5)
    assert ac.volume == 0.5
    try:
        ac.volume = 2.0
        assert False
    except ValueError:
        pass

    print("All Module 10 checks passed.")
