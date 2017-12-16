from flask import Flask, render_template
from flask import *
app = Flask(__name__)


@app.route('/about-me')
def aboutme():
    self = [
        {
            "name" :"Nguyễn Sơn Tùng",
            "work" : "I'm a techkids's student",
            "study" : "At techkids",
            "hobbies" : "I like to play games",
            "crush":"My crush is my right hand"
        }
    ]
    return render_template('self.html',selfs=self)


@app.route("/school")
def school():
    return redirect("http://techkids.vn",code =302)
if __name__ == '__main__':
  app.run(debug=True)

@app.route("/")
