import time
import random

from flask import Flask

app = Flask(__name__)

def random_line(fname):
   lines = open(fname).read().splitlines()
   return random.choice(lines)

@app.route('/')
def hello(): 
   random_name = random_line('list_dir/list') 
   return "Random: {} \n".format(random_name)
   
if __name__ == "__main__": 
   app.run(host="0.0.0.0", port=8080, debug=True)
