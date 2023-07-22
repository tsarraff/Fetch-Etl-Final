'''
This a Record class to hold the different attributes.
'''

class Record:
    def __init__(self, user_id, device_type, masked_ip,
                 masked_device_id, locale, app_version, create_date):
        self.user_id = user_id
        self.device_type = device_type
        self.masked_ip = masked_ip
        self.masked_device_id = masked_device_id
        self.locale = locale
        self.app_version = app_version
        self.create_date = create_date
        self.tuple = (self.user_id, self.device_type, self.masked_ip, self.masked_device_id, self.locale, self.app_version, self.create_date)

    def __repr__(self):
        return (
            f"Record("
            f"user_id='{self.user_id}', "
            f"device_type='{self.device_type}', "
            f"masked_ip='{self.masked_ip}', "
            f"masked_device_id='{self.masked_device_id}', "
            f"locale='{self.locale}', "
            f"app_version='{self.app_version}', "
            f"create_date='{self.create_date}'"
            f")"
        )