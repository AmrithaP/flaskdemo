## Flask App routing

from flask import Flask, render_template, request, redirect, url_for, jsonify

## create a simple Flask application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
  return "<h1>Welcome to Amritha's Home page</h1>"

@app.route("/index",methods =["GET"])
def index():
  return "<h2>Welcome to Index page</h2>"

# VARIABLE RULE
@app.route("/success/<int:score>") # score = parameter , no methods sent then by default - GET
def success(score):
  return "The person has passed the exam and the score is : "+ str(score)

@app.route("/fail/<int:score>") # score = parameter , no methods sent then by default - GET
def fail(score):
  return "The person has failed the exam and the score is : "+ str(score)

# Display HTML content
@app.route('/form',methods=["GET","POST"])
def form():
  if request.method == "GET":
    return render_template('form.html')
  else:
    maths = float(request.form['maths'])
    science = float(request.form['science'])
    history = float(request.form['history'])

    average_marks = (maths + science + history)/3
    result = ""
    if average_marks >=50:
      result = "success"
    else:
      result = "fail"

    return redirect(url_for(result,score=average_marks))
    #return render_template('form.html', score = average_marks)


# Create API IN FLASK
@app.route('/api', methods =['POST'])
def calculate_sum():
  data = request.get_json()
  a_val = float(dict(data)['a'])
  b_val = float(dict(data)['b'])
  return jsonify(a_val + b_val)



if __name__ =="__main__":
  app.run(debug=True) # default url = localhost and port = 5000
  