# -*- coding: utf-8 -*-
# file: userInsert.py
# author: Lyndon

import psycopg2
import uuid
import datetime


class userInsert(object):

    def __init__(self):
        """initial connect data"""
        self.conn = psycopg2.connect(database="giant_product", user="bestone",
                                     password="q4V*t5YWwRtq92G&^nRDQE34",
                                     host="127.0.0.1",
                                     port="5432")

    def insertData(self, userData):
        """insert user data"""

        cur = self.conn.cursor()
        data = userData

        for user in data:
            # insert a user
            user_uuid = str(uuid.uuid1())
            if user['name'] != '':
                user_name = user['name']
            else:
                user_name = user['mobile']
            cur.execute("INSERT INTO users (email, encrypted_password, uuid, name, home_name, address, description, qq, logo_photo_id, mobile, sex, birthday, default_logo, temp_token, temp_token_at, authentication_token, token_expiry, reset_password_token, reset_password_sent_at, remember_created_at, sign_in_count, current_sign_in_at, last_sign_in_at, current_sign_in_ip, last_sign_in_ip, confirmation_token, confirmed_at, confirmation_sent_at, unconfirmed_email, created_at, updated_at, name_public, qq_public, email_public, mobile_public, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (user['email'], '$2a$10$sD8Xb8SqlGyLOru1MzC3COLR3Bw8OEl06b1BG4bi6HxBzDtvD7RfS', user_uuid, None, user_name, user['address'], None, None, None, user['mobile'], None, None, '/assets/1.jpg', None, None, None, datetime.datetime.now(), None, None, None, '0', None, None, None, None, None, None, datetime.datetime.now(), None, datetime.datetime.now(), datetime.datetime.now(), None, None, None, None, 'enabled'))

            self.conn.commit()

            cur.execute("SELECT id FROM users where mobile = %s;",
                        (user['mobile'], ))
            user_id = cur.fetchall()[0][0]

            cur.execute("SELECT max(position) FROM galleries;")
            user_position = cur.fetchall()[0][0] + 1

            cur.execute("INSERT INTO galleries (name, clazz, parent_id, position, class_id, owner_id, owner_type, cluster_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        ('新上传', 'user_root', '0', user_position, None, user_id, 'User', None, datetime.datetime.now(), datetime.datetime.now()))
            self.conn.commit()

        self.conn.close()

if __name__ == '__main__':
    # userdata = userInsert()
    # data =
    # userdata.insertData(data)
    pass
