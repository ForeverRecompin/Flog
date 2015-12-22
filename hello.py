from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

# Route registered to app's index
@app.route('/')
def index():
    #return('<h1>Hello! :></h1>')
    return(render_template('index.html'))

# Dynamic route
@app.route('/user/<name>')
def user(name):
    #return('<h1>Hello, %s!</h1>' % name)
    return(render_template('user.html', name=name))

# Dynamic route with an int component
@app.route('/uid/<int:id>')
def uid(id):
    return('<h1>Hello, %d user-id!</h1>' % id)

# Dynamic route with a float component
@app.route('/float_balance/<float:balance>')
def float_balance(balance):
    return('<h1>Balance: %f</h1>' %balance)

# Dynamic route with a path component
@app.route('/weird_path/<path:address>')
def weird_path(address):
    return("<h1>You're here: %s</h1>" %address)

# Demonstrate request contexts - objects that are accessed by view
# functions are made global temporarily to avoid cluttering view functions
# with a lot of objects(they'd have be passed as parameters to view functions)
@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return ('<p>Your browser is %s</p>' % user_agent)

# Ensures - web server is started only when it's directly started
# (and not when it's imported by another script)
if __name__ == '__main__':
    app.run(debug=True)

''' Check each of the following in the Address bar:
http://localhost:5000/
http://localhost:5000/user/Joe
http://localhost:5000/uid/123
http://localhost:5000/float_balance/2015.007
http://localhost:5000/weird_path/some_directory/some_file.html
http://localhost:5000/browser
'''
