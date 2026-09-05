# MODULE 05 — POLYMORPHISM & DUCK TYPING

"""
"Polymorphism" = "many forms". The same method call
(`obj.forward(x)`, `obj.fit(X, y)`) behaves differently depending on
WHICH concrete object it's called on, without the calling code needing
to know or care exactly which subclass it's dealing with.
"""

# 1. POLYMORPHISM VIA INHERITANCE (the classic case)
class Layer:
    def forward(self, x):
        raise NotImplementedError


class ReLU(Layer):
    def forward(self, x):
        return max(0, x)


class Sigmoid(Layer):
    def forward(self, x):
        return 1 / (1 + 2.718281828 ** -x)


class Identity(Layer):
    def forward(self, x):
        return x


def run_layer(layer, x):
    # This function has NO idea which concrete Layer it received.
    # It just trusts that ANY Layer has a .forward() method that works.
    return layer.forward(x)


for layer in [ReLU(), Sigmoid(), Identity()]:
    print(type(layer).__name__, "->", run_layer(layer, -2))

"""
This is the entire point of an nn.Module-style `.forward()` convention: a training loop can call 
`.forward(x)` (or in real PyTorch, just `layer(x)`, via __call__) on ANY layer object, completely uniformly,
regardless of what that layer actually does internally. 
Add a new layer type tomorrow, and the training loop doesn't change ONE line.
"""
# 2. DUCK TYPING -- "IF IT WALKS LIKE A DUCK..."

"""
Python takes polymorphism further than languages with strict typing. You DON'T need a shared base class
at all. If an object simply HAS the right method with the right signature, Python is happy to call it.
This is "duck typing": "If it walks like a duck and quacks like a duck, treat it as a duck", Python cares
about BEHAVIOR, not declared type.
"""


class ScikitLikeModel:
    def fit(self, X, y):
        return f"fit on {len(X)} samples (sklearn-style)"


class MyCustomModel:
    def fit(self, X, y):
        return f"custom training loop on {len(X)} samples"


def train_any_model(model, X, y):
    # No shared base class required whatsoever. This function only cares that `model` has a `.fit(X, y)`
    return model.fit(X, y)


print(train_any_model(ScikitLikeModel(), [1, 2, 3], [0, 1, 0]))
print(train_any_model(MyCustomModel(), [1, 2, 3], [0, 1, 0]))


# 3. WHY THIS MATTERS: OPEN/CLOSED DESIGN

"""
Contrast this bad pattern:
"""


def run_layer_BAD(layer, x):
    if isinstance(layer, ReLU):
        return max(0, x)
    elif isinstance(layer, Sigmoid):
        return 1 / (1 + 2.718281828 ** -x)
    elif isinstance(layer, Identity):
        return x
    else:
        raise TypeError("unknown layer type")


"""
This function must be EDITED every single time a new layer type is added -- a maintenance nightmare,
and a violation of what's called the "Open/Closed Principle" (Module 12): code should be OPEN to extension
(new layer types) but CLOSED to modification (you shouldn't have to touch run_layer_BAD's body ever again).
Polymorphism is exactly how you satisfy that principle: each class knows how to handle itself, and
calling code just trusts the shared interface.
"""

# 4. OPERATOR POLYMORPHISM
"""
Even Python's own `+` operator is polymorphic: `1 + 2` and `"a" + "b"` and `[1] + [2]` all use the SAME `+` 
syntax but each type defines its own meaning for it (via a dunder method, `__add__`.
"""

if __name__ == "__main__":
    print("\n--- Module 5 demo ---")
    for layer in [ReLU(), Sigmoid(), Identity()]:
        print(run_layer(layer, 3))
