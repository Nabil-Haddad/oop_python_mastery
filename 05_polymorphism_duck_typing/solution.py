class LossFunction:
    def compute(self, pred, target):
        raise NotImplementedError("")


class MSE(LossFunction):
    def compute(self, pred, target):
        return (pred - target) ** 2


class MAE(LossFunction):
    def compute(self, pred, target):
        return abs(pred - target)


def evaluate(loss_fn, pred, target):
    return loss_fn.compute(pred, target)


class LowercaseCleaner:
    def preprocess(self, text):
        return text.lower()


class StripCleaner:
    def preprocess(self, text):
        return text.strip()


def run_pipeline(cleaners, text):
    clean = text
    for cleaner in cleaners:
        clean = cleaner.preprocess(clean)

    return clean



if __name__ == "__main__":
    assert evaluate(MSE(), 5, 2) == 9
    assert evaluate(MAE(), 5, 2) == 3


    result = run_pipeline([StripCleaner(), LowercaseCleaner()], "  HELLO  ")
    assert result == "hello"
        


