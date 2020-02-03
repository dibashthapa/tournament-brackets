from flask import *
import csv
import random
app=Flask(__name__)

Names=[]
RandomNames=[]
with open('file.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        Names.append(row[0])

@app.route("/")
def home():
    random.shuffle(Names)
    count=len(Names)
    return render_template("index.html",names=Names,count=count)
if __name__=='__main__':
    app.run(debug=True)
