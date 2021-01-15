from flask import Flask, request, render_template


app = Flask(__name__)
@app.route('/')

@app.route('/', methods=['POST'])

def index():
     return render_template('converter.html')

if __name__ == '__main__':
     app.config['TEMPLATES_AUTO_RELOAD'] = True
     app.run(debug = True, use_reloader = True)