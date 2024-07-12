from ccc.components.model_evaluation import Evaluation
from ccc.config.configuration import ConfigurationManager
from ccc import logger 

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        logger.info(f"EVALUATION COMPLETED. SAVING TO MLFLOW.")
        evaluation.mlflow_log()
        logger.info(f"SAVING TO MLFLOW COMPLETED.")

if __name__ == '__main__':
    try:
        logger.info(f">>> STAGE {STAGE_NAME} STARTED <<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>> STAGE {STAGE_NAME} COMPLETED <<<")
    except:
        logger.error(f">>> STAGE {STAGE_NAME} FAILED <<<")
        raise e
