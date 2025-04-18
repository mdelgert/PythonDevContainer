from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML from the templates directory
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)