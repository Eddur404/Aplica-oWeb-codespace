from Flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá mundo'

# blablabla