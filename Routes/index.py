from flask import Blueprint,  render_template,request,redirect,url_for,session
from Controller.usuarioBLL import UsuarioBLL
from Controller.form import CreateAccountForm, LoginForm
from Model.usuario import Usuario

index = Blueprint('index', __name__)

@index.route('/', methods=['GET','POST'])
def getLogin():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']
        
        # Locate user
        logado = UsuarioBLL.Login(username,password)
        
        # Check the password
        if logado:
           session['username'] = username
           return redirect(url_for('index.getIndex'))

        # Something (user or pass) is not ok
        return render_template('Login/login.html',
                               msg='Usuário ou senha incorretos',
                               form=login_form)

    else:
        return render_template('Login/login.html',form=login_form)
    

@index.route('/index', methods=['GET'])
def getIndex():
    if session.get('username'):       
        return render_template('index.html', segment='index')
    else:
        return redirect(url_for('index.getLogin')) 

    
    
@index.route('/registrar', methods=['GET','POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        novo_usuario = Usuario()

        novo_usuario.nome = request.form['nome_fantasia']
        novo_usuario.senha = request.form['cnpj_create']

        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        user = None #Users.query.filter_by(username=username).first()
        if user:
            return render_template('Login/register.html',
                                   msg='Ja existe uma conta cadastrada com esse usuário',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user =None #Users.query.filter_by(email=email).first()
        if user:
            return render_template('Login/register.html',
                                   msg='Ja existe uma conta com esse email',
                                   success=False,
                                   form=create_account_form)
     
        
        return render_template('Login/register.html',
                               msg='Usuário registrado com sucesso',
                               success=True,
                               form=create_account_form)
    else:
        return render_template('Login/register.html', form=create_account_form)


@index.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index.getLogin'))

@index.route('/clientes')
def clientes():
    return render_template('clientes.html', segment='clientes')

@index.route('/prestadores')
def prestadores():
    return render_template('prestadores.html', segment='prestadores')

@index.route('/servicos')
def servicos():
    return render_template('servicos.html', segment='servicos')

