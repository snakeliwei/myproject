# -*- coding: utf-8 -*-
# file: pgconn.py
# author: Lyndon

import psycopg2
import uuid
import datetime


# 数据库连接参数
conn = psycopg2.connect(database="giant_test",
                        user="bestone",
                        password="q4V*t5YWwRtq92G&^nRDQE34",
                        host="127.0.0.1",
                        port="5432")
cur = conn.cursor()

user_id = str(uuid.uuid1())

# insert a user
cur.execute("INSERT INTO users (email, encrypted_password, uuid, name, home_name, address, description, qq, logo_photo_id, mobile, sex, birthday, default_logo, temp_token, temp_token_at, authentication_token, token_expiry, reset_password_token, reset_password_sent_at, remember_created_at, sign_in_count, current_sign_in_at, last_sign_in_at, current_sign_in_ip, last_sign_in_ip, confirmation_token, confirmed_at, confirmation_sent_at, unconfirmed_email, created_at, updated_at, name_public, qq_public, email_public, mobile_public, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ('', '$2a$10$pzj7EfuUUCfHiNrLekCE/.6iav8r12H8i7Nwyz7Ns7HwZTD2Ibus.', user_id, None, '18086688888', None, None, None, None, '18086688888', None, None, '/assets/1.jpg', None, None, None, datetime.datetime.now(), None, None, None, '0', None, None, None, None, None, None, datetime.datetime.now(), None, datetime.datetime.now(), datetime.datetime.now(), None, None, None, None, 'enabled'))

conn.commit()
cur.close()
conn.close()
