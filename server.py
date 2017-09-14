from flask import Flask, render_template, request, redirect
app = Flask(__name__, static_url_path='/static/')

@app.route("/")
def index():
  return app.send_static_file('index.html')

@app.route("/edit")
def edit():
  f = open("static/index.html", "r")
  return render_template('edit.html', content=f.read())

@app.route("/update")
def update():
  content = request.args.get('content')
  f = open("static/index.html", "w")
  f.write(content)
  return redirect('/')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4545)
