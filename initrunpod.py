import os
import sys
import gdown
import logging

# GDrive Test
#GDRIVE_MODEL_DIR = 'https://drive.google.com/drive/folders/1Bkq2VJJP1_yxue5QeinB4_3K_zHVURWW'
#GDRIVE_LORA_DIR =  'https://drive.google.com/drive/folders/1F1CBmGONCFmWi0UV6CyNPMePRDhXiXRV'

# GDrive AI
GDRIVE_LORA_DIR = 'https://drive.google.com/drive/folders/1vCi8_0ieUnKeKMB5VZJSOguUHIiGEOzu'
GDRIVE_MODEL_DIR = 'https://drive.google.com/drive/folders/1AcJXa7tSPRxGa4oXCREOmLvWjkMbvkGZ'

#Local
#LOCAL_MODEL_DIR = 'C:/Users/alexa/OneDrive/Dev/init-runpod/models'
#LOCAL_LORA_DIR = 'C:/Users/alexa/OneDrive/Dev/init-runpod/Lora'

#Runpod.io
LOCAL_MODEL_DIR = '/workspace/stable-diffusion-webui/models'
LOCAL_LORA_DIR = '/workspace/stable-diffusion-webui/models/Lora'

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():

    download_folder_contents(GDRIVE_MODEL_DIR, GDRIVE_LORA_DIR)

def download_folder_contents(model_folder_url, lora_folder_url):
    global LOCAL_MODEL_DIR, LOCAL_LORA_FOLDER

    # Create local folders if they don't exist
    os.makedirs(LOCAL_MODEL_DIR, exist_ok=True)
    os.makedirs(LOCAL_LORA_DIR, exist_ok=True)

    # Download content of "models" folder
    download_folder(model_folder_url, LOCAL_MODEL_DIR)

    # Download content of "lora" folder
    download_folder(lora_folder_url, LOCAL_LORA_DIR)

    logger.info('Download complete.')

def download_folder(folder_url, destination_path):
    logger.info(f'Downloading folder: {folder_url}')
    
    command = f'gdown --folder {folder_url} --output {destination_path}'

    os.system(command)

def download_file(file_id, destination_path):
    file_url = f'https://drive.google.com/uc?id={file_id}'
    output_path = os.path.join(destination_path, file_id)
    gdown.download(file_url, output_path, quiet=False)

if __name__ == '__main__':
    main()
