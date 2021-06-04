from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
   app.run(debug=True)