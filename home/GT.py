from flask import Flask
app= Flask(__name__)


@app.route("/")
def home():    
    return "Running Successfully"

@app.route("/main")
def main():
    ret="<head>Main Page</head> <body><h1><b>Inside Body</b></h1></body>"
    return ret
