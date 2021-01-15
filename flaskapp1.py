from flask import Flask

#set up flask by creating an instance which we will call app
app = Flask(__name__)

#@ symbol denotes a Python decorator (an advanced topic).
#the following line tells flask that we want the app (a bit like a webpage) 
#to be served at the root of the URL

@app.route('/') # this function tells flask what data we want to send to the app (webpage)
def basic():
    return 'Hi Everybody! \n You can put any content you want here.'


# each function can now be seen as specific part of the app with its own path
@app.route('/test')
def test():
    return 'This is a test app!!'
    #to access, go to  http://127.0.0.1:5000/test

#adding variables
@app.route('/<name>')
def name_site(name):
    return 'Welcome, {name}! Welcome back!'.format(name=name)
    #to access, go to http://127.0.0.1:5000/yourname

if __name__ == '__main__':
   app.run()
