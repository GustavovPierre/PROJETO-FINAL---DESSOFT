from flask import Flask, render_template, request

produtos = [
    {
        'id': 0,
        'nome_produto': 'Leite',
        'marca': 'Parmalat',
        'quantidade': 6,
        'feito': False,
    },
    {
        'id': 1,
        'nome_produto': 'Cerveja',
        'marca': 'Colorado',
        'quantidade': 2,
        'feito': False,
    },
    {   
        'id': 2,
        'nome_produto': 'Chocolate',
        'marca': 'Nestle',
        'quantidade': 5,
        'feito': False,
    },
    
]

mercados = {
    "Carrefour": {
        "Chocolate": {"nome_produto": "Chocolate","marca": "Nestle","valor unitario": 7.00},
        "Arroz": {"nome_produto": "Arroz","marca" : "Tio João","valor unitario": 4.00},
        "Refrigerante": {"nome_produto": "Refrigerante","marca" : "Lacta", "valor unitario": 5.00},
        "Carne": {"nome_produto": "Carne","marca" : "Friboi", "valor unitario": 30.00},
        "Frango": {"nome_produto": "Frango","marca" : "Perdigao", "valor unitario": 22.00},
        "Peixe": {"nome_produto": "Peixe","marca" : "Frescato", "valor unitario": 26.00},
        
        "cerveja": {"nome_produto" :"Cerveja", "marca" : "Colorado", "valor unitario": 20.80},
        },
    "Extra": {
        "chocolate": {"nome_produto" :"Chocolate", "marca": "Nestle","valor unitario": 4.80},
        "arroz": {"nome_produto" :"Arroz", "marca" : "Tio João","valor unitario": 4.40},
        "refrigerante": {"nome_produto" :"Refrigerante", "marca" : "Coca-Cola", "valor unitario": 4.30},
        "carne": {"nome_produto" :"Carne", "marca" : "Friboi", "valor unitario": 32.00},
        "frango": {"nome_produto" :"Frango","marca" : "Sadia", "valor unitario": 18.00},
        "peixe": {"nome_produto" :"Peixe", "marca" : "Frescato", "valor unitario": 23.00},
        "suco": {"nome_produto" :"Suco", "marca" : "Tang", "valor unitario": 8.90},
        "feijao": {"nome_produto":"Feijao", "marca" : "Kicaldo", "valor unitario": 5.25},
        "cerveja": {"nome_produto" :"Cerveja", "marca" : "Colorado", "valor unitario": 14.80},
        "Leite": {"nome_produto": "Leite","marca" : "Parmalat", "valor unitario": 5.00},
        },
    "Zona Sul": {
        "abobora": {"nome_produto" :"Abobora", "marca" : "Fazendinha", "valor unitario": 16.30},
        "arroz": {"nome_produto" :"Arroz", "marca" : "Tio João", "valor unitario": 5.55},
        "refrigerante": {"nome_produto" :"Refrigerante", "marca" : "Pepsi", "valor unitario": 3.99},
        "carne": {"nome_produto" :"Carne", "marca" : "Friboi", "valor unitario": 40.00},
        "frango": {"nome_produto" :"Frango", "marca" : "Fazendinha", "valor unitario": 18.99},
        "suco": {"nome_produto" :"Suco", "marca" : "Tang", "valor unitario": 8.33},
        "feijao": {"nome_produto" :"Feijao", "marca" : "Tio Joao", "valor unitario": 4.09},   
        "vinho": {"nome_produto" :"Vinho", "marca" : "Casillero del Diabo", "valor unitario": 55.99},
        "cerveja": {"nome_produto" :"Cerveja", "marca" : "Colorado", "valor unitario": 23.80},
        "Leite": {"nome_produto": "Leite","marca" : "Parmalat", "valor unitario": 10.00},
        "Chocolate": {"nome_produto": "Chocolate","marca": "Nestle","valor unitario": 9.00},
        },
}
    
carrinho = []
matching={}
for lista_produto in produtos:
    for mercado in mercados:
        for itens in mercados[mercado]:
            if lista_produto["marca"]==mercados[mercado][itens]["marca"] and lista_produto["nome_produto"]==mercados[mercado][itens]["nome_produto"]:
                matching = {
                        'nome_produto':lista_produto["nome_produto"],
                        'marca':lista_produto["marca"],
                        'preco':mercados[mercado][itens]["valor unitario"],
                        'quantidade':lista_produto["quantidade"],
                        'mercado':mercado,
                }
                carrinho.append(matching)

Carrefour=[]
a="Carrefour"
Extra=[]
b="Extra"
Zona_Sul=[]
c="Zona Sul"
for e in carrinho:
    if a==e["mercado"]:
        Carrefour.append(e)
    if b==e["mercado"]:
        Extra.append(e)
    if c==e["mercado"]:
        Zona_Sul.append(e)

x = (len(Carrefour)/len(produtos))*100        
y = (len(Extra)/len(produtos))*100 
z = (len(Zona_Sul)/len(produtos))*100

soma_carrefour=0
soma_extra=0
soma_zonasul=0
for i in Carrefour:
    soma_carrefour+=i["preco"]*i["quantidade"]
for u in Extra:
    soma_extra+=u["preco"]*u["quantidade"]
for z in Zona_Sul:
    soma_zonasul+=z["preco"]*z["quantidade"]

app = Flask(__name__)
"""
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)
"""

@app.route('/')
def homepage():
    return render_template('teste.html')
@app.route('/support/')
def suporte():
    return render_template('paginasuporte.html')
@app.route('/lojas/')
def lojas():
    return render_template('endereço.html')
@app.route('/fazer_compras/', methods=['POST', 'GET'])
def fazer_compras():
    mensagem_erro_nome_produto = ''
    mensagem_erro_quantidade = ''
    if request.method == 'POST':
        if 'id' in request.form:
            id = int(request.form['id'])
            produtos[id]['feito'] = request.form['feito'] == 'True'
        else:
            nome_produto = request.form['nome_produto']
            marca = request.form['marca']
            quantidade = request.form['quantidade']
            novo_produto = {
                'id': len(produtos),
                'nome_produto': nome_produto,
                'marca': marca,
                'quantidade': quantidade,
                'feito': False,
            }
            tem_erro = False
            if len(nome_produto) == 0:
                mensagem_erro_nome_produto = 'Nome do produto não pode ser vazio'
                tem_erro = True
            if not quantidade.isnumeric():
                mensagem_erro_quantidade = 'Quantidade deve ser um número inteiro'
                tem_erro = True
            if not tem_erro:
                produtos.append(novo_produto)
    return render_template('fazer_compras.html', produtos=produtos,
                           mensagem_erro_nome_produto=mensagem_erro_nome_produto,
                           mensagem_erro_quantidade=mensagem_erro_quantidade)

@app.route('/carrinho/', methods=['POST','GET'])
def carrinho():
    if request.method == 'POST':
        if 'id' in request.form:
            id = int(request.form['id'])
            produtos[id]['feito'] = request.form['feito'] == 'True'
    if len(produtos)==0:
        mensagem_mercado = "Não há produtos adicionados à lista"
    else:
        if soma_carrefour<soma_extra and soma_carrefour<soma_zonasul:
            mensagem_mercado = "O mercado mais barato para seu carrinho é o Carrefour, com {0}% dos produtos presentes.".format(round(x,2))
        elif soma_extra<soma_carrefour and soma_extra<soma_zonasul:
            mensagem_mercado = "O mercado mais barato para seu carrinho é o Extra, com {0}% dos produtos presentes.".format(round(y,2))
        else:
            mensagem_mercado = "O mercado mais barato para seu carrinho é o Zona Sul, com {0}% dos produtos presentes.".format(round(z,2))
            
    return render_template('carrinho.html', produtos=produtos, mensagem_mercado=mensagem_mercado)

@app.route('/signup/', methods=['POST','GET'])
def signup():
    mensagem_erro_nome = ''
    mensagem_erro_sobrenome = ''
    mensagem_erro_senha = ''
    if request.method == 'POST':
        if 'id' in request.form:
            id = int(request.form['id'])
            produtos[id]['feito'] = request.form['feito'] == 'True'
        else:
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            
            senha = request.form['senha']
            senha1 = request.form['senha1']
                            
            
            if len(nome) == 0:
                mensagem_erro_nome = 'Nome não pode ser vazio'
            if len(sobrenome) == 0:
                mensagem_erro_sobrenome = 'Sobrenome não pode ser vazio'
            if senha1 != senha:
                mensagem_erro_senha = 'As senhas não batem'
                
    return render_template('signup.html', produtos=produtos,
                           mensagem_erro_nome=mensagem_erro_nome,
                           mensagem_erro_sobrenome=mensagem_erro_sobrenome,
                           mensagem_erro_senha=mensagem_erro_senha)

@app.route('/login/', methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/produtos_disponiveis/', methods=['POST','GET'])
def produtos_disponiveis():
    if soma_carrefour<soma_extra and soma_carrefour<soma_zonasul:
        disponiveis = Carrefour
        soma_total = soma_carrefour
    elif soma_extra<soma_carrefour and soma_extra<soma_zonasul:
        disponiveis = Extra
        soma_total = soma_extra
    else:
        disponiveis = Zona_Sul
        soma_total = soma_zonasul
            
    return render_template('disponiveis.html', disponiveis=disponiveis, soma_total=soma_total)


"""
class RegisterForm(Form):
    name = StringField('Nome', [validators.Length(min=1, max=50)])
    username = StringField('Nome de Usuário', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senha Inválida')
    ])
    confirm = PasswordField('Confirme a Senha')
    
@app.route('/signup/', methods=['POST','GET'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate:
        render_template('signup.html')
    return render_template('signup.html', form=form)
"""

app.run('0.0.0.0', 5000, True)