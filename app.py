print ("Hello World")
@app.route("/hello")
def hello():
    return "Hello from Azure!"
@app.route("/broken")
def broken():
    return "Oops!"
