# mongo-upload-download
MongoDB Python Code

## Description
A simple python file that can be used to upload a local file to the local MongoDB service and in turn download the same file.

Effectively, this serves as a sanitary check to ascertain if MongoDB is running and if a database can be created and whether documents in the form of complete files can be uploaded and downloaded 

---

### C++ Installation 

1. Follow the instructions from http://mongocxx.org/mongocxx-v3/installation/linux/
2. Add the following line to your .bashrc file (if you are using a bash terminal) 
```echo "export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig" >> .bashrc```
3. Run the file as follows: ```c++ --std=c++11 mongo_download.cpp $(pkg-config --cflags --libs libmongocxx) -o mongo_download && ./mongo_download```