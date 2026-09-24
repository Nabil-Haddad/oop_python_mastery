# MODULE 09 — SOLUTIONS

from dataclasses import dataclass, field


@dataclass
class RetrievalResult:
    doc_id: str
    score: float
    text: str


@dataclass
class QueryLog:
    query: str
    top_k: int = 5
    retrieved_ids: list = field(default_factory=list)


@dataclass(frozen=True)
class Citation:
    source: str
    page: int


if __name__ == "__main__":
    result1 = RetrievalResult("doc_1", 0.87, "some text")
    result2 = RetrievalResult("doc_1", 0.87, "some text")
    assert result1 == result2
    assert "doc_1" in repr(result1)

    log1 = QueryLog("what is hypertension?")
    log2 = QueryLog("what is stroke?")
    log1.retrieved_ids.append("doc_9")
    assert log1.retrieved_ids == ["doc_9"]
    assert log2.retrieved_ids == []
    assert log1.top_k == 5

    c = Citation("nejm_2021", 4)
    try:
        c.page = 5
        assert False
    except Exception:
        pass

    print("All Module 9 checks passed.")
