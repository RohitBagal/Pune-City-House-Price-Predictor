from flask import Flask , render_template,request
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db=SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    desc = db.Column(db.String(500))    
   
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def home():
    # if request.method=='POST':
    #     demo = 42
    #     area_type=1
    #     location=1
    #     area = int(request.form['area'])
    #     bedroom_count = int(request.form['bedroom_count'])
    #     bathroom_count = int(request.form['bathroom_count'])
    #     balcony_count = int(request.form['balcony_count'])

    #     input_values = [[bedroom_count,area,bathroom_count,balcony_count,location]]
    #     input_values = np.array(input_values)
    #     print(type(input_values))
    #     print(input_values)
    #     print(type(input_values[0,0]))
        
    #     predictions=model.predict(input_values) 
    #     print(predictions)

        
        
    return render_template('index.html')


@app.route('/predict',methods =['GET','POST'])
def predict():
    if request.method=='POST':
        demo = 42
        area_type=1
        location=1
        area = int(request.form['area'])
        bedroom_count = int(request.form['bedroom_count'])
        bathroom_count = int(request.form['bathroom_count'])
        balcony_count = int(request.form['balcony_count'])

        input_values = [[bedroom_count,area,bathroom_count,balcony_count,location]]
        input_values = np.array(input_values)
        # print(type(input_values))
        print(input_values)
        # print(type(input_values[0,0]))
        
        predictions=model.predict(input_values) 

        predictionsstr = np.array2string(predictions)
        # predictions = predictions.astype(str)
        # predictions = predictions.slice(2,2)
        #print(type(predictionsstr))
        # predictionsstr = predictionsstr[2:-7]
        # print(predictionsstr)

                

        
    return render_template('/predictor.html',pred='{}'.format(predictionsstr[2:-7]))
@app.route('/contact')
def about():
    return render_template('/contact.html')

@app.route('/predictor')
def predictor():
    return render_template('/predictor.html')

@app.route('/documentation')
def documentation():
    return render_template('/documentation.html')





if __name__=="__main__":
    app.run(debug=True)