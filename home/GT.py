from flask import Flask
app= Flask(__name)


@app.route("/")
def home:    
    return "Running Successfully"
