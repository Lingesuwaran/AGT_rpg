from flask_ngrok import run_with_ngrok
from flask import Flask, render_template,request
from game import game,name_changer

name = "" 
app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def Title_screen():
  return render_template('Title_screen.html')

@app.route('/username',methods = ["POST","GET"])
def Username():
  if request.method == "POST":
    name = request.form["input"]
  return render_template('name.html')

@app.route('/Play',methods= ["POST",'GET'])
def Play():
  data = ""
  if request.method == "POST":
    input1 = request.form["input"]
    print(input1)
    data = game.Menu(1,str(data+" "+input1))
    data = name_changer.names(data,name)
    return render_template('Play.html',data=data)
  else:
    data = game.Menu(1,1)
    data = name_changer(data)
    return render_template('Play.html',data=data)


app.run()