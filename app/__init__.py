from flask import Flask, jsonify, request, send_from_directory, render_template
from werkzeug.exceptions import NotFound
from werkzeug.utils import secure_filename
import os
from os import listdir
from os.path import isfile, join
from dotenv import get_key
from kenzie import create_files_directory_variable
import logging
logger = logging.getLogger('ftpuploader')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif'}
MAX_CONTENT_LENGTH = 1 * 1024 * 1024


create_files_directory_variable()


# directory = get_key('./.env', 'FILES_DIRECTORY')
directory = os.environ.get('FILES_DIRECTORY')

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

@app.route('/upload', methods=['POST'])
def upload_file():
 

  try:
    f = request.files["file"]
    filename_variable = f.filename
   
    png_file = filename_variable.lower().endswith(('png'))
    jpg_file = filename_variable.lower().endswith(('jpg'))
    gif_file = filename_variable.lower().endswith(('gif'))
    if png_file:
      path = './image/PNG'
      if_it_exists = os.path.exists(path)
      if if_it_exists:
        f.save(f"./image/PNG/{f.filename}")
        return jsonify(f.filename), 201
      else:
        path = os.path.join(directory, 'PNG')
        os.mkdir(path)
        f.save(f"{directory}/PNG/{f.filename}")
        return jsonify(f.filename), 201
    elif jpg_file:
      path = './image/JPG'
      if_it_exists = os.path.exists(path)
      if if_it_exists:
          
        f.save(f".image/JPG/{f.filename}")
        return jsonify(f.filename), 201
      else:
        path = os.path.join(directory, 'JPG')
        os.mkdir(path) 
        f.save(f"{directory}/JPG/{f.filename}")
        return jsonify(f.filename), 201
    elif gif_file:
      path = './image/GIF'
      if_it_exists = os.path.exists(path)
      if if_it_exists:
           
        f.save(f".image/GIF/{f.filename}")
        return jsonify(f.filename), 201
      else:
        path = os.path.join(directory, 'GIF')
        os.mkdir(path) 
        f.save(f"{directory}/GIF/{f.filename}")
        return jsonify(f.filename), 201
    
    else:
      return "File format not aloud", 415
  except KeyError as e:   
    return {'msg': str(e)}, 500      
  except FileNotFoundError:
    return "File already exists", 409
  except TypeError:
    return "File format not aloud", 415
 


@app.route('/files', methods=['GET'])
def list_files():
  list_all_files = []
  def check_png_file_exists():
    path = './image/PNG'
    if_it_exists = os.path.exists(path)
    if if_it_exists:
      only_png_files = [f for f in listdir('./image/PNG') if isfile(join('./image/PNG', f))]
      list_all_files.extend(only_png_files)
  def check_jpg_file_exists():
    path = './image/JPG'
    if_it_exists = os.path.exists(path)
    if if_it_exists:
      only_jpg_files = [f for f in listdir('./image/JPG') if isfile(join('./image/JPG', f))]
      list_all_files.extend(only_jpg_files)
  def check_gif_file_exists():
    path = "./image/GIF"
    if_it_exists = os.path.exists(path)
    if if_it_exists:
      only_gif_files = [f for f in listdir('./image/GIF') if isfile(join('./image/GIF', f))]
      list_all_files.extend(only_gif_files)
  check_png_file_exists()
  check_jpg_file_exists()
  check_gif_file_exists()
  return jsonify(list_all_files)



@app.route('/files/<string:tipo>', methods=['GET'])
def list_files_by_tipo(tipo: str):
  path = "./image/GIF"
  if_it_exists = os.path.exists(path)
  check_png = "./image/PNG"
  if_png = os.path.exists(check_png)
  check_jpg = "./image/JPG"
  if_jpg_exists = os.path.exists(check_jpg)
  try:
    incoming_tipo = tipo.lower()
    
    if incoming_tipo == 'png' and if_png:
      only_png_files = [f for f in listdir('./image/PNG') if isfile(join('./image/PNG', f))]
      return jsonify(only_png_files)
 
    elif incoming_tipo == 'jpg' and if_jpg_exists:
      only_jpg_files = [f for f in listdir('./image/JPG') if isfile(join('./image/JPG', f))]
      return jsonify(only_jpg_files)
    
    elif incoming_tipo == 'gif' and if_it_exists:

      only_gif_files = [f for f in listdir('./image/GIF') if isfile(join('./image/GIF', f))]
      return jsonify(only_gif_files)
    else:
      return 'No files of that type were found', 404
  except  TypeError:
    return {'msg': 'Mensagem de erro'}, 400
  except FileNotFoundError:
    return {'Files of that format do not exist'}, 400



@app.route("/download/<path:name>")
def download_file(name):
  try:
    png_file = name.lower().endswith(('png'))
    jpg_file = name.lower().endswith(('jpg'))
    gif_file = name.lower().endswith(('gif'))
    if png_file:
      return send_from_directory(directory='../image/PNG', path=f"{name}", as_attachment=True)
    elif jpg_file:
      return send_from_directory(directory='../image/JPG', path=f"{name}", as_attachment=True)
    else:
      return send_from_directory(directory='../image/GIF', path=f"{name}", as_attachment=True)
 
  except TypeError:
    return 'That file does not exist', 404
  except NotFound:
    return 'That file does not exist', 404


@app.route('/download-zip', methods=['GET'])
def download_dir_as_zip():
  ...
 