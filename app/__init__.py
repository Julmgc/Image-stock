from flask import Flask, jsonify, request, send_from_directory, render_template
from werkzeug.exceptions import NotFound
from werkzeug.utils import secure_filename
import os
import glob
from os import listdir
from os.path import isfile, join

from dotenv import get_key
from kenzie import image
from zipfile import Path, ZipFile
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


@app.route('/files/<string:tipo>', methods=['GET'])
def list_files_by_tipo(tipo: str):
  return image.get_file_by_format(tipo)


@app.route("/download/<path:name>")
def download_file(name):
  return image.download_specific_file(name)


@app.route('/download-zip', methods=['GET'])
def download_dir_as_zip():
  try:
    file_type = request.args.get('file_type')
    file_type_uppercase = file_type.upper()
    compression_rate = request.args.get('compression_rate')
    list_files_type = []
    directory =  f'./images-used/{file_type_uppercase}'
    for filename in os.listdir(directory):
      f = os.path.join(directory, filename)
      if os.path.isfile(f):
        list_files_type.append(f)
    zipObj = ZipFile('jpg.zip', 'w')
    for file in list_files_type:
      zipObj.write(file)
    zipObj.close()
    return 'it worked'
  except Exception as e:
    return str(e)
 