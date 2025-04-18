# Serve a simple web page
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Return the dark theme HTML directly
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dark Theme Page</title>
        <style>
            body {
                background-color: #121212;
                color: #ffffff;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            h1 {
                color: #bb86fc;
            }
            a {
                color: #03dac6;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Welcome to the Dark Theme Page</h1>
            <p>This is a simple web page with a dark theme.</p>
            <p><a href="https://flask.palletsprojects.com/">Learn more about Flask</a></p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)