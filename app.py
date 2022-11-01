from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "slackUsername": "josee",
            "backend": True,
            "age": 21,
            "bio": "Joseph Ndungi and I am awesome"
        }
  
        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True)
