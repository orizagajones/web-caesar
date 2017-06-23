from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

caesar_form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action="/" method = 'POST'>
                <label>Rotate by:
                    <input type="text" name="rot">
                </label>
                <textarea id="txtArea" name="text">{0}</textarea>
                <label>
                    <input type="submit">
                </label>
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return caesar_form.format('')

@app.route("/", methods=['POST', 'GET'])
def encrypt():

    rot = int(request.form['rot'])
    text = request.form['text']
    message = rotate_string(text, rot)
    
    return caesar_form.format(message)


app.run()
