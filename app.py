import random 
from flask import Flask , render_template , request , redirect , url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/workouts')
def workouts():
    return render_template('workouts.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact_form', methods = ['POST'])
def submit_contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        return redirect(url_for('contact')) 

if __name__ == "__main__":
    app.run(debug=True)