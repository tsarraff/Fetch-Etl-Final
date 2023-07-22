import hashlib
from datetime import datetime


'''
This fumction will mask the ip and device id. Then it will create a dictionary with the new values and return it. 
'''
def pii_mask(data):
    user_id = data.get("user_id")
    device_type = data.get("device_type")
    ip = data.get("ip")
    device_id = data.get("device_id", "unknown")
    locale = data.get("locale", "unknown")
    app_version = data.get("app_version")
    create_date = datetime.now()


    if ip:

        ip_masked = hashlib.sha256(ip.encode("utf-8")).hexdigest()
        device_id_masked = hashlib.sha256(device_id.encode("utf-8")).hexdigest()


        res_dic = {
            "user_id": user_id,
            "device_type": device_type,
            "masked_ip": ip_masked,
            "masked_device_id": device_id_masked,
            "locale": locale,
            "app_version": app_version,
            "create_date":create_date
        }

        return res_dic
    else:
        return None
