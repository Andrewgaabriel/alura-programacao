from flask import Flask, render_template


class jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)

@app.route('/inicio')
def inicio():
    jogo1 = jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = jogo('God Of War', 'Rack n Slash', 'PS2')
    jogo3 = jogo('Mortal Kombat', 'Luta', 'PS2')    
    
    jogosLista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=jogosLista)


app.run(host='0.0.0.0', port=8080, debug=True) 