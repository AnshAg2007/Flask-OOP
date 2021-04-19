from flask import Flask 

class App(Flask):
	def __init__(self,name):
		super().__init__(name)
		self.add_url_rule('/','index',self.index)
	
	def index(self):
		return "Hello World"
		
	def run(self,host,port,debug=False):
		super().run(host=host,port=port,debug=debug)

if __name__ == "__main__":
	app = App(__name__)
	app.run(debug=True,host='0.0.0.0',port=8000)