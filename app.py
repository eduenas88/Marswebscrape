from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
#import scrape_mars

# Create an instance of Flask 
app = Flask(__name__)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_news_db
collection = db.newsheadlines

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable

    mars = list(collection.find())
    mars = mars[0]
    
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars= mars)

@app.route('/scrape')
def scrape(): 
    mars = db
    mars_info = scrape_mars.scrape()
    mars.update({}, mars_info, upsert=True)
    return redirect ('/')
    
    #db.collection.delete_many({})
    #db.collection.insert_one(mars_info)
if __name__ == "__main__":
    app.run(debug=True)
