from flask import Flask, jsonify, render_template, request
from storage.mongodb import MongoStorage

app = Flask(__name__)
db = MongoStorage()

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/stats")
def stats():
    label_counts = db.collection.aggregate([
        {"$group": {"_id": "$label", "count": {"$sum": 1}}}
    ])
    data = {item["_id"]: item["count"] for item in label_counts}
    return jsonify(data)

@app.route("/api/posts")
def posts():
    keyword = request.args.get('keyword', '')
    query = {}
    if keyword:
        query["text"] = {"$regex": keyword}
    docs = db.find(query=query, limit=50)
    for d in docs:
        d['_id'] = str(d['_id'])
    return jsonify(docs)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
