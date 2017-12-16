from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to BMI test"

@app.route("/bmi/<weight>/<height>")
def bmi(weight,height):
    fl_weight = float(weight)
    fl_height = float(height)
    bmi = fl_weight / (fl_height* fl_height)
    if bmi < 16:
        return "severely underweight"
    else:
        if bmi <= 18.5:
            return "underweight"
        else:
            if bmi <= 25:
                return "Normal"
            else:
                if bmi <= 30:
                    return "overweigh"
                else:
                    return "obese"
@app.route("/bmi_2/<weight>/<height>")
def bmi_2(weight,height):
    fl_weight = float(weight)
    fl_height = float(height)
    bmi = fl_weight / (fl_height* fl_height)
    return render_template("bmi_2.html",weight=weight,height=height,bmi=bmi)
if __name__ == '__main__':
  app.run(debug=True)
