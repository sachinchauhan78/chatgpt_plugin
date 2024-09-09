from flask import Flask, render_template,request,jsonify
import requests


app = Flask(__name__)
@app.route ('/')
def index():
    return render_template('index.html')
@app.route ('/chat',methods=['post'])
def chat():
    user_message =request.form['message']
    try:
        response =request.post('7.0.0.1:5000/chat',
        json={'message':user_message})
        ai_message =response.json().get ('response','')
        return jsonify({'response':ai_message})
    except Exception as e:
        return jsonify({'error':str(e)}),500
    if __name__=='__main__':
     app.run(debug=True)
