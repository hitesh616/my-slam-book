from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def my_form():
     return render_template('first.html')


@app.route('/info', methods =["GET", "POST"])
def my_app():         
     if request.method == "POST":
#       form_data = request.form

#       return render_template('second.html', form_data = form_data)


       firstname = request.form.get('fname')
       lastname = request.form.get('lname')
       gender = request.form.get('gender')
       birthday = request.form.get('birthday')
       photo = request.form.get('file')

       return render_template('second.html', firstname=firstname, lastname=lastname, gender=gender, birthday=birthday, photo=photo)

#       return "your first name is "+ firstname +" last name is "+ lastname +" and you are a "+ gender + " and your birthday is on " + birthday
     return render_template('first.html')
app.run(debug=True)
