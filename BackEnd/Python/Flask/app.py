from flask import Flask, render_template

#Ta instanciando o servidor flask neste código
app = Flask(__name__) #Aqui que vai organizar tudo

#Vai definir a url raiz da página (Home page)
@app.route('/')
def home():
    return render_template("home.html")#É o que vai mostrar ao acessar a página inicial

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/consulta')
def consulta():
    return render_template("consulta.html")

#Pra garantir que é o proprio arquivo que esta chamando a função
if __name__ == '__main__':
           #Modo debug vai colocar os erros mais detalhados na tela
    app.run(debug=True)