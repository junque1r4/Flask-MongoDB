from flask import Flask, make_response
from flask_mongoengine import MongoEngine


app=Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'USERS',
    'host': 'localhost',
    'port': 27017
}

db=MongoEngine()
db.init_app(app)

class User(db.Document):
    user_id= db.IntField()
    user_name=db.StringField()
    user_bio=db.StringField()

    def to_json(self):
        #convert this document to JSON
        return {
            "user_id" : self.user_id,
            "user_name" : self.user_name,
            "user_bio" : self.user_bio
        }

@app.route("/USERS/db_populate",methods=['POST'])
def db_populate():
    user1=User(user_id=1,user_name="Marco", user_bio="Hi!")
    user2=User(user_id=2,user_name="Francesca", user_bio="What a weird program!")
    user1.save()
    user2.save()
    return make_response("",201)

@app.route("/Users/user",methods=['Get','POST'])
def users():
    pass

@app.route("/Users/user/<user_id>",methods=['GET','PUT',"DELETE"])
def single_user():
    pass

if __name__ == '__main__' :
    app.run(debug=True)