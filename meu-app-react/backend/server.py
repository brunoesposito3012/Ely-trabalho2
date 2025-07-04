from flask import Flask
from flask_cors import CORS
from alunos import alunos_bp

app = Flask(__name__)
CORS(app)  

app.register_blueprint(alunos_bp)

@app.route('/')
def home():
    return {"message": "API do Sistema de Alunos está funcionando!"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)



