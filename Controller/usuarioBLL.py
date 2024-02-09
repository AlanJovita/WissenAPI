from Model.usuario import Usuario
from Data.bd import *

class UsuarioBLL():

    def Login(login:str,senha:str)->str:
        
        result = selectAll(f"select * from usuario where login = '{login}' and senha = '{senha}'")

        if result==None or len(result)==0:
            return '{status:False}'
        else:
            return '{status:True}'







        
        

