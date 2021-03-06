import os
from services import image
from flask import Flask
import logging
logger = logging.getLogger('ftpuploader')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif'}
MAX_CONTENT_LENGTH = 1 * 1024 * 1024

image.create_files_directory_variable()

directory = os.environ.get('FILES_DIRECTORY')

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

@app.route('/upload', methods=['POST'])
def upload_file():
    return image.upload_files_type()

@app.route('/files', methods=['GET'])
def list_files():
    return image.get_all_files()

@app.route('/files/<string:type>', methods=['GET'])
def list_files_by_type(type: str):
    return image.get_file_by_format(type)

@app.route("/download/<path:file_name>")
def download_file(file_name):
    return image.download_specific_file(file_name)

@app.route('/download-zip', methods=['GET'])
def download_dir_as_zip():
    return image.donwload_zip_format_files()
 