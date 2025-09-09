print ("Hello World")
@app.route("/hello")
def hello():
    return "Hello from Azure!"
@app.route("/broken")
def broken()   # <-- Notice the missing colon ':' here
    return "Oops!"
