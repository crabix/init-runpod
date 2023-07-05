import logging
import csv
import requests
import os
from tqdm.auto import tqdm

ODEL_DIR = 'https://drive.google.com/drive/folders/1AcJXa7tSPRxGa4oXCREOmLvWjkMbvkGZ'

#Local
#CSV_FILE = 'C:/Users/alexa/OneDrive/Dev/init-runpod/civitai.csv'
#LOCAL_MODEL_DIR = 'C:/Users/alexa/OneDrive/Dev/init-runpod/models'
#LOCAL_LORA_DIR = 'C:/Users/alexa/OneDrive/Dev/init-runpod/Lora'



#Runpod.io
CSV_FILE = 'civitai.csv'
LOCAL_MODEL_DIR = '/workspace/stable-diffusion-webui/models' #models
LOCAL_LORA_DIR = '/workspace/stable-diffusion-webui/models/Lora' #loras
LOCAL_EMBEDDINGS_DIR = '/workspace/stable-diffusion-webui/embeddings' #embeddings

logging.basicConfig(level=logging.ERROR)

def download(url: str, fname: str, chunk_size=1024):
    try:
        resp = requests.get(url, stream=True)
        total = int(resp.headers.get('content-length', 0))
        with open(fname, 'wb') as file, tqdm(
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            position=0,
            leave=True,
        ) as bar:
            for data in resp.iter_content(chunk_size=chunk_size):
                size = file.write(data)
                bar.update(size)
    except requests.exceptions.RequestException as e:
        logging.exception(f"Error occurred while downloading file from {url}: {e}")
    except OSError as e:
        logging.exception(f"Error occurred while writing file {fname}: {e}")

def download_files_from_csv(file_path):
    logging.exception('path'+str(file_path))
    try:
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            num_lines = sum(1 for line in csv_reader)
            csv_file.seek(0)
            for row in tqdm(csv_reader,total=num_lines, position=0,desc='Total',leave=True):
                file_type = row[0]
                name = row[1]
                url = row[2]
                if file_type == "Lora":
                    directory = LOCAL_LORA_DIR
                if file_type == "Embedding":
                    directory = LOCAL_EMBEDDINGS_DIR
                else:
                    directory = LOCAL_MODEL_DIR
                if not os.path.exists(directory):
                    os.makedirs(directory)
                extension = ".safetensors"
                file_name = os.path.join(directory, name+extension)
                #download_file(url, file_name)
                download(url, file_name)
    except FileNotFoundError as e:
        logging.exception(f"CSV file not found: {e}")
    except Exception as e:
        logging.exception(f"Error occurred while downloading files from CSV: {e}")

def main():
    download_files_from_csv(CSV_FILE)

if __name__ == "__main__":
    main()
