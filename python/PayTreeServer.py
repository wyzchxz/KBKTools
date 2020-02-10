from flask import Flask
app = Flask(__name__)

filedic = {'get':'get.json','confirm':'conf.json',}

@app.route('/paytree/get/<type>/<imiwakarann>/')
def bbb(type,imiwakarann):
    with open(filedic[type],'r', encoding="utf-8") as theJson:
        return eval("".join(theJson.readlines()))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)