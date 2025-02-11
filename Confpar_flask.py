import configparser,json,pymongo
from pymongo import MongoClient
from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from bson import objectid

Confpar_flask = Flask(__name__)
Confpar_flask.config["MONGO_URI"] = "mongodb+srv://avinjaymewada25:1wKVfxoZizex5R2s@cluster0.k6qhq.mongodb.net/DB_Config"
pmdb=PyMongo(Confpar_flask)

def insert():
    conf = configparser.ConfigParser()
    conf.read('Configuration.txt')

        #dc = dict(conf.items('Section')) 
    #print(len(conf.sections()))

    cf = {}
    #op1 = {}
    for each_section in (conf.sections()):
        #sec[each_section]=each_section
        #cf[each_section]=each_section
        #for (each_key,each_val) in (
        #sec[each_section]=conf.options(each_section)
        op1 = {}
        for (each_key, each_val) in conf.items(each_section):
            op1 [each_key]=each_val

        cf[each_section]=op1

    #json_con=json.dumps(cf)
    #json_obj=json.loads(json_con)
    # json_obj=json.dumps(cf, indent=4)
    # print(json.dumps(cf, indent=4))

    myclient = pymongo.MongoClient("mongodb+srv://avinjaymewada25:1wKVfxoZizex5R2s@cluster0.k6qhq.mongodb.net/")
    mydb = myclient["DB_Config"]
    mycol = mydb["Config_par"]

    mycol.insert_one(cf)


insert()   

@Confpar_flask.route('/fetch',methods=["GET"])
def fetch():
    data=dict(pmdb.db.Config_par.find())
    return data



if __name__ == '__main__':
    Confpar_flask .run(debug=True,port=4009) 

#print(cf)