from flask import (
	Flask,
	render_template,
	request,
	session,
	redirect,
	url_for
	)
import json
import psycopg2
import os
import pathlib

BASE = pathlib.Path(__file__).parent

class App(Flask):
	def __init__(self,name):
		super(App,self).__init__(name)
		self.config["SECRET_KEY"] = self.cfg("secret_key")
		self.pg_con = psycopg2.connect(
			dbname=self.cfg("db_name"),
			user=self.cfg("db_user"),
			password=self.cfg("db_pw"),
			host=self.cfg("db_host"),
			port=self.cfg("db_port")
			)
		self.pg_cur = self.pg_con.cursor()
		self.add_url_rule('/','index',self.index,methods=["GET","POST"])
		self.add_url_rule('/register','register',self.register,methods=["GET","POST"])
		self.add_url_rule('/login','login',self.login,methods=["GET","POST"])
	
	def cfg(self,key):
		with open(os.path.join(BASE,"config.json"),"r") as config_file:
			data = json.load(config_file)
			config_file.close()
		return data[key]
	
	def index(self):
		return render_template("index.html")
		
	def register(self):
		if request.method == "POST":
			name = request.form["username"]
			email = request.form["email"]
			pw = request.form["pw"]
			return redirect(url_for("index"))
			
		return render_template("register.html")
	
	def login(self):
		return render_template("login.html")
		
	def run(self,host,port,debug=False):
		super().run(host=host,port=port,debug=debug)

if __name__ == "__main__":
	app = App(__name__)
	app.run(host='0.0.0.0',port=8000,debug=True)