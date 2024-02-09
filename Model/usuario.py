from typing import Any
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    login: str
    senha: str
    nome: str
    email: str
    telefone: str
    endereco: str
    cidade: str
    estado: str
    cep: str

    @staticmethod
    def from_dict(obj: Any) -> 'Usuario':
        assert isinstance(obj, dict)
        id = int(obj.get("id"))
        login = str(obj.get("login"))
        senha = str(obj.get("senha"))
        nome = str(obj.get("nome"))
        email = str(obj.get("email"))
        telefone = str(obj.get("telefone"))
        endereco = str(obj.get("endereco"))
        cidade = str(obj.get("cidade"))
        estado = str(obj.get("estado"))
        cep = str(obj.get("cep"))
        return Usuario(id, login, senha, nome, email, telefone, endereco, cidade, estado, cep)
    
    @staticmethod
    def from_position(obj: Any) -> 'Usuario':
        assert isinstance(obj, dict)
        id = int(obj[0])
        login = str(obj[1])
        senha = str(obj[2])
        nome = str(obj[3])
        email = str(obj[4])
        telefone = str(obj[5])
        endereco = str(obj[6])
        cidade = str(obj[7])
        estado = str(obj[8])
        cep = str(obj[9])
        return Usuario(id, login, senha, nome, email, telefone, endereco, cidade, estado, cep)

