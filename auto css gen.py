from flask import Flask,render_template,request

app=Flask(__name__)


@app.route("/",methods=['POST','GET'])
def homepage():
    return render_template("homepage.html")

@app.route("/render",methods=['POST','GET'])
def render():
    return render_template("render.html")

@app.route("/render/colouredbox",methods=['POST','GET'])
def cbox():
    width,height,color,round,ele="","","","",""
    if request.method=="POST":
        width=request.form['width']
        height=request.form['height']
        color=request.form['color']
        round=request.form['round']  
        ele=request.form['ele']
    return render_template("colouredbox.html",width=width,height=height,color=color,round=round,ele=ele)

if __name__=="__main__":
    app.run(debug=True)

