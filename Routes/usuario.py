from flask import Blueprint,make_response,jsonify
from Controller.usuarioBLL import UsuarioBLL

usuario = Blueprint("usuario",__name__)

@usuario.route('/autenticacao/<string:login>/<string:senha>',methods=['GET'])
def autenticacao(login,senha):
        return make_response(jsonify(UsuarioBLL.Login(login,senha)))
    
