from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def lol_guide():
    champs = [
        {
            'image': 'Yasuo.png',
            'name':'Yasuo',
            'group':'Đấu sĩ'
        },
        {
            'image': 'Velkoz.png',
            'name':"Vel'Koz",
            'group':'Pháp Sư'
        },
        {
            'image': 'Jhin.png',
            'name':'Jhin',
            'group':'Xạ thủ'
        },
        {
            'image': 'Zed.png',
            'name':'Zed',
            'group':'Sát thủ'
        },
        {
            'image': 'Ornn.png',
            'name':'Ornn',
            'group':'Đấu sĩ/Chống chịu'
        },
    ]
    return render_template('league.html', champs = champs)

if __name__ == '__main__':
  app.run(debug=True)
