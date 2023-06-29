import logging
import csv
import requests
import os


# GDrive AI
GDRIVE_LORA_DIR = 'https://drive.google.com/drive/folders/1vCi8_0ieUnKeKMB5VZJSOguUHIiGEOzu'
GDRIVE_MODEL_DIR = 'https://drive.google.com/drive/folders/1AcJXa7tSPRxGa4oXCREOmLvWjkMbvkGZ'

#Local
CSV_FILE = 'C:/Users/alexa/OneDrive/Dev/init-runpod/civitai.csv'
LOCAL_MODEL_DIR = 'C:/Users/alexa/OneDrive/Dev/init-runpod/models'
LOCAL_LORA_DIR = 'C:/Users/alexa/OneDrive/Dev/init-runpod/Lora'

#Runpod.io
#LOCAL_MODEL_DIR = '/workspace/stable-diffusion-webui/models'
#LOCAL_LORA_DIR = '/workspace/stable-diffusion-webui/models/Lora'

logging.basicConfig(filename="download.log", level=logging.DEBUG)

def download_file(url, file_name):
    try:
        with open(file_name, "wb") as file:
            response = requests.get(url)
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        logging.exception(f"Error occurred while downloading file from {url}: {e}")
    except OSError as e:
        logging.exception(f"Error occurred while writing file {file_name}: {e}")

def download_files_from_csv(file_path):
    logging.exception('path'+str(file_path))
    try:
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                file_type = row[0]
                name = row[1]
                url = row[2]
                if file_type == "Lora":
                    directory = LOCAL_LORA_DIR
                else:
                    directory = LOCAL_MODEL_DIR
                if not os.path.exists(directory):
                    os.makedirs(directory)
                extension = ".safetensor"
                file_name = os.path.join(directory, name+extension)
                download_file(url, file_name)
    except FileNotFoundError as e:
        logging.exception(f"CSV file not found: {e}")
    except Exception as e:
        logging.exception(f"Error occurred while downloading files from CSV: {e}")

def main():
    download_files_from_csv(CSV_FILE)

if __name__ == "__main__":
    main()
