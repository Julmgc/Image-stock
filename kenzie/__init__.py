# escrever as funções aqui
# 
import os
from os.path import isfile, join
from flask import request, jsonify

directory = os.environ.get('FILES_DIRECTORY')

def create_files_directory_variable():
  if 'FILES_DIRECTORY' in os.environ:
    pass
  else:
    os.environ['FILES_DIRECTORY'] = './image'


# def create_image_files():
#   def check_png():
#     path = './image/PNG'
#     if_it_exists = os.path.exists(path)
#     if if_it_exists:
#       ...
#     else:
#       path = os.path.join(directory, 'PNG')
#       os.mkdir(path)
#   def check_jpg():
#     path = "./image/JPG"
#     if_jpg_file_exists = os.path.exists(path) 
#     if if_jpg_file_exists:
#       ...
#     else:
#       path = os.path.join(directory, 'JPG')
#       os.mkdir(path)
#   def check_gif():
#     path = "./image/GIF"
#     if_gif_file_exists = os.path_gif.exists('GIF')
#     if if_gif_file_exists:
#       ...
#     else:
#       path = os.path.join(directory, 'GIF')
#       os.mkdir(path)
#   check_png()      
#   check_jpg()
#   check_gif()
#   return 'all files checked'


# def upload_files_function():

#   try:
#     f = request.files["file"]
#     filename_variable = f.filename

#     png_file = filename_variable.lower().endswith(('png'))
#     jpg_file = filename_variable.lower().endswith(('jpg'))
#     gif_file = filename_variable.lower().endswith(('gif'))
#     if png_file:
#       path = './image/PNG'
#       if_it_exists = os.path.exists(path)
    
#       if if_it_exists:
       
#         f.save(f"./image/PNG/{f.filename}")
#         return jsonify(f.filename), 201
#       else:
#         path = os.path.join(directory, 'PNG')
#         os.mkdir(path) 
#         f.save(f"{directory}/PNG/{f.filename}")
#         return jsonify(f.filename), 201
#     elif jpg_file:
#       path = './image/JPG'
#       if_it_exists = os.path.exists(path)
#       if if_it_exists:
          
#         f.save(f".image/JPG/{f.filename}")
#         return jsonify(f.filename), 201
#       else:
#         path = os.path.join(directory, 'JPG')
#         os.mkdir(path) 
#         f.save(f"{directory}/JPG/{f.filename}")
#         return jsonify(f.filename), 201
#     elif gif_file:
#       path = './image/GIF'
#       if_it_exists = os.path.exists(path)
#       if if_it_exists:
           
#         f.save(f".image/GIF/{f.filename}")
#         return jsonify(f.filename), 201
#       else:
#         path = os.path.join(directory, 'GIF')
#         os.mkdir(path) 
#         f.save(f"{directory}/GIF/{f.filename}")
#         return jsonify(f.filename), 201
    
#     else:
#       return "File format not aloud", 415
#   except KeyError as e:   
#     return {'msg': str(e)}, 500      
#   except FileNotFoundError:
#     return "File already exists", 409
#   except TypeError:
#     return "File format not aloud", 415
