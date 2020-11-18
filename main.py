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
        return redirect("/happy")
    if(prediction=='disgust'):
        return redirect("/disgust")
    if(prediction=='angry'):
        return redirect("/angry")
    if(prediction=='fearful'):
        return redirect("/fearful")
    if(prediction=='happy'):
        return redirect("/happy")
    if(prediction=='surprised'):
        return redirect("/surprised")
    if(prediction=='sad'):
        return redirect("/sad")
    if(prediction=='neutral'):
        return redirect("/happy")
    return "Hello"

@app.route('/disgust', methods=["GET","POST"])
def disgust():    
    return render_template('disgust.html')

@app.route('/happy', methods=["GET","POST"])
def happy():    
    return render_template('happy.html')

@app.route('/angry', methods=["GET","POST"])
def angry():    
    return render_template('angry.html')

@app.route('/fearful', methods=["GET","POST"])
def fearful():    
    return render_template('fearful.html')

@app.route('/sad', methods=["GET","POST"])
def sad():    
    return render_template('sad.html')

@app.route('/surprised', methods=["GET","POST"])
def surprised():    
    return render_template('surprised.html')

if __name__ == "__main__":
	app.run(debug=True)