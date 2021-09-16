import os
import flask
from os.path import isfile, join
from flask import jsonify, request, send_from_directory
from os import listdir
import os.path
from werkzeug.exceptions import NotFound
import tempfile

directory = os.environ.get('FILES_DIRECTORY')

def create_files_directory_variable():
  if not os.path.exists("./uploaded-images"):
    os.mkdir("./uploaded-images")
  if not 'FILES_DIRECTORY' in os.environ:
    os.environ['FILES_DIRECTORY'] = './uploaded-images'

def upload_files_type():
  try:
    f = request.files["file"]
    filename_variable = f.filename
    
    png_file = filename_variable.lower().endswith(('png'))
    jpg_file = filename_variable.lower().endswith(('jpg'))
    gif_file = filename_variable.lower().endswith(('gif'))

    if png_file:
      if os.path.isfile(f'./uploaded-images/PNG/{filename_variable}'):
        return "File already exists", 409
      if os.path.exists('./uploaded-images/PNG'):
        f.save(f"./uploaded-images/PNG/{f.filename}")
        return jsonify(f.filename), 201
      else:
        path = os.path.join(directory, 'PNG')
        os.mkdir(path)
        f.save(f"{directory}/PNG/{f.filename}")
        return jsonify(f.filename), 201

    elif jpg_file:
      if os.path.isfile(f'./uploaded-images/JPG/{filename_variable}'):
        return "File already exists", 409
      if os.path.exists('./uploaded-images/JPG'):
        f.save(f"./uploaded-images/JPG/{f.filename}")
        return jsonify(f.filename), 201
      else:
        path = os.path.join(directory, 'JPG')
        os.mkdir(path) 
        f.save(f"{directory}/JPG/{f.filename}")
        return jsonify(f.filename), 201

    elif gif_file:
      if os.path.isfile(f'./uploaded-images/GIF/{filename_variable}'):
        return "File already exists", 409
      if os.path.exists('./uploaded-images/GIF'):
        f.save(f"./uploaded-images/GIF/{f.filename}")
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
    return "File is bigger than 1MB", 413

def get_all_files():
  list_all_files = []
  def check_png_file_exists():
    if os.path.exists('./uploaded-images/PNG'):
      only_png_files = [f for f in listdir('./uploaded-images/PNG') if isfile(join('./uploaded-images/PNG', f))]
      list_all_files.extend(only_png_files)

  def check_jpg_file_exists():
    if os.path.exists('./uploaded-images/JPG'):
      only_jpg_files = [f for f in listdir('./uploaded-images/JPG') if isfile(join('./uploaded-images/JPG', f))]
      list_all_files.extend(only_jpg_files)

  def check_gif_file_exists():
    if os.path.exists("./uploaded-images/GIF"):
      only_gif_files = [f for f in listdir('./uploaded-images/GIF') if isfile(join('./uploaded-images/GIF', f))]
      list_all_files.extend(only_gif_files)

  check_png_file_exists()
  check_jpg_file_exists()
  check_gif_file_exists()
  return jsonify(list_all_files)

def get_file_by_format(type):
  try:
    incoming_tipo = type.lower()
    if incoming_tipo == 'png' and os.path.exists("./uploaded-images/PNG"):
      only_png_files = [f for f in listdir('./uploaded-images/PNG') if isfile(join('./uploaded-images/PNG', f))]
      return jsonify(only_png_files)
    elif incoming_tipo == 'jpg' and os.path.exists("./uploaded-images/JPG"):
      only_jpg_files = [f for f in listdir('./uploaded-images/JPG') if isfile(join('./uploaded-images/JPG', f))]
      return jsonify(only_jpg_files)
    elif incoming_tipo == 'gif' and os.path.exists("./uploaded-images/GIF"):
      only_gif_files = [f for f in listdir('./uploaded-images/GIF') if isfile(join('./uploaded-images/GIF', f))]
      return jsonify(only_gif_files)
    else:
      return 'No files of that type were found', 404
  except  TypeError:
    return {'msg': 'Mensagem de erro'}, 400
  except FileNotFoundError:
    return {'Files of that format do not exist'}, 400

def download_specific_file(file_name):
  try:
    png_file = file_name.lower().endswith(('png'))
    jpg_file = file_name.lower().endswith(('jpg'))
  
    if png_file:
      return send_from_directory(directory='../uploaded-images/PNG', path=f"{file_name}", as_attachment=True)
    elif jpg_file:
      return send_from_directory(directory='../uploaded-images/JPG', path=f"{file_name}", as_attachment=True)
    else:
      return send_from_directory(directory='../uploaded-images/GIF', path=f"{file_name}", as_attachment=True)
 
  except TypeError:
    return 'That file does not exist', 404
  except NotFound:
    return 'That file was not yet uploaded', 404


def donwload_zip_format_files():
  try:
    type_file = request.args.get('file_type')
    file_name = tempfile.NamedTemporaryFile(mode='w+b', delete=True)
    file_type_uppercase = type_file.upper()
    rate_compression = request.args.get('compression_rate')
    os.system(f'zip -{rate_compression} -r {file_name.name}.zip ./uploaded-images/{file_type_uppercase}')
    os.system(f'mv ./{file_name.name}.zip /tmp')

    return flask.send_file(f'{file_name.name}.zip' , attachment_filename=f'{file_name.name}.zip', as_attachment=True)
  
  except FileNotFoundError:
    return 'File does not exist', 404









