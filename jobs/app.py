from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
@app.route('Jobs')
def Jobs():
    return render_template('index.html')
