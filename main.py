# Importing the custom logger we created inside our project
# This helps us track what is happening at each stage
from cnnClassifier import logger

# Importing all the pipeline stages one by one
# Each stage handles a specific responsibility in the ML workflow
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


# =========================
# STAGE 1 — Data Ingestion
# =========================

# Giving a clear name to this stage (just for logging clarity)
STAGE_NAME = "Data Ingestion stage"

try:
   # Logging that this stage has started
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 

   # Creating the object of Data Ingestion pipeline
   # This stage usually downloads data, unzips it, and prepares raw files
   data_ingestion = DataIngestionTrainingPipeline()

   # Calling the main method to execute everything inside this stage
   data_ingestion.main()

   # Logging that this stage has successfully completed
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

# If anything goes wrong, we log the full error details
except Exception as e:
        logger.exception(e)
        raise e



# ===============================
# STAGE 2 — Prepare Base Model
# ===============================

STAGE_NAME = "Prepare base model"

try: 
   # Just adding a visual separator in logs to differentiate stages
   logger.info(f"*******************")

   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

   # This stage prepares the base CNN model (like loading VGG, ResNet, etc.)
   # and modifies the final layers according to our use case
   prepare_base_model = PrepareBaseModelTrainingPipeline()

   # Executing the model preparation logic
   prepare_base_model.main()

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e



# ======================
# STAGE 3 — Training
# ======================

STAGE_NAME = "Training"

try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

   # This stage actually trains the model using the prepared base model
   # and the processed dataset
   model_trainer = ModelTrainingPipeline()

   # Running the training process
   model_trainer.main()

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e



# ==========================
# STAGE 4 — Model Evaluation
# ==========================

STAGE_NAME = "Evaluation stage"

try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

   # Final stage — here we evaluate the trained model
   # This usually includes calculating accuracy, metrics, etc.
   model_evalution = EvaluationPipeline()

   # Executing evaluation
   model_evalution.main()

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e
