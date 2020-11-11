from flask import Flask, render_template, request, redirect
from ML import livePredictions

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        return redirect("/pred")

        # pred = livePredictions(path='SER_model.h5',file='audio.wav')
        # pred.load_model()
        # prediction = pred.makepredictions()
        # print(prediction)
        # if(prediction=='calm'):
        # 	return redirect("/disgust")
        # if(prediction=='disgust'):
        # 	return redirect("/disgust")
        # print("abc")
    
    return render_template('index.html')

@app.route('/pred', methods=["GET","POST"])
def pred():
    pred = livePredictions(path='SER_model.h5',file='audio.wav')
    pred.load_model()
    prediction = pred.makepredictions()
    print(prediction)
    if(prediction=='calm'):
        return redirect("/calm")
    if(prediction=='disgust'):
        return redirect("/disgust")
    return "Hello"

@app.route('/disgust', methods=["GET","POST"])
def disgust():    
    return render_template('disgust.html')

@app.route('/calm', methods=["GET","POST"])
def calm():    
    return render_template('calm.html')

if __name__ == "__main__":
	app.run(debug=True)