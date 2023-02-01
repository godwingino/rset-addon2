from flask import Flask
from flask import render_template
# used for parsing requests from client
from flask import request

app = Flask(__name__)

#base root 
@app.route('/')
def hello_world():
#    return 'Hello World'
    return render_template('index.html')

#path or url hello
@app.route('/hello')
def hello():
    return 'Hello World-path hello'

#url with name as argument to get function
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
# url with datatype int
@app.route('/post/<username>/<int:post_id>')
def show_post(username,post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
# adding more than one path
@app.route('/greeting')
@app.route('/greeting/<name>')
def hello_greeting(name=None):
    return render_template('greeting.html', name=name)
# using request methods get and post
@app.route('/mailsent',methods=['GET','POST'])
def sentmail():
    email = request.form.get('email')
    name = request.form.get('name')
    print('email',email)
    print('name',name)
    if email==None:
        return render_template('mailform.html')
    else:
        return render_template('mailsample.html',email=email,name=name)

if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0')
    