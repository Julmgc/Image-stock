from flask import Flask, jsonify, request, send_from_directory, render_template
from werkzeug.utils import secure_filename
import os
from pathlib import Path
from dotenv import get_key

ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif'}
MAX_CONTENT_LENGTH = 1 * 1024 * 1024

directory = get_key('./.env', 'FILES_DIRECTORY')
app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

@app.route('/upload', methods=['POST'])
def upload_file():
  check_exists_file = Path(request.files["file"]).is_file()
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
        print('PNG exists') 
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
        print('JPG exists')   
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
        print('GIF exists')   
        f.save(f".image/GIF/{f.filename}")
        return jsonify(f.filename), 201
      else:
        path = os.path.join(directory, 'GIF')
        os.mkdir(path) 
        f.save(f"{directory}/GIF/{f.filename}")
        return jsonify(f.filename), 201
  except KeyError as e:   
    return {'msg': str(e)}, 500      
  except TypeError as e:
    return {'msg': str(e)}, 409
  # else:
  #   return jsonify('Not an accepted file format'), 415 

  #  f.save(f"{directory}/{f.filename}")
  #  return jsonify('Foi')
      





@app.route('/files', methods=['GET'])
def list_files():
  ...
# que irá listar todos os arquivos


@app.route('/files/<type>', methods=['GET'])
def list_files_by_type():
  ...
# lista os arquivos de um determinado tipo


@app.route('/download/<file_name>', methods=['GET'])
def download():
  ...
# faz o download do arquivo solicitado em file_name

@app.route('/download-zip', methods=['GET'])
def download_dir_as_zip():
  ...
  # Utilizar o diretório /tmp do linux e a biblioteca os para executar um 
# comando de terminal e gerar o arquivo zip temporariamente e fazer o 
# download desse arquivo;
  # zipar e salvar no tmp que está em Home 
# com query_params-file_type, compression_rate
# para especificar o tipo de arquivo para baixar todos
# compactados e também a taxa de compressão

# 6ª ROTA ?
# @app.route('/static/<path:filename>', methods=['GET'])
# def upload():
#   ...
# O QUE É PRA FAZER?

# Specifies the maximum size (in bytes) of the files to be uploaded

# If the uploaded file is too large, Flask will automatically return status code 413 Request Entity Too Large 

# FILES_DIRECTORY- caminho principal aonde os arquivos são salvos - variável de ambiente

# Regras e observações:
# Cada tipo de arquivo é salvo em um subdiretório no diretório
#  principal parametrizado;

# O caminho do diretório principal onde os arquivos são salvos 
# pode ser parametrizado por uma variável de ambiente FILES_DIRECTORY;

# O tamanho máximo de arquivos deve ser parametrizado via variável 
# de ambiente MAX_CONTENT_LENGTH e possuir o valor 1MB por padrão;

# As operações sobre arquivos devem ser importadas de uma biblioteca
#  (pacote) criada por você e chamada de kenzie, em um módulo chamado image;

# Caso os diretórios necessários não existam, devem ser criados sempre 
# que a aplicação iniciar. No __init__ do pacote.


# Você pode utilizar os arquivos disponíveis para download no canvas para testar;

# Utilizar padrão JSON para listar os arquivos;

# Todos os erros devem ser tratados como exceções;

# Os fluxos normais, devem ser os casos retornados sem ter captado nenhuma 
# exceção na execução do código;



# As funções do módulo image devem possuir docstrings que auxiliem a 
# utilização;

# As exceções devem gerar uma resposta com o status_code que mais faz 
# sentido (Consulte a rubrica);

# As operações com arquivos e diretórios não deve ser implementada 
# dentro da rota. A lógica e tratamentos devem ser implementados na 
# biblioteca e importado no app para utilizar nas rotas sempre que possível.

# Tome o cuidado de adicionar uma regra para os arquivos de upload 
# não serem adicionados ao repositório.