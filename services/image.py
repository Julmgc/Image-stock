import os
import flask
from flask import jsonify, request, send_from_directory
from os import listdir
import os.path
from werkzeug.exceptions import NotFound
import tempfile

directory = os.environ.get('FILES_DIRECTORY')

def create_files_directory_variable():
  if not os.path.exists("./uploaded-images"):
    os.mkdir("./uploaded-images")
    os.mkdir("./uploaded-images/PNG")
    os.mkdir("./uploaded-images/JPG")
    os.mkdir("./uploaded-images/GIF")

  if not 'FILES_DIRECTORY' in os.environ:
    os.environ['FILES_DIRECTORY'] = './uploaded-images'

def upload_files_type():
  try:
    f = request.files["file"]
    filename_variable = f.filename

    if filename_variable.lower().endswith(('png')):
      if os.path.isfile(f'./uploaded-images/PNG/{filename_variable}'):
        return "File already exists", 409
      f.save(f"./uploaded-images/PNG/{f.filename}")
      return jsonify(f.filename), 201

    elif filename_variable.lower().endswith(('jpg')):
      if os.path.isfile(f'./uploaded-images/JPG/{filename_variable}'):
        return "File already exists", 409
      f.save(f"./uploaded-images/JPG/{f.filename}")
      return jsonify(f.filename), 201

    elif filename_variable.lower().endswith(('gif')):
      if os.path.isfile(f'./uploaded-images/GIF/{filename_variable}'):
        return "File already exists", 409
      f.save(f"./uploaded-images/GIF/{f.filename}")
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
  only_png_files = [f for f in listdir('./uploaded-images/PNG')]
  list_all_files.extend(only_png_files)
  only_jpg_files = [f for f in listdir('./uploaded-images/JPG')]
  list_all_files.extend(only_jpg_files)
  only_gif_files = [f for f in listdir('./uploaded-images/GIF')]
  list_all_files.extend(only_gif_files)
  return jsonify(list_all_files)

def get_file_by_format(type):
  try:
    file_type_data = [f for f in listdir(f'./uploaded-images/{type.upper()}')]
    if len(file_type_data) > 0:
      return jsonify(file_type_data)
    return 'No files of that type were found', 404
  except  TypeError:
    return {'msg': 'Mensagem de erro'}, 400
  except FileNotFoundError:
    return {'Files of that format do not exist'}, 400

def download_specific_file(file_name):
  try:
    return send_from_directory(directory=f'../uploaded-images/{file_name[-3:].upper()}', path=f"{file_name}", as_attachment=True)
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









