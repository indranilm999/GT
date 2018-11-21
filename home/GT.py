from flask import Flask,render_template
app= Flask(__name__)

dates = [ {'date' :'November 21 2018'
    
    
    
        },
        
            { 'date' :'November 22 2018'  }
        
        
        ]

@app.route("/")
def home():    
    return render_template('home.html', dates = dates)

@app.route("/main")
def main():
    ret="<head>Main Page</head> <body><h1><b>Inside Body</b></h1></body>"
    return ret


if __name__ == '__main__':
    app.run(debug=True)
