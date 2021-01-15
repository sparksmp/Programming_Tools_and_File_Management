from flask import Flask, request, render_template
import random


app = Flask(__name__)
@app.route('/')


@app.route('/', methods=['POST'])
def generate_numbers():
    L = [x for x in range(1,71)]
    r5 = random.sample(L,5)
    r5.sort()
    r1 = random.sample(L[:26],1)
    return render_template('application.html', random5 = r5, random1 = r1)

if __name__ == '__main__':

   app.config['TEMPLATES_AUTO_RELOAD']=True
   app.run(debug=True,use_reloader=True)
   