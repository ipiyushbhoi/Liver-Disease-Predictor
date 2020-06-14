from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
#app = Flask(__name__)

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('index2.html')


@app.route('/predict',methods = ['POST','GET'])
def predict():
    int_features = []

    for x in request.form.values():
        if x == 'Male':
            int_features.append(0)
        elif x == 'Female':
            int_features.append(1)
        else:
            int_features.append(float(x))
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
  

    if output >=1.10 and output <= 1.27:
        output /= 3.7
    else:
        output /= 1.5
    output *= 100
    if output > 100:
        output /= 110
        output  *= 100
   

    if output > 50:
        return render_template('fail.html', pred='Probability of Liver Failure is {:.2f} %'.format(output))
    return render_template('success.html', pred='Probability of Liver Failure is {:.2f} %'.format(output))


if __name__ == '__main__':
    app.run(debug = True)


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
