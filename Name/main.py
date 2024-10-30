from flask import Flask , render_template

App = Flask(__name__)

@App.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    App.run(debug=True)


