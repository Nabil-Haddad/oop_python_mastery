# MODULE 10 — EXERCISES



# EXERCISE 1: Write a reusable validating descriptor

# Create a descriptor class `RangeBound` that:
#   - takes `min_value` and `max_value` in __init__
#   - uses __set_name__ to remember the attribute name (store the real
#     value under "_" + name, like the lesson's PositiveNumber)
#   - __set__ raises ValueError if value is outside [min_value, max_value]
#   - __get__ returns the stored value (handle instance is None: return self)
#
# Then use it on a class `SamplingConfig` with:
#   temperature = RangeBound(0.0, 2.0)
#   top_p = RangeBound(0.0, 1.0)

class RangeBound:
    pass  # replace


class SamplingConfig:
    pass  # replace


# cfg = SamplingConfig(temperature=0.7, top_p=0.9)
# assert cfg.temperature == 0.7
# try:
#     cfg.top_p = 1.5
#     assert False, "should have raised"
# except ValueError:
#     pass



# EXERCISE 2: Reuse the SAME descriptor on a second, unrelated class

# Create class `AudioConfig` using RangeBound for `volume` (0.0 to 1.0),
# proving RangeBound truly is reusable across classes without any
# copy-pasted validation logic.

class AudioConfig:
    pass  # replace


# ac = AudioConfig(volume=0.5)
# assert ac.volume == 0.5
# try:
#     ac.volume = 2.0
#     assert False, "should have raised"
# except ValueError:
#     pass


if __name__ == "__main__":
    print("Uncomment assertions above as you implement RangeBound.")
