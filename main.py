from flask import Flask, render_template, request
from ML import livePredictions

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        pred = livePredictions(path='SER_model.h5',file='audio.wav')
        pred.load_model()
        prediction = pred.makepredictions()
        print(prediction)
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)