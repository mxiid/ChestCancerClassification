import os
import zipfile
import gdown
from pathlib import Path
from ccc import logger
from ccc.utils.common import get_size
from ccc.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self)->str:
        '''Fetch data from the URL'''

        try:
            if os.path.exists(self.config.local_data_file):
                path_to_file = Path(self.config.local_data_file)
                path_size = get_size(path_to_file)
                logger.info(f"Data already exists at {path_to_file} with size {path_size}. Skipping download.")
            else:
                dataset_url=self.config.source_URL
                zip_download_dir=self.config.local_data_file
                os.makedirs("artifacts/data_ingestion", exist_ok=True)
                logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

                file_id = dataset_url.split("/")[-2]
                prefix = "https://drive.google.com/uc?/export=downloadU&id="
                gdown.download(prefix+file_id, zip_download_dir)

                logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e

    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        '''

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)