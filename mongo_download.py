#! /usr/bin/python3 
from pymongo import MongoClient 
import gridfs
import os

# These are all the names of the files
files = ['state_estimation.pdf', 'bag_file.bag']

def add_line():
    print('-' * 100)

def upload(name):
    add_line()
    file_location = "/home/globotix/Downloads/" + name
    file_data = open(file_location, "rb")
    data = file_data.read()
    fs = gridfs.GridFS(db)
    fs.put(data, filename = name)
    print("uploading of {} completed".format(name))

def download(name):
    data = db.fs.files.find_one({'filename':name})
    my_id = data['_id']

    fs = gridfs.GridFS(db)
    outputdata = fs.get(my_id).read()
    download_location = "/home/globotix/Desktop/" + name
    output = open(download_location, "wb")
    output.write(outputdata)
    output.close()
    print("downloading of {} to the desktop is complete".format(name))

# MongoDB connection function
def mongo_conn():
    try:  
        conn = MongoClient(host='127.0.0.1', port=27017)
        print("MongoDB connected with the following information: ", conn)
        return conn.grid_file
    except Exception as e: 
        print("Error in MongoDB connection:", e)

if __name__ == "__main__":
    print('''
    ---------------------------------
    |                                |
    |                                |
    | Starting connection to MongoDB |
    |                                |
    |                                |
    ----------------------------------
    ''')
    print('''
    Will be uploading the following files from the Downloads folder
            
            1) {}
            2) {}

    and downloading them into the Desktop folder. If you have 2 new 
    files in desktop. Then this worked gracefully. Congrats!
        '''.format(files[0], files[1]))

    print("-" * 100)

    # Call the MongoDB function
    db = mongo_conn()

    for file in files:
        upload(file)
        download(file)

    add_line()
    print('''
    ---------------------------------
    |                                |
    |                                |
    |  All processes are complete    |
    |                                |
    |                                |
    ----------------------------------
    ''')