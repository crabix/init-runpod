import os
import sys
import gdown

# Global variables
#DEFAULT_FOLDER_URL = 'https://drive.google.com/drive/folders/your_folder_id'
DEFAULT_FOLDER_URL = 'https://drive.google.com/drive/folders/1yQndn6L5i84PiBE8czeuPeSMULci7i5Q'

#DEFAULT_DESTINATION_PATH = 'path/to/save/files/'
DEFAULT_DESTINATION_PATH = 'C:/Users/alexa/OneDrive/Dev/init-runpod'
#DEFAULT_DESTINATION_PATH = '.'

def main():
    folder_url, destination_path = parse_command_line_args()

    folder_id = extract_folder_id(folder_url)
    download_folder_contents(folder_id, destination_path)

def parse_command_line_args():
    if len(sys.argv) >= 3:
        folder_url = sys.argv[1]
        destination_path = sys.argv[2]
    else:
        folder_url = DEFAULT_FOLDER_URL
        destination_path = DEFAULT_DESTINATION_PATH

    return folder_url, destination_path

def extract_folder_id(folder_url):
    parts = folder_url.split('/')
    return parts[-1]

def download_folder_contents(folder_id, destination_path):
    folder_url = f'https://drive.google.com/drive/folders/{folder_id}'
    command = f'gdown --folder {folder_url} --output {destination_path}'

    os.system(command)

    print('Download complete.')

if __name__ == '__main__':
    main()