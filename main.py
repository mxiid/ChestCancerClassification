from ccc import logger
from ccc.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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