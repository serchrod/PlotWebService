# PlotWebService
Send type of graph you want and the data of each to return an image.

## Install Dependencies
``` 
pip install matplotlib
pip3 install flask
```

## Examples

You can test this api sending a request to the forward URL: http://127.0.0.1:5000/get_image
with this body as request

```javascript
{
	"type":"1",
	"labels_x":["Label 1","Label 2","Label 3","Label 4"],
	"label_y":"Data",
	"legend":["Label 1","Label 2"],
	"title":"Tittle",
	"filename":"graph.png",
	"valueGroup":[[6,7,8,3],[10,12,13,14]]
}
```
