from flask import Flask, render_template

app = Flask (_name_)

@app.route('/')
@app.route('Jobs')
def Jobs():
    return render_template('index.html')
