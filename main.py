from flask import Flask,render_template
import json
import os
import pathlib

BASE = pathlib.Path(__file__).parent

def get_json_data(key):
	with open(os.path.join(BASE,"config.json"),"r") as config_file:
		data = json.load(config_file)
		config_file.close()

	return data[key]

class App(Flask):
	def __init__(self,name):
		super(App,self).__init__(name)
		self.add_url_rule('/','index',self.index,methods=["GET","POST"])
		self.add_url_rule('/register','register',self.register,methods=["GET","POST"])
		self.add_url_rule('/login','login',self.login,methods=["GET","POST"])
	
	def index(self):
		return render_template("index.html")
		
	def register(self):
		return render_template("register.html")
	
	def login(self):
		return render_template("login.html")
		
	def run(self,host,port,debug=False):
		super().run(host=host,port=port,debug=debug)

if __name__ == "__main__":
	app = App(__name__)
	app.run(host='0.0.0.0',port=8000,debug=True)