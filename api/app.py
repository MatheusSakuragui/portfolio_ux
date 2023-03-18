from flask import Flask, app, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contatos.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
