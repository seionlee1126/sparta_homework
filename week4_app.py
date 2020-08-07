from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('week4_index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    info = {
        'name' : name_receive,
        'amount' : amount_receive,
        'address' : address_receive,
        'phone' : phone_receive
    }

    db.infos.insert_one(info)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    info_list = list(db.infos.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'info_list': info_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)