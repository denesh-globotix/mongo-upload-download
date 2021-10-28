#! /usr/bin/python3 
from pymongo import MongoClient 
import gridfs

print("Starting connection to MongoDB")

# MongoDB connection function
def mongo_conn():
    try:  
        conn = MongoClient(host='127.0.0.1', port=27017)
        print("MongoDB connected", conn)
        return conn.grid_file
    except Exception as e: 
        print("Error in MongoDB connection:", e)

# Call the MongoDB function
db = mongo_conn()

print("Upload file")
name ='state_estimation.pdf'
file_location = "/home/globotix/Downloads/" + name
file_data = open(file_location, "rb")
data = file_data.read()
fs = gridfs.GridFS(db)
fs.put(data, filename = name)
print("upload completed")

data = db.fs.files.find_one({'filename':name})
my_id = data['_id']
outputdata = fs.get(my_id).read()
download_location = "/home/globotix/Desktop/" + name
output = open(download_location, "wb")
output.write(outputdata)
output.close()
print("download completed")

print("Uploading bag file. I will be stuck here if service is not started")
name ='bag_file.bag'
file_location = "/home/globotix/Downloads/" + name
file_data = open(file_location, "rb")
data = file_data.read()
fs = gridfs.GridFS(db)
fs.put(data, filename = name)
print("upload completed")

data = db.fs.files.find_one({'filename':name})
my_id = data['_id']
outputdata = fs.get(my_id).read()
download_location = "/home/globotix/Desktop/" + name
output = open(download_location, "wb")
output.write(outputdata)
output.close()
print("download completed")