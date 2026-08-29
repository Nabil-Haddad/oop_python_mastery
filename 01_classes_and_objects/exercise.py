# MODULE 01 — EXERCISES

# EXERCISE 1: Build a class from scratch

# Create a class `ModelConfig` representing a minimal ML model config.
# It must have an __init__ that accepts:
#   - model_name (str)
#   - learning_rate (float)
#   - batch_size (int)
# and stores each as an instance attribute of the SAME name.
#
# TODO: define the class here.


class ModelConfig:
    pass  # replace with your implementation


cfg = ModelConfig("resnet50", 0.001, 32)
assert cfg.model_name == "resnet50"
assert cfg.learning_rate == 0.001
assert cfg.batch_size == 32



# EXERCISE 2: Two independent objects

# Create a second ModelConfig with different values and prove that
# changing one object's attribute does NOT affect the other.

cfg2 = ModelConfig("vit-base", 0.0003, 64)

# TODO: mutate cfg's batch_size to 128 (one line)

assert cfg.batch_size == 128
assert cfg2.batch_size == 64  # must be unaffected



# EXERCISE 3: Add a method

# Add a method `summary(self)` to ModelConfig (edit the class above)
# that returns a string formatted EXACTLY like:
#   "resnet50 | lr=0.001 | batch=32"
# (model_name | lr=<learning_rate> | batch=<batch_size>)
#
# TODO: implement summary() inside the ModelConfig class above, then
# uncomment the assertions below.

# fresh_cfg = ModelConfig("resnet50", 0.001, 32)
# assert fresh_cfg.summary() == "resnet50 | lr=0.001 | batch=32"



# EXERCISE 4: A second, unrelated class

# Create a class `TrainingRun` with __init__(self, config, epochs) that
# stores both as instance attributes, plus a method
# `total_steps(self, steps_per_epoch)` returning epochs * steps_per_epoch.
#
# TODO: define the class here.


class TrainingRun:
    pass  # replace with your implementation


# run = TrainingRun(cfg, epochs=10)
# assert run.epochs == 10
# assert run.config is cfg          # note: `is`, not `==` — same object!
# assert run.total_steps(500) == 5000


if __name__ == "__main__":
    print("All exercises attempted. Uncomment asserts as you complete each part.")
    print("If this prints with no AssertionError above, Exercise 1-2 are solid.")
