from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)
def write_to(data):
    with open('../database.txt', mode='a') as database :
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email,subject,message}')
def writeTo_csv(data):
    with open('database.csv', mode='a', newline ='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_witer  = csv.writer(database2, delimiter = ',',  quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_witer.writerow([email,subject,message])
@app.route('/submit_form',methods=['POST','GET'])
def login():
    if request.method=="POST":
        try:
            DATA = request.form.to_dict()
            writeTo_csv(DATA)
            return redirect('/thankyou.html')
        except:
            return "was not saved to the database"
    else:
        return "Something went wrong"


def home(page_name):
    return render_template(page_name)


if __name__ == '__main__':
    app.run()
