from flask import Flask, request, render_template
import random


app = Flask(__name__)
@app.route('/')


@app.route('/', methods=['POST'])
def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    return render_template('Quiz9.asp', die1 = dice1, die2 = dice2, total = sum)

if __name__ == '__main__':

   app.config['TEMPLATES_AUTO_RELOAD']=True
   app.run(debug=True,use_reloader=True)