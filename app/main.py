from flask import Flask, render_template

app = Flask(__name__)

# Lista de produtos fictícios (você pode substituir por um banco de dados depois)
produtos = [
    {
        "nome": "Shampoo Hidratante",
        "preco": "29,90",
        "imagem": "/static/produtos/shampoo.jpg"
    },
    {
        "nome": "Máscara Capilar",
        "preco": "39,90",
        "imagem": "/static/produtos/mascara.jpg"
    },
    {
        "nome": "Kit Reconstrução",
        "preco": "89,90",
        "imagem": "/static/produtos/kit.jpg"
    }
]

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
