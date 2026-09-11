# MODULE 08 — COMPOSITION vs INHERITANCE

"""
Inheritance (Module 04) models "IS-A" relationships: a Conv2D IS-A Layer.
Composition models "HAS-A" relationships: a Trainer HAS-A Model,
HAS-A Optimizer, HAS-A DataLoader. Composition means building a class
out of OTHER OBJECTS as attributes, rather than inheriting their code.
"""

# 1. THE PROBLEM: MISUSING INHERITANCE FOR "HAS-A"

class Model:
    def predict(self, x):
        return f"prediction for {x}"


# BAD: Trainer is NOT a kind of Model. It just NEEDS one to do its job.
class BadTrainer(Model):
    def train(self):
        return "training..."


bt = BadTrainer()
print(bt.predict("x"))  # works, but semantically nonsensical
                        # "a Trainer IS a Model"?? No.

"""
This "works" mechanically, but it's a lie about what a Trainer IS. It
also drags along everything Model does (and will do in the future)
whether Trainer wants it or not, and locks you into exactly ONE model
implementation forever.

"""


# 2. THE FIX: COMPOSITION

class GoodTrainer:
    def __init__(self, model, optimizer):
        # Trainer HOLDS references to a model and optimizer.
        # It does not pretend to BE either of them.
        self.model = model
        self.optimizer = optimizer

    def train_step(self, x):
        pred = self.model.predict(x)         # delegate to the model
        update = self.optimizer.step()        # delegate to the optimizer
        return f"{pred}, then {update}"


class SGD:
    def step(self):
        return "SGD updated weights"


trainer = GoodTrainer(model=Model(), optimizer=SGD())
print(trainer.train_step("batch_1"))

"""
Now GoodTrainer can work with ANY object that has a .predict() method
and ANY object with a .step() method (duck typing, Module 05) --
swap in a completely different Model or Optimizer subclass tomorrow,
and Trainer's code doesn't change at all.
"""

# 3. "FAVOR COMPOSITION OVER INHERITANCE"


"""

This is one of the most repeated pieces of OOP wisdom, and for good
reason. Composition tends to be more FLEXIBLE than inheritance:

  - Inheritance relationships are fixed at class-definition time and
    apply forever to every instance.
  - Composition relationships can be swapped at RUNTIME
    (`trainer.model = some_other_model`) and configured per-instance.
  - Deep inheritance chains (A -> B -> C -> D) get fragile: changing a
    method way up in A can have surprising ripple effects on D.
    Composition keeps components more independent and easier to test
    in isolation.

Rule of thumb: reach for inheritance ONLY when the "IS-A" relationship
is genuinely, unambiguously true AND you want to inherit real shared
behavior (like ReLU IS-A Layer with a shared describe() method).
Reach for composition for everything else -- which, in real systems,
is most things.

"""

# 4. A REALISTIC RAG-PIPELINE EXAMPLE (composition in action)


class Retriever:
    def retrieve(self, query):
        return [f"doc1 about {query}", f"doc2 about {query}"]


class Generator:
    def generate(self, query, docs):
        return f"answer to '{query}' using {len(docs)} docs"


class RAGPipeline:
    # RAGPipeline HAS-A retriever and HAS-A generator.
    # It is not "a kind of" either -- it coordinates both.
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def answer(self, query):
        docs = self.retriever.retrieve(query)
        return self.generator.generate(query, docs)


pipeline = RAGPipeline(Retriever(), Generator())
print(pipeline.answer("stroke risk factors"))

"""
This is exactly the shape of a real RAG system:
swap Retriever for a HybridRetriever (dense+sparse), swap Generator
for a different LLM wrapper, all WITHOUT touching RAGPipeline itself
-- because RAGPipeline only depends on the SHAPE of the interface
(.retrieve(), .generate()), not on any specific class.
"""

if __name__ == "__main__":
    print("\n--- Module 8 demo ---")
    print(pipeline.answer("hypertension"))
