from flask import Flask

app = Flask(__name__)


cafe_menu = [
    {
        'name':'White Sauce Pasta',
        'price':80
    },
    {
        'name':'Cold Coffee',
        'price':90
    },
    {
        'name':'Virgin Mojito',
        'price':90
    },
    {
        'name':"Momos",
        'price':60
    }
]



@app.route('/getmenu')
def get_menu():
    return {'menu':cafe_menu}


if __name__=='__main__':
    app.run(debug=True)