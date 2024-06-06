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


# @app.route('/get-item/<string:name>')   using dynamic url
# def get_item(name):
#     for item in cafe_menu:
#         if name == item['name']:
#             return item
#     return {"message":"Item doesn't Exist"}


@app.route('/get-item')      #using arguments
def get_item():
    name = request.args.get('name')
    for item in cafe_menu:
        if name == item['name']:
            return item
    return {"message":"Item doesn't Exist"}, 404


@app.route('/additem', methods=['POST'])
def add_item():
    if request.method == 'POST':  
        new_item = request.get_json()
        print(new_item)
        cafe_menu.append(new_item)
        return {'message': 'new item added successfully'}, 201


@app.route('/update-item', methods=['PUT'])
def update_item():
    item_name = request.get_json()
    for item in cafe_menu:
        item['name'] = item_name['name']
        item['price'] = item_name['price']
        return {"message":"Item Updated Successfully"}
    return {"Item doesn't exist"}


@app.route('/delete-item', methods=['DELETE'])
def delete_item():
    item_name = request.args.get('name')
    for item in cafe_menu:
        if item_name == item['name']:
            cafe_menu.remove(item)
            return {"message":"Item Deletes Successfully"}
    return {"message":"Item doesn't Exist"}



if __name__=='__main__':
    app.run(debug=True)