from flask import Flask,render_template
from mlab import mlab_connect
from models.champ import Champ
from flask import *
app = Flask(__name__)

mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')



@app.route("/upload")
def upload():
    return render_template('upload.html', champs = Champ.objects())



@app.route("/admin")
def admin():
    return render_template("admin.html", champs = Champ.objects())

@app.route("/delete/<champ_id>")
def delete(champ_id):
    dels = Champ.objects(id = champ_id)
    dels.delete()
    return redirect("http://127.0.0.1:5000/admin",code =302)


@app.route("/info/<champ_id>")
def info(champ_id):
    c_info = Champ.objects().with_id(champ_id)
    c_img = c_info.image
    c_role = c_info.role
    c_name = c_info.name
    return render_template("info.html",c_img = c_img, c_role = c_role , c_name = c_name)

if __name__ == '__main__':
  app.run(debug=True)
