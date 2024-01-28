from flask import Flask, render_template, request, flash
import pyshorteners

app = Flask(__name__)
app.secret_key = 'amo-programar'  # Chave secreta para proteção

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        try:
            # Captura a URL recebida do formulário
            url_recebida = request.form["url"]

            # Encurta a URL usando a API do TinyURL
            url_encurtada = pyshorteners.Shortener().tinyurl.short(url_recebida)
            flash("URL encurtada com sucesso")
            # Renderiza o template com as URLs original e encurtada
            return render_template("form.html", nova_url=url_encurtada, url_antiga=url_recebida)
        except pyshorteners.exceptions.ShorteningErrorException as e:
            flash('Erro ao encurtar a URL. Certifique-se de que é uma URL válida.')
        except Exception as e:
            flash('Ocorreu um erro inesperado.')
   
    return render_template('form.html')
