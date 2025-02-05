from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to Flask!"

@app.route('/home/<name>')
def hello(name):
    return f"hello,{name}!"

@app.route('/data', methods=['GET'])
def get_data():
    data = request.json
    return{"data":data, "message":"send a POST request with json data "} 

@app.route('/data', methods=['POST'])
def handle_data():
    data = request.json
    return{"message":"data received","data":data}

@app.route('/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return{"message":f"Item{item_id} updated"}

@app.route('/delete/<int:item_id>', methods=['DELETE'])  
def delete_item(item_id):
    return{"message":f"Item{item_id} deleted"}

if __name__ == '_main_':
     app.run(debug=True)
       
