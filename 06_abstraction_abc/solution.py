from abc import ABC, abstractmethod


class Retriever(ABC):
    @abstractmethod
    def retrieve(self, query):
        ...

    def name(self):
        return self.__class__.__name__


class DummyRetriever(Retriever):
    def retrieve(self, query):
        return [f"doc about {query}"]


class Reranker(ABC):
    @abstractmethod
    def score(self, query, doc):
        ...

    @abstractmethod
    def rerank(self, query, docs):
        ...


class LengthReranker(Reranker):
    def score(self, query, doc):
        return len(doc)

    def rerank(self, query, docs):
        return sorted(docs, key=lambda d: self.score(query, d), reverse=True)


if __name__ == "__main__":
    r = DummyRetriever()
    assert r.retrieve("stroke risk") == ["doc about stroke risk"]
    assert r.name() == "DummyRetriever"
    try:
        Retriever()
        assert False
    except TypeError:
        pass

    rr = LengthReranker()
    docs = ["short", "a much longer document here"]
    assert rr.rerank("q", docs) == sorted(docs, key=len, reverse=True)

    print("All Module 6 checks passed.")
