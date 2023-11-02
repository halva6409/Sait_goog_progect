from flask import Flask
from gen_pin import genn_pin

app = Flask(__name__)


@app.route('/')
def hello_word():
    return '''
    <a href="gen_pas">Сгенерировать пароль</a>
    <p>
        <a href="https://www.google.ru">
        <img scr="static/images/гугл_лог_2.jpeg" width="1500" heght="200" alt="imag">
        </a>
    </p>    
    
    
    '''
gen = genn_pin

@app.route("/gen_pas")
def genn_pas():
    return f'{gen}'




app.run(debug=True)