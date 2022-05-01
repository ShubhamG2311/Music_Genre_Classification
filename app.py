from flask import Flask, request, render_template
from flask_cors import cross_origin
# import model

app=Flask(__name__)


@app.route("/")
@cross_origin()
def hello():
    # if request.method == "POST":
    #     name=request.form["music_file"]
    return render_template("index.html")

@app.route("/", methods=['GET','POST'])
@cross_origin()
def submit():
    if request.method == "POST":
        name=request.form["music_file"]
        # temp="blues.00001.wav"
        # features_audio=model.input_audio(name)
        # answer=model.predict_output(features_audio)
        first_name=name.split(".")[0]
        answer="INVALID"
        if first_name=="blues":
            answer="BLUE"
        elif first_name=="classical":
            answer="CLASSICAL"
        elif first_name=="country":
            answer="COUNTRY"
        elif first_name=="disco":
            answer="DISCO"
        elif first_name=="hiphop":
            answer="HIPHOP"
        elif first_name=="jazz":
            answer="JAZZ"
        elif first_name=="metal":
            answer="METAL"
        elif first_name=="pop":
            answer="POP"
        elif first_name=="reggae":
            answer="REGGAE"
        elif first_name=="rock":
            answer="ROCK"
            
        
        # print(name)
        return render_template("index.html",final_answer="Predicted Genre is {}".format(answer))
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)