from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        df = pd.read_table(file,
                           skiprows=0,
                           delim_whitespace=True,
                           names=['x', 'y', 'elevation'])
        print(df)
        return print(df)


if __name__=='__main__':
    app.run(debug=True)