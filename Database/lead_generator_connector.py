"""
This module contains funcitons related to mongodb and logic related to creating random test leads
"""
import sys
import os
from pymongo import MongoClient
from pymongo import UpdateOne
from bson.objectid import ObjectId


# Add the root directory to the Python path to access 'config'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Config.settings import MONGODB_URI, MONGODB_DB

def connect_to_mongodb():
    """This function contains the logic to connect to database"""
    # Use the MongoDB URI from the settings
    client = MongoClient(MONGODB_URI)
    # Access the specific database
    db = client[MONGODB_DB]
    return db

# def get_users_collection():
#     db = connect_to_mongodb()
#     return db['users']


def fetch_leads(leads_collection):
    """This function contains the logic to fetch leads from database"""
    leads = leads_collection.find(
        {
            "lead_type": {"$exists": False},  # Documents without 'lead_type'
            "outbound message": {
                "$exists": False
            },  # Documents without 'outbound message'
        }
    )
    leads_list = list(leads)
    return leads_list

def fetch_leads_for_user(leads_collection, user_id):
    """This function contains the logic to fetch leads from database"""
    leads = leads_collection.find(
        {
            "user_id": ObjectId(user_id),
            "lead_type": {"$exists": False},  # Documents without 'lead_type'
            "outbound message": {
                "$exists": False
            },  # Documents without 'outbound message'
        }
    )
    leads_list = list(leads)
    print(leads_list)
    print("printing in fetch leads for user funciton NEW")
    return leads_list

def fetch_agent_and_company_name(user_id):
    """This function contains the logic to fetch agent and company names from database"""
    database = connect_to_mongodb()
    users_collection = database["users"]
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    company_name = user["company_name"]
    agent_name = user["agent_name"]   
    print("fetching executive and company details")
    details = {"company_name": company_name, "agent_name": agent_name}
    return details


def update_user_with_token(user_id, token):

    database = connect_to_mongodb()
    users_collection = database["users"]

    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},  # Filter to match the lead's unique ID
        {"$set": {"gtoken": token.to_json()}},  # Update the google_token field
    )
    return result.raw_result



def update_leads(batch):
    "This function contains logic to update the leads in the database"
    database = connect_to_mongodb()
    leads_collection = database["leads"]

    # Create a list to hold update operations
    operations = []

    # Prepare the update operations for each lead
    for lead in batch:
        operation = UpdateOne(
            {"_id": lead["_id"]},  # Filter to match the lead's unique ID
            {
                "$set": {
                    "lead_type": lead["lead_type"],  # Set the lead_type field
                    "outbound message": lead[
                        "outbound message"
                    ],  # Set the outbound message field
                }
            },
        )
        operations.append(operation)  # Add the operation to the list

    # Perform the bulk write operation
    if operations:  # Check if there are operations to execute
        result = leads_collection.bulk_write(operations)
    else:
        result = None

    return result  # Return the result of the bulk write operation

def update_lead_with_form_data(user_id,frequency,company_name,agent_name):
    "This function contains logic to update the frequency in the database"
    database = connect_to_mongodb()
    user_collection = database["users"]

    # Perform the update operation
    result = user_collection.update_one(
        {"_id": ObjectId(user_id)},  # Filter to match the lead's unique ID
        {"$set": {"frequency": int(frequency), "company_name": str(company_name), "agent_name": str(agent_name)}},  # Update the frequency field
    )
    return result.raw_result

def create_leads(leads):
    database = connect_to_mongodb()
    leads_collection = database["leads"]

    result = leads_collection.insert_many(leads)

    return result.inserted_ids

def add_new_leads(leads_list,leads_collection):
    """This function contains the logic to add a new lead to the database"""

    for lead_dict in leads_list:
        lead_dict.setdefault("Initial contact", "No")
    # Insert the list of new leads into the 'leads' collection
    result = leads_collection.insert_many(leads_list)

    # Print the IDs of the inserted documents
    return result.inserted_ids


def delete_leads(lead_id_list):
    """This function contains the logic to delete leads in the database"""
    database = connect_to_mongodb()
    leads_collection = database["leads"]

    # Input all lead IDs in ObjectId format as below
    #[ObjectId('672df04fc86cdfbe0242d5e0'), ObjectId('672df04fc86cdfbe0242d5e1')]

    # Delete the leads with the specified IDs using $in operator
    result = leads_collection.delete_many({"_id": {"$in": lead_id_list}})

    # Check how many documents were deleted
    if result.deleted_count > 0:
        print(f"{result.deleted_count} leads have been deleted.")
    else:
        print("No leads found with the specified IDs.")
