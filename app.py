from flask import Flask, request

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


@app.route('/additem', methods=['POST'])
def add_item():
    if request.method == 'POST':  
        new_item = request.get_json()
        print(new_item)
        cafe_menu.append(new_item)
        return {'message': 'new item added successfully'}, 201


if __name__=='__main__':
    app.run(debug=True)