"""
Flask Web Application Module

This module imports essential components from the Flask framework for building web applications.
Attributes:
    - Flask: The main Flask class representing the web application.
    - render_template: A function for rendering HTML templates in response to requests.
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the index page.

    Handles both GET and POST requests and renders the 'index.html' template.
    """
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Render the contact page.

    Handles both GET and POST requests and renders the 'contact.html' template.
    """
    return render_template('contact.html')

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    """Render the projects page.

    Handles both GET and POST requests and renders the 'projects.html' template.
    """
    return render_template('projects.html')

@app.route('/CV', methods=['GET', 'POST'])
def cv():
    """Render the CV (resume) page.

    Handles both GET and POST requests and renders the 'resume.html' template.
    """
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)
