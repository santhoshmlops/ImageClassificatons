from cnnClassifier.pipeline.train_pipeline import DataIngestionTrainingPipeline
from cnnClassifier.logger import logging
from cnnClassifier.exception import CustomException
import os,sys

try:
    logging.info("Data Ingestion Started")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logging.info("Data Ingestion completed")
except Exception as e:
    raise CustomException(e,sys)
