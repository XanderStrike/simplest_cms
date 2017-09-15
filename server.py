from flask import Flask, render_template, request, redirect
import os, bcrypt

app = Flask(__name__)

salt = ''
if os.path.isfile("data/salt"):
  salt = open("data/salt", "r").read()
else:
  salt = bcrypt.gensalt()
  open("data/salt", "w").write(salt)

@app.route("/")
def index():
  if os.path.isfile("data/index.html"):
    return open("data/index.html", "r").read()
  else:
    return redirect("/setup")

@app.route("/edit")
def edit():
  if os.path.isfile("data/index.html"):
    f = open("data/index.html", "r")
    return render_template("edit.html", content=f.read())
  else:
    return redirect("/setup")

@app.route("/setup")
def setup():
  if os.path.isfile("data/index.html"):
    return redirect("/")
  else:
    return render_template("setup.html")

@app.route("/update")
def update():
  if os.path.isfile("data/password") and open("data/password", "r").read() != bcrypt.hashpw(request.args.get("password").encode('utf-8'), salt):
    return redirect("/")

  newpass = request.args.get("newpassword")
  if newpass and newpass != '':
    hashed = bcrypt.hashpw(request.args.get("newpassword").encode('utf-8'), salt)
    open("data/password", "w").write(hashed)

  content = request.args.get("content")
  f = open("data/index.html", "w")
  f.write(content)
  return redirect("/")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4545)
