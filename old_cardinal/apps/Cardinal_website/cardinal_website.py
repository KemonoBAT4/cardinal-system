from flask import Flask
from flask import render_template

app = Flask(__name__)
template_name = "cardinal_website.html" # cardinal website template name


@app.route('/')
def home():
    render_template(template_name)

app.run(host='0.0.0.0', debug=True)
