from flask import Flask, jsonify, request




app = Flask(__name__)





@app.route('/data/api/v1.0/test_data',methods=['POST','GET',])
def test_data():


    return jsonify({"Test Data ":"data"})



if __name__ == '__main__':
    app.run(debug=True)