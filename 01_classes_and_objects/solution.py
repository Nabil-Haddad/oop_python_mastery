class ModelConfig:
    def __init__(self,model_name: str, learning_rate: float, batch_size: int ):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.batch_size = batch_size

    def summary(self)->str:
        return f"{self.model_name} | lr={self.learning_rate} | batch={self.batch_size}"


class TrainingRun:
    def __init__(self,config, epochs):
        self.config = config
        self.epochs = epochs

    def total_steps(self, steps_per_epoch):
        return self.epochs * steps_per_epoch




if __name__ == "__main__":
    cfg = ModelConfig("resnet50", 0.001, 32)
    cfg2 = ModelConfig("vit-base", 0.0003, 64)
    
    assert cfg.model_name == "resnet50"
    assert cfg.learning_rate == 0.001
    assert cfg.batch_size == 32

    cfg.batch_size = 128
    assert cfg.batch_size == 128
    assert cfg2.batch_size == 64 

    fresh_cfg = ModelConfig("resnet50", 0.001, 32)
    assert fresh_cfg.summary() == "resnet50 | lr=0.001 | batch=32"

    run = TrainingRun(cfg, epochs=10)
    assert run.epochs == 10
    assert run.config is cfg         
    assert run.total_steps(500) == 5000