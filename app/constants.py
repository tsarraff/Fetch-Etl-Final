query = 'INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES %s';
queue_url = 'http://localhost:4566/000000000000/login-queue'