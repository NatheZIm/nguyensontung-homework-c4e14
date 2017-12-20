from flask import Flask,render_template
from mlab import mlab_connect
from models.champ import Champ
from flask import Flask, render_template
app = Flask(__name__)

mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')
def upload():
    return render_template('upload.html', all_champs = Champ.objects())

if __name__ == '__main__':
  app.run(debug=True)
 
