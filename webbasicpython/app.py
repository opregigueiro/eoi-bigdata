import socket
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello(): 
   ctrname = socket.gethostname() 
   return "ID del contenedor: {} \n".format(ctrname)
   
if __name__ == "__main__": 
   app.run(host="0.0.0.0", port=8080, debug=True)
