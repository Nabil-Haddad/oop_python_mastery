# MODULE 09 — EXERCISES

from dataclasses import dataclass, field



# EXERCISE 1: Basic dataclass

# Create a dataclass `RetrievalResult` with fields:
#   doc_id: str
#   score: float
#   text: str

# TODO: implement.


# result1 = RetrievalResult("doc_1", 0.87, "some text")
# result2 = RetrievalResult("doc_1", 0.87, "some text")
# assert result1 == result2
# assert "doc_1" in repr(result1)



# EXERCISE 2: Defaults and mutable default_factory

# Create a dataclass `QueryLog` with:
#   query: str
#   top_k: int = 5
#   retrieved_ids: list = field(default_factory=list)
# Then prove two separate QueryLog instances don't share the same list.

# TODO: implement.


# log1 = QueryLog("what is hypertension?")
# log2 = QueryLog("what is stroke?")
# log1.retrieved_ids.append("doc_9")
# assert log1.retrieved_ids == ["doc_9"]
# assert log2.retrieved_ids == []
# assert log1.top_k == 5



# EXERCISE 3: frozen dataclass

# Create a frozen dataclass `Citation` with fields source: str, page: int.
# Prove attempting to mutate .page after creation raises an exception.

# TODO: implement.


# c = Citation("nejm_2021", 4)
# try:
#     c.page = 5
#     assert False, "should have raised"
# except Exception:
#     pass


if __name__ == "__main__":
    print("Uncomment assertions above as you implement each dataclass.")
