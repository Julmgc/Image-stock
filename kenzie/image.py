import os
from os.path import isfile, join
from flask import jsonify, request, send_from_directory
from os import listdir
from werkzeug.exceptions import NotFound
directory = os.environ.get('FILES_DIRECTORY')

def create_files_directory_variable():
  if 'FILES_DIRECTORY' in os.environ:
    pass
  else:
    os.environ['FILES_DIRECTORY'] = './images-used'



def upload_files_type():
  try:
    f = request.files["file"]
    filename_variable = f.filename
   
    png_file = filename_variable.lower().endswith(('png'))
    jpg_file = filename_variable.lower().endswith(('jpg'))
    gif_file = filename_variable.lower().endswith(('gif'))
    if png_file:
      path = './images-used/PNG'
      if_it_exists = os.path.exists(path)
      if if_it_exists:
        f.save(f"./images-used/PNG/{f.filename}")
        return jsonify(f.filename), 201
      else:
        path = os.path.join(directory, 'PNG')
        os.mkdir(path)
        f.save(f"{directory}/PNG/{f.filename}")
        return jsonify(f.filename), 201
    elif jpg_file:
      path = './images-used/JPG'
      if_it_exists = os.path.exists(path)
      if if_it_exists:
          
        f.save(f"./images-used/JPG/{f.filename}")
        return jsonify(f.filename), 201
      else:
        path = os.path.join(directory, 'JPG')
        os.mkdir(path) 
        f.save(f"{directory}/JPG/{f.filename}")
        return jsonify(f.filename), 201
    elif gif_file:
      path = './images-used/GIF'
      if_it_exists = os.path.exists(path)
      if if_it_exists:
           
        f.save(f"./images-used/GIF/{f.filename}")
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

def get_all_files():
  list_all_files = []
  def check_png_file_exists():
    path = './images-used/PNG'
    if_it_exists = os.path.exists(path)
    if if_it_exists:
      only_png_files = [f for f in listdir('./images-used/PNG') if isfile(join('./images-used/PNG', f))]
      list_all_files.extend(only_png_files)
  def check_jpg_file_exists():
    path = './images-used/JPG'
    if_it_exists = os.path.exists(path)
    if if_it_exists:
      only_jpg_files = [f for f in listdir('./images-used/JPG') if isfile(join('./images-used/JPG', f))]
      list_all_files.extend(only_jpg_files)
  def check_gif_file_exists():
    path = "./images-used/GIF"
    if_it_exists = os.path.exists(path)
    if if_it_exists:
      only_gif_files = [f for f in listdir('./images-used/GIF') if isfile(join('./images-used/GIF', f))]
      list_all_files.extend(only_gif_files)
  check_png_file_exists()
  check_jpg_file_exists()
  check_gif_file_exists()
  return jsonify(list_all_files)

def get_file_by_format(tipo):
  path = "./images-used/GIF"
  if_it_exists = os.path.exists(path)
  check_png = "./images-used/PNG"
  if_png = os.path.exists(check_png)
  check_jpg = "./images-used/JPG"
  if_jpg_exists = os.path.exists(check_jpg)
  try:
    incoming_tipo = tipo.lower()
    
    if incoming_tipo == 'png' and if_png:
      only_png_files = [f for f in listdir('./images-used/PNG') if isfile(join('./images-used/PNG', f))]
      return jsonify(only_png_files)
 
    elif incoming_tipo == 'jpg' and if_jpg_exists:
      only_jpg_files = [f for f in listdir('./images-used/JPG') if isfile(join('./images-used/JPG', f))]
      return jsonify(only_jpg_files)
    
    elif incoming_tipo == 'gif' and if_it_exists:

      only_gif_files = [f for f in listdir('./images-used/GIF') if isfile(join('./images-used/GIF', f))]
      return jsonify(only_gif_files)
    else:
      return 'No files of that type were found', 404
  except  TypeError:
    return {'msg': 'Mensagem de erro'}, 400
  except FileNotFoundError:
    return {'Files of that format do not exist'}, 400

def download_specific_file(name):
  try:
    png_file = name.lower().endswith(('png'))
    jpg_file = name.lower().endswith(('jpg'))
    gif_file = name.lower().endswith(('gif'))
    if png_file:
      return send_from_directory(directory='../images-used/PNG', path=f"{name}", as_attachment=True)
    elif jpg_file:
      return send_from_directory(directory='../images-used/JPG', path=f"{name}", as_attachment=True)
    else:
      return send_from_directory(directory='../images-used/GIF', path=f"{name}", as_attachment=True)
 
  except TypeError:
    return 'That file does not exist', 404
  except NotFound:
    return 'That file does not exist', 404
