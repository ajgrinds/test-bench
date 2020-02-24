from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def web():
    return "Web server online"


@app.route('/input')
def render():
    if 'filename' in request.args:
        myfilename = request.args.get('filename')
        return render_template(myfilename)
    else:
        return "No input file specified"


@app.route('/ping')
def ping():
    print(request.remote_addr)
    return "Printed IP"


if __name__ == '__main__':
    app.run(debug=True)
