#!/usr/bin/env python3

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Welcome to my app!</h1>'

# @app.route('/<string:username>')
# def user(username):
#     return f'<h1>Profile for {username}</h1>'

# if __name__ == '__main__':
#     app.run(port=5555)

from flask import Flask

app = Flask(__name__)

# Your index() view should be routed to at the base URL with /. It should Contain 
# an h1 element that contains the title of this application, "Python Operations with
# Flask Routing and Views".
@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'


# A print_string view should take one parameter, a string. It should print the string
# in the console and display it in the web browser. Its URL should be of 
# the format /print/parameter.
@app.route('/print/<string:text>')
def print_string(text):
   print(text) # this will print the string in the console 
   return f'<p>Printed String: {text} </p>'

# A count() view should take one parameter, an integer. It should display all numbers 
# in the range of that parameter on separate lines. Its URL should be of the 
# format /count/parameter.
@app.route('/count/<int:num>')
def count(num):
    result = ''
    for num in range(num + 1):
        result += f'{num}\n'
    return result 

# A math() view should take three parameters: num1, operation, and num2. It must perform 
# the appropriate operation on the two numbers in the order that they are presented. The 
# included operations should be: +, -, *, div (/ would change the URL path), and %. Its 
# URL should be of the format /math/<num1><operation><num2>.
@app.route('/math/<int:num1><operation><int:num2>') 
def math(num1, operation, num2):
    # when writing this in the browser it will look sth like this 'http://127.0.0.1:5554/math/5-3'
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    
    return f'The result of {num1} {operation} {num2} is: {result}'
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
