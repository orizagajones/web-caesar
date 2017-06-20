from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

caesar_form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form method = "post">
                <label>Enter a Number</label>
                <input id="box1" type="text" name="rot">
                <input type="submit">

                <input id="box2" type="textarea" name="text">

            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return caesar_form

app.run()
