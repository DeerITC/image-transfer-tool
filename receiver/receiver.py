from flask import Flask , request , jsonify
app = Flask(__name__)
@app.route('/data_receiver', methods=["GET","POST"]) #data receiver is my endpoint, the function needs to have the same name
def data_receiver():
   if request.method=="GET":
       Name=request.args.get("Name") #new variable i'm telling the program to take the value from the "Name" coulnb defined in the r_get in sender
       return jsonify({"method": "GET", "Name": Name})
   elif request.method=="POST":
       data=request.json #this object contains variables (the names i wrote)
       return jsonify({"method": 'POST', "Name" : data.get("Name")})
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080) #if this application was running in the main then run the app (host is my device, 0000 becuase it allows everything)