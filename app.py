import os
import sys

sys.path.insert(0,os.path.dirname(__file__))

from flask import Flask
from Routes.usuario import usuario
from Routes.index import index
from Routes.checklist import checklist

from config import config_dict

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = Flask(__name__,template_folder="View")
app.config.from_object(app_config)
app.register_blueprint(usuario)
app.register_blueprint(index)
app.register_blueprint(checklist)

app.config['JSON_SORT_KEYS']=False
app.config['JSON_AS_ASCII'] = False

app.run(debug=True)

# def register_blueprints(app):
#     # Obtém a lista de arquivos no diretório 'routes'
#     route_files = os.listdir(os.path.dirname(__file__))

#     # Loop através dos arquivos e importa todos os blueprints
#     for filename in route_files:
#         if filename.endswith(".py") and filename != "__init__.py":
#             module_name = filename[:-3]  # Remove a extensão .py
#             module = __import__(f"routes.{module_name}", fromlist=["routes"])
#             blueprint = getattr(module, f"{module_name}_blueprint")
#             app.register_blueprint(blueprint, url_prefix=f"/{module_name}")

# app = Flask(__name)

# # Chame a função para registrar os blueprints
# register_blueprints(app)