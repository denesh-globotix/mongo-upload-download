#! /usr/bin/python3
from pymongo import MongoClient

# Create a class because classes are awesome
class PathUploader():
    def __init__(self):

        # Call the MongoDB function
        self.db = self.mongo_conn()

        # Define a ROS Service
        rospy.Service('upload_path_to_MongoDB', LoadGoal, self.uploadPath)
    
    def uploadPath(self, req):
        print(req.path)
        return []

    def create(self):
        # Access the collection
        post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"]}

        # Insert the above post into the zones document
        collection = self.db["books"]
        collection.insert_one((post))

    def read(self):
        collection = self.db["books"]
        cursor = collection.find({})
        for document in cursor:
          print(document)


    def update(self):
        collection = self.db["books"]
        collection.update_one({'author': "Mike"}, {"$set": {"path": "put some fancy path here"}}, upsert=False)
        return

    def delete(self):
        collection = self.db["books"]
        collection.delete_one({ "author": "Mike" })
        return

    # Returns a MongoDB connection object to the database: zones
    def mongo_conn(self):
        try:
            conn = MongoClient(host='127.0.0.1', port=27017)
            rospy.loginfo("MongoDB connected with the following information: {}".format(conn))
            return conn.zones
        except Exception as e:
            rospy.loginfo("Error in MongoDB connection: {}".format(e))
            return None


if __name__ == "__main__":
    # Start an instance of the class
    path_uploader = PathUploader()
    path_uploader.delete()
