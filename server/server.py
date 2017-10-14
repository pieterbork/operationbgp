from flask import Flask, render_template, url_for
import random
app = Flask(__name__)


@app.route('/')
def index():

    colors = []
    with open('colors.txt') as f:
        colors = f.readline().split(',')
    
    maxlen = len(colors) -1
    
    ran = random.randint(0, maxlen)
    print(ran, maxlen)
    color=colors[ran]

    return render_template("index.html", color=color)

if __name__ == '__main__':
    app.run()
