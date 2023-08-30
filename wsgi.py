"""App entry point."""
from games import create_app
from flask import render_template

app = create_app()

app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)


