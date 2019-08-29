from flask import Flask, escape, request
from flask import send_file
from Graph.plot import Plot

app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello():
   print(request.method)
   req_data= request.get_json()
   print(req_data)
   name = request.args.get("name", "World")
   return f'Hello, {escape(name)}!'




@app.route('/get_image',methods=["POST"])
def get_image():
   
   req_data= request.get_json()
   plot= Plot()
   
   plot.labels_x=list(req_data["labels_x"])
   plot.labels_y=req_data["label_y"]
   plot.title=req_data["title"]
   plot.legend=list(req_data["legend"])
   plot.valueGroup1=list(req_data["valueGroup"][0])
   plot.valueGroup2=list(req_data["valueGroup"][1])
   plot.filename=req_data["filename"]
   if req_data["type"]=="1":
      plot.createGroupBarPlot()
   elif req_data["type"]=="2":
      plot.createPieChart()

   
   return send_file(req_data["filename"], mimetype='image/png')