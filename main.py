from ccc import logger
from ccc.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ccc.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from ccc.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from ccc.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>> STAGE {STAGE_NAME} STARTED <<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> STAGE {STAGE_NAME} COMPLETED <<<")

except Exception as e:
    logger.error(f">>> STAGE {STAGE_NAME} FAILED <<<")
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f">>> STAGE {STAGE_NAME} STARTED <<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>> STAGE {STAGE_NAME} COMPLETED <<<")

except Exception as e:
    logger.error(f">>> STAGE {STAGE_NAME} FAILED <<<")
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"

try:
    logger.info(f">>> STAGE {STAGE_NAME} STARTED <<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>> STAGE {STAGE_NAME} COMPLETED <<<")

except Exception as e:
    logger.error(f">>> STAGE {STAGE_NAME} FAILED <<<")
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"

try:
        logger.info(f">>> STAGE {STAGE_NAME} STARTED <<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>> STAGE {STAGE_NAME} COMPLETED <<<")
except Exception as e:
    logger.error(f">>> STAGE {STAGE_NAME} FAILED <<<")
    raise e