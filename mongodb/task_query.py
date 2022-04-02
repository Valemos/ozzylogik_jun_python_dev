from connection import *


if __name__ == '__main__':
    selected = database["random_strings"].aggregate([
        {"$project": {"first_letter": {"$substrCP": ["$s2", 0, 1]}}},
        {"$match": {"first_letter": {"$regex": "[a-zA-Z]"}}},
        {"$unset": "first_letter"}
    ])

    for doc in selected:
        id_to_delete = doc["_id"]
        database["random_strings"].delete_one({"_id": id_to_delete})
        print(id_to_delete, "deleted")
