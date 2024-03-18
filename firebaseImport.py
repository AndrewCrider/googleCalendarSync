import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

def import_json_to_firestore(json_array, collection_name):
    
    #TODO: Ensure that Service Account JSON files are in /config/googleJSON, change the below 
    #      definition to that file name
    # Initialize Firebase Admin SDKg
    cred = credentials.Certificate('config/googleJSON/firebase.json')
    firebase_admin.initialize_app(cred)

    # Get Firestore client
    db = firestore.client()

    for json_object in json_array:
        # Generate a new document ID
        doc_id = json_object.pop('id')
        doc_ref = db.collection(collection_name).document(doc_id)

        # Create or update the document with the generated ID
        doc_ref.set(json_object)
    
    print('Import successful!')


