#include <cstdint>
#include <iostream>
#include <vector>
#include <bsoncxx/json.hpp>
#include <mongocxx/client.hpp>
#include <mongocxx/stdx.hpp>
#include <mongocxx/uri.hpp>
#include <mongocxx/instance.hpp>
#include <bsoncxx/builder/stream/helpers.hpp>
#include <bsoncxx/builder/stream/document.hpp>
#include <bsoncxx/builder/stream/array.hpp>


using bsoncxx::builder::stream::close_array;
using bsoncxx::builder::stream::close_document;
using bsoncxx::builder::stream::document;
using bsoncxx::builder::stream::finalize;
using bsoncxx::builder::stream::open_array;
using bsoncxx::builder::stream::open_document;

int main(void) 
{
  mongocxx::instance instance{}; // This should be done only once.
  mongocxx::uri uri("mongodb://localhost:27017");
  mongocxx::client client(uri);
  
  std::cout << "This should create the database mydb inside of MongoDB" << std::endl;
  mongocxx::database db = client["grid_file"];
  mongocxx::collection coll = db["fs.files"];
             
  auto cursor = coll.find({}); //cursor store reference to document
             for(auto&& doc_val :cursor)
             {
                    std::cout<<bsoncxx::to_json(doc_val)<<std::endl; // not print as no document
                                                                     // is inserted
             }

        // Add a document to a collection. If the collection does not exist, make it
        using bsoncxx::builder::basic::kvp;
        using bsoncxx::builder::basic::make_array;
        using bsoncxx::builder::basic::make_document;
        
        
        mongocxx::database new_db = client["new_database"];
        new_db["new_collection"].insert_one(make_document(
            kvp("item", "canvas"),
            kvp("qty", 100),
            kvp("tags", make_array("cotton")),
            kvp("size", make_document(kvp("h", 28), kvp("w", 35.5), kvp("uom", "cm")))));
        // End Example 1


             std::cout<< "Datbase Created!" << std::endl;
             std::cout<< "Collection Created!" <<std::endl;

             return 0;
}
