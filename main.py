from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/getParam')
def getParam():
    #print(request.args.get('vards'))
    return f"It Works! {request.args.get('vards')}"

@app.route('/postMsg', methods = ['POST'])
def postMsg():
    #print(request.json)
    data = request.json
    return f"This is post! {data['vatds']}"

@app.route('/info', methods = ['GET', 'POST'])
def info():
    if request.method == "GET":
        return "This is info GET route!"
    elif request.method == "POST":
        return "This is info POST route!"
    else:
        return "Unknow request method!"


app.run(host='0.0.0.0', port=80, debug=True)
