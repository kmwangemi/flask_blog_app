from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0e57e90e4b6d96d3792456ad07afd585'

posts = [
   {
      "author": "Corey Schafer", 
      "title": "First Post", 
      "content": "This is a post from a different user 1", 
      "date_posted": "April 20, 2018"
   }, 
   {
      "author": "Joyce Mayer", 
      "title": "Second Post", 
      "content": "This is a post from a different user 2", 
      "date_posted": "August 20, 2020"
   } 
]

@app.route("/")
@app.route("/home")
def home():
   return render_template('home.html', posts = posts)

@app.route("/about")
def about():
   return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      flash(f'Account created for {form.username.data}!', 'success')
      return redirect(url_for('home'))
   return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      if form.email.data == 'admin@gmail.com' and form.password.data == '123':
         flash('You have been logged in!', 'success')
         return redirect(url_for('home'))
      else:
         flash('Login unsuccessful, Please check username and password!', 'danger')
   return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
   app.run(debug=True)