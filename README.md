# Flask + redis integration
Playing with python flask

## Run
Manual: ```python src/main.py```<br>
VsCode: <em>just press F5</em>

## Endpoints
This example has two functional endpoints:<br>
Save value on redis: http://localhost/set?key=${your_key}&value=${your_value}<br>
Get value from redis: http://localhost/get?key=${your_key}<br>
