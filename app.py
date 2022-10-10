from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/main')
def index():
    return render_template('main.html')

@app.route('/gauges')
def app_page():
    return render_template('gauges.html')



@app.route('/receive_data', methods=['GET', 'POST'])
def app_page1():
    print("Data received!")
    print(request.data)
    return "200"


if __name__ == '__main__':
    app.run('0.0.0.0',port=83,debug=True)
