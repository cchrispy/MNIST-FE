from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder='web/templates',
    static_folder='web/static'
)


@app.route('/')
def ping():
    return render_template('index.html')

