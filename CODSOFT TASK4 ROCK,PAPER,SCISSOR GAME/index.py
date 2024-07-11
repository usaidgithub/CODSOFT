import flask
import random
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
app=Flask(__name__)
CORS(app)
random_number=random.randint(0,2)
list=["rock","paper","scissor"]
@app.route('/')
def index():
    return render_template('guess.html')
@app.route('/submit_query',methods=['POST'])
@cross_origin()
def submit_query():
    if request.method=='POST':
        user_input=request.form.get('guess')
        computer_input=list[random_number]
        if(user_input=="rock" and computer_input=="paper"):
            message=f"Computer choice:{computer_input},User's Choice:{user_input},Computer Won"
        elif(user_input=="rock" and computer_input=="scissor"):
            message=f"Computer choice:{computer_input},User's choice:{user_input},You Won"
        elif(user_input=="scissor" and computer_input=="rock"):
            message=f"Computer choice:{computer_input},User's choice:{user_input},Computer Won"
        elif(user_input=="scissor" and computer_input=="paper"):
            message=f"Computer choice:{computer_input},User's choice:{user_input},You Won"
        elif(user_input=="paper" and computer_input=="rock"):
            message=f"Computer choice:{computer_input},User's choice:{user_input},You Won"
        elif(user_input=="paper" and computer_input=="scissor"):
            message=f"Computer choice:{computer_input},User's choice:{user_input},Computer Won"
        elif(user_input==computer_input):
            message=f"Computer choice:{computer_input},User's choice:{user_input},It is a draw"
        print(f"The return message is {message}")
        return jsonify({'message':message})
@app.route('/reset_game',methods=["GET"])
@cross_origin()
def reset_game():
    global random_number
    if request.method=="GET":
        random_number=int(random.randint(0,2))
        return jsonify({'message':"game reset successfuuly"})


if(__name__=='__main__'):
    app.run(debug=True,port=3000)