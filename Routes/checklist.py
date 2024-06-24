import os
from flask import Blueprint,make_response,jsonify, redirect, render_template, request, url_for
from Data.bd import *

checklist = Blueprint("checklist",__name__)

@checklist.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    filename = os.path.join(os.getcwd(), file.filename)
    file.save(filename)
    
    # Salvar a imagem no armazenamento do Appwrite
    try:
        file_data = open(filename, 'rb')
        os.remove(filename)  # Remover o arquivo local depois de carregado
        file_info = createFile(file=file_data)
        return f'Imagem carregada com sucesso! ID do arquivo: {file_info["$id"]}'
    except Exception as e:
        return f'Ocorreu um erro ao carregar a imagem: {str(e)}'

@checklist.route('/checklist',methods=['GET','POST'])
def Page():
        if request.method == 'POST':
            # Obter os dados do formulário
            cliente = request.form['cliente']
            whatsapp = request.form['whatsapp']
            valor = request.form['valor']
            valor_pago = request.form['valor_pago']
            valor_adicional = request.form['valor_adicional']
            valor_desconto = request.form['valor_desconto']

        # Salvar os dados na tabela "obra" do banco de dados Appwrite
            
            result = createDocument(Table.Obra,document={
                'cliente': cliente,
                'whatsapp': whatsapp,
                'valor_original': valor,
                'valor_servico': valor,
                'valor_pago': valor_pago,
                'valor_adicional': valor_adicional,
                'valor_desconto': valor_desconto
            })

            if result is None:
                  print('Erro ao salvar os dados')
            else:
                  print('Dados salvos com sucesso')

            return redirect(url_for('checklist.Page'))

        # Obter os relatórios cadastrados do banco de dados Appwrite
        rt = listDocuments(Table.Obra, filter=[])

        if rt is None:
              rt=[] 

        return render_template('checklist.html', relatorios=rt)