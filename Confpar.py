import configparser, json, pymongo
from pymongo import MongoClient
from bson import ObjectId

# Function to read configuration from a file
def conf_file_read(file_name):
    conf = configparser.ConfigParser()  # Create a ConfigParser object to handle .ini files
    try:
        # Try reading the configuration file
        if not conf.read(file_name):
            # If file is not found, print message and exit
            print("File not found")
            exit(1)
    except Exception as f:
        # If there is any error while reading, print the error message and exit
        print("Error while reading file is", f)
        exit(1)
    return conf  # Return the loaded configuration object

# Function to read MongoDB URI from a file
def conf_file_mongo(file_name):
    conf_mongo = configparser.ConfigParser()  # Create a ConfigParser object for MongoDB URI
    try:
        # Try reading the MongoDB URI configuration file
        if not conf_mongo.read(file_name):
            # If file is not found, print message and exit
            print("Mongo connection File not found")
            exit(1)
        MONGO_URI = conf_mongo.get('MONGO', 'uri')  # Get the Mongo URI from the file under 'MONGO' section
    except Exception as f:
        # If there is any error while reading, print the error message and exit
        print("Error while reading Mongo URI file file is", f)
        exit(1)
    return MONGO_URI  # Return the Mongo URI

# Function to insert data into MongoDB
def insert_database(cf, MONGO_URI):
    try:
        # Connect to the MongoDB client using the provided URI
        myclient = pymongo.MongoClient(MONGO_URI)
        mydb = myclient["DB_Config"]  # Select the "DB_Config" database
        mycol = mydb["Config_par"]  # Select the "Config_par" collection
        
        # Insert the configuration data into MongoDB
        mycol.insert_one(cf)
    except Exception as e:
        # If there is an error during insertion, print the error message and exit
        print("The error while making inserting to mongo DB", e)
        exit(1)

# Function to fetch and display configuration data from MongoDB
def fetch_configuration(MONGO_URI):
    try:
        # Connect to MongoDB client using the provided URI
        myclient = pymongo.MongoClient(MONGO_URI)
        mydb = myclient["DB_Config"]
        mycol = mydb["Config_par"]
        
        # Fetch the first document from the collection
        ret = mycol.find_one()
    except Exception as e:
        # If there is an error during fetching, print the error message and exit
        print("The error while fetching data", e)
        exit(1)

    
    del ret['_id']

    # Iterate over the fetched configuration and print the key-value pairs
    for p_p, p_val in ret.items():
        print(p_p.strip(), ":")  # Print the parent section name
        if isinstance(p_val, dict):  # If the value is a dictionary, print its items
            for key, val in p_val.items():
                print("-", key.strip(), ":", val.strip())  # Print child key-value pairs

# Main execution block
if __name__ == '__main__':
    # Read the main configuration file
    conf = conf_file_read('Configuration.txt')
    
    # Read the MongoDB URI configuration file
    MONGO_URI = conf_file_mongo('Configuration_mongo.txt')
    
    cf = {}  # Dictionary to hold the configuration data
    
    # Iterate over each section in the configuration file
    for each_section in conf.sections():
        op1 = {}  # Temporary dictionary for each section's key-value pairs
        
        # For each section, get its key-value pairs and store them in op1
        for each_key, each_val in conf.items(each_section):
            op1[each_key] = each_val
        
        # Add the section and its key-value pairs to the final configuration dictionary
        cf[each_section] = op1
    
    # Insert the configuration data into MongoDB
    insert_database(cf, MONGO_URI)

    # Fetch and display the configuration from MongoDB
    fetch_configuration(MONGO_URI)

