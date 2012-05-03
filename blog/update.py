#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import config
import model


if __name__ == "__main__":
    cursor=model.sql()
    cursor.execute("alter table site add column (modsite INT,modmsg text)")
    cursor.execute("UPDATE site SET modsite=1,modmsg=''")
    cursor.close()
    raw_input('Been completed successfully update the database,Press the enter for exit.')
