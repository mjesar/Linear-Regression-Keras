from flask import Flask, jsonify, request
from keras.models import load_model
trained_model = load_model('trained_model.h5')



app = Flask(__name__)





@app.route('/data/api/v1.0/test_data',methods=['POST','GET',])
def test_data():

    if request.method == 'POST':


        return jsonify({"POST Method ":"data"})

    elif request.method == 'GET':

        data = request.get_json(force=True)


        #get data from json post request
        X_new=data['test_data']


        #load saved model
        trained_model = load_model('trained_model.h5')
        

        return jsonify({"GET Method":"Data"})



if __name__ == '__main__':
    app.run(debug=True)