import os

from first import app

if __name__ == "__main__":
	app.debug = True #make changes automatically in server
	host = os.environ.get("IP","0.0.0.0") #post in localhost
	port = int(os.environ.get("PORT", 8080))
	app.run(host=host, port=port)



