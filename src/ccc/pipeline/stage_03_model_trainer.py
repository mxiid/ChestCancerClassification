from ccc.config.configuration import ConfigurationManager
from ccc.components.model_trainer import Training
from ccc import logger 

STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        trianing_config = config.get_training_config()
        training = Training(config=trianing_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f">>> STAGE {STAGE_NAME} STARTED <<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>> STAGE {STAGE_NAME} COMPLETED <<<")

    except Exception as e:
        logger.error(f">>> STAGE {STAGE_NAME} FAILED <<<")
        logger.exception(e)
        raise e