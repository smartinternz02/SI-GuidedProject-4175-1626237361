from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
model=pickle.load(open('dtr.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/guest',methods=["post"])
def Guest():
    year=request.form["year"]
    month=request.form["month"]
    day=request.form["day"]
    data=[[year,month,day]]
    prediction=model.predict(data)
    prediction=prediction[0]
    return render_template("index.html",y="The Gas  price is "+str(prediction)) 
@app.route('/use ')
def user():
     return "hello user welcome"
if __name__=='__main__': #void main(){}
    app.run(debug=True) #create a local host url
 














