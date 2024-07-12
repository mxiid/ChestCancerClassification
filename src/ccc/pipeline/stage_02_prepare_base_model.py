from ccc.config.configuration import ConfigurationManager
from ccc.components.prepare_base_model import PrepareBaseModel
from ccc import logger

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def _init_(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f">>> STAGE {STAGE_NAME} STARTED <<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>> STAGE {STAGE_NAME} COMPLETED <<<")

    except Exception as e:
        logger.error(f">>> STAGE {STAGE_NAME} FAILED <<<")
        logger.exception(e)
        raise e
