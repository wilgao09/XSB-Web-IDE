from flask import Flask, send_from_directory, Response

server = Flask(__name__)

# Send a file located in the presentation module when one is requested
@server.route("/<path:file>")
def generic_response(file):
	# The XSB Terminal library currently assumes all library files are at root.
	if "xsbInterface" in file or "xsbTerminal" in file :	# If a file from the xsbInterface or xsbTerminal is requested, then send it from ./src/modules/terminal. 
		if ".wasm" in file: # Manually send file with mimetype according to extension (Flask mimetype inference is bad)

			u = send_from_directory('./src/modules/terminal/', file, mimetype="application/wasm")
			u.headers.set('Cross-Origin-Opener-Policy','same-origin')
			u.headers.set('Cross-Origin-Embedder-Policy','require-corp')

			return u
		elif ".js" in file:
			u = send_from_directory('./src/modules/terminal/', file, mimetype="text/javascript")
			u.headers.set('Cross-Origin-Opener-Policy','same-origin')
			u.headers.set('Cross-Origin-Embedder-Policy','require-corp')
			
			return u
		u = send_from_directory('./src/modules/terminal/', file)
		u.headers.set('Cross-Origin-Opener-Policy','same-origin')
		u.headers.set('Cross-Origin-Embedder-Policy','require-corp')
		
		
		return u


	else:
		u= send_from_directory("./src/", file)
		u.headers.set('Cross-Origin-Opener-Policy','same-origin')
		u.headers.set('Cross-Origin-Embedder-Policy','require-corp')		
		

	
	return u

# Send main webpage when "/" url is queried by client
@server.route("/")
def home():
	u =  send_from_directory("./src/modules/presentation/", "index.html")
	
	u.headers.set('Cross-Origin-Opener-Policy','same-origin')
	u.headers.set('Cross-Origin-Embedder-Policy','require-corp')
	##u.headers.set('X-Content-Type-Options', 'nosniff')

	return u

# Start server on port 8000
server.run("localhost", "8000")