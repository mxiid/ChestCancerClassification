# ChestCancerClassification


## Workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## Deviations

### 1. `model_training.py`
> In model traning, the model was being compiled with the optimizer which was causing a `Unknown Value Error` in the model. The error was resolved by removing the optimizer from the model compilation. The model was then compiled with the optimizer in the training function.
> I've learned that you have to recompile the model with the optimizer if you're introducing new values to the model. Otherwise, it will return an error.

### 2. `model_evaluation.py`
> In model evaluation, `mlflow.set_tracking_uri(self.config.mlflow_uri)` and `mlflow.set_registry_uri(self.config.mlflow_uri)` are two different functions. You have to set the tracking URI and registry URI separately.
> Also, Windows is so shit that you can't set environment variables using `export` like in `bash` in the terminal. I tried using `SETX` but it didn't work which was causing the issue. Had I set the `tracking_uri` in the terminal, it wouldn't have given me the error...but hey this is windows! `^.^`