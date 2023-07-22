from record import Record
import json
from piiMasking import pii_mask


'''
This function will create a Record object that will be used when adding to the database.
'''
def create_record(data):
    if data:
        version = data["app_version"].replace(".", "")
        version = int(version)

        return Record(user_id = data['user_id'],
            device_type = data['device_type'],
            masked_ip = data['masked_ip'],
            masked_device_id = data['masked_device_id'],
            locale = data['locale'],
            app_version = version,
            create_date = data['create_date'])
    else:
        return None
    

'''
This function will create a list of record objects that will be used when adding to the database.
'''
def create_record_objects(messages):
    records = []

    for m in messages:
        data = json.loads(m["Body"])
        masked_data = pii_mask(data)

        record = create_record(masked_data)

        if record:
            records.append(record)

    return records