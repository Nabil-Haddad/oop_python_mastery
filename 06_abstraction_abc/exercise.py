# MODULE 06 — EXERCISES"""

from abc import ABC, abstractmethod



# EXERCISE 1: Define an abstract base class

# Create abstract class `Retriever(ABC)` with:
#   - abstract method `retrieve(self, query)`
#   - concrete method `name(self)` returning self.__class__.__name__
# Create concrete subclass `DummyRetriever` whose retrieve(query)
# returns [f"doc about {query}"].
#
# TODO: implement both.

class Retriever(ABC):
    pass  # replace


class DummyRetriever(Retriever):
    pass  # replace


# r = DummyRetriever()
# assert r.retrieve("stroke risk") == ["doc about stroke risk"]
# assert r.name() == "DummyRetriever"

# Prove Retriever itself cannot be instantiated:
# try:
#     Retriever()
#     assert False, "should have raised TypeError"
# except TypeError:
#     pass



# EXERCISE 2: Multiple abstract methods

# Create abstract class `Reranker(ABC)` requiring BOTH:
#   - abstract method `score(self, query, doc)` -> float
#   - abstract method `rerank(self, query, docs)` -> sorted list
# Create a concrete subclass `LengthReranker` where:
#   - score(query, doc) returns len(doc) (as a stand-in scoring function)
#   - rerank(query, docs) returns docs sorted by score() descending
#
# TODO: implement both, then create a subclass missing ONE method and
# confirm (in your head, or with a try/except) that it still fails to
# instantiate.

class Reranker(ABC):
    pass  # replace


class LengthReranker(Reranker):
    pass  # replace


# rr = LengthReranker()
# docs = ["short", "a much longer document here"]
# assert rr.rerank("q", docs) == sorted(docs, key=len, reverse=True)


if __name__ == "__main__":
    print("Uncomment assertions above as you implement each class.")
