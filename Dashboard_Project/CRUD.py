# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'CS340'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30328
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("connected!")

# Create method.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            print("Data was added to the database!")
            return True

        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Read method.
    def read(self, data):
        if data is not None:
                results = self.collection.find(data)
                #results list
                rList = list(())
                #Display each item that has been found
                for item in results:
                    #print("Found data: " + str(item["name"]))
                    rList.append(item)
                return rList
            #for testing...
                #print(rList)


        else:
            #No data as input, warn user
            raise Exception("No data was entered, try again!")
            return False
# Tuned Read Method
    def readNew(self, data):
        results = self.collection.find(data,{"_id":False})
        return results

# Update Method.
    def update(self, data, newData):
        if data is not None:
            #Perform update
            updated = self.collection.update_many(data, {"$set": newData})
            #Store count
            numUpdated = updated.modified_count
            print("Modified " + str(numUpdated) + " Items!")
            return numUpdated
        else:
            #No data as input, warn user
            raise Exception("No data was entered, try again!")
            return False
        
#Delete Method.        
    def delete(self, data):
        if data is not None:
            #Perform delete
            deleted = self.collection.delete_many(data)
            #Store count
            numDeleted = deleted.deleted_count
            print("Deleted " + str(numDeleted) + " Items!")
            return numDeleted
        else:
            #No data as input, warn user
            raise Exception("No data was entered, try again!")
            return False        

                
            

