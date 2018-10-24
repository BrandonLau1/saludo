from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "El numero 1 no es primo"
 
if __name__ == "__main__":
    app.run()
