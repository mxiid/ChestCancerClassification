import os
from pathlib import Path
import tensorflow as tf
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from ccc.entity.config_entity import EvaluationConfig
from ccc.utils.common import save_json
from ccc import logger 
from ccc.constants import MLFLOW_TRACKING_USERNAME, MLFLOW_TRACKING_PASSWORD


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):

        datagenerator_kwargs = dict(rescale=1.0 / 255, validation_split=0.30)

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def mlflow_log(self):
        os.environ["MLFLOW_TRACKING_USERNAME"] = MLFLOW_TRACKING_USERNAME
        os.environ["MLFLOW_TRACKING_PASSWORD"] = MLFLOW_TRACKING_PASSWORD
        logger.info("Starting MLflow logging")
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_registry_uri(self.config.mlflow_uri)
        logger.info(f"MLflow registry URI set to: {self.config.mlflow_uri}")
        
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        logger.info(f"Tracking URL type: {tracking_url_type_store}")

        try:
            with mlflow.start_run():
                logger.info("MLflow run started")
                
                logger.info("Logging parameters")
                mlflow.log_params(self.config.all_params)
                
                logger.info("Logging metrics")
                mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})

                logger.info("Logging model")
                if tracking_url_type_store != "file":
                    mlflow.keras.log_model(
                        self.model, "model", registered_model_name="VGG16Model"
                    )
                else:
                    mlflow.keras.log_model(self.model, "model")
                
                logger.info("MLflow logging completed successfully")
        except Exception as e:
            logger.error(f"Error during MLflow logging: {str(e)}")
            raise
