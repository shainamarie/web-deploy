 import psycopg2
    try:
       connection = psycopg2.connect(user="postgres",
                                      password="password",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
       cursor = connection.cursor()
       
        def createuser(FNAME, LNAME):
            
            try:
                connection = psycopg2.connect(user="postgres",
                                            password="password",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="postgres_db")
                cursor = connection.cursor()
            
                postgres_insert_query = """ INSERT INTO mobile (USER_ID, FNAME, LNAME) VALUES (%s,%s,%s)"""
                record_to_insert = (1, 'Sample1', 'Sample2')
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
                count = cursor.rowcount
            print (count, "Record inserted successfully into mobile table")
            except (Exception, psycopg2.Error) as error :
                if(connection):
                    print("Failed to insert record into mobile table", error)
            finally:
                #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

        def updateuser(USER_ID)
            
            try:
                connection = psycopg2.connect(user="postgres",
                                            password="password",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="postgres_db")
                cursor = connection.cursor()

                print("Table Before updating record ")
                sql_select_query = """select * from mobile where id = %s"""
                cursor.execute(sql_select_query, (mobileId, ))
                record = cursor.fetchone()
                print(record)
                # Update single record now
                sql_update_query = """Update mobile set price = %s where id = %s"""
                cursor.execute(sql_update_query, (price, mobileId))
                connection.commit()
                count = cursor.rowcount
                print(count, "Record Updated successfully ")
                print("Table After updating record ")
                sql_select_query = """select * from mobile where id = %s"""
                cursor.execute(sql_select_query, (mobileId,))
                record = cursor.fetchone()
                print(record)
            except (Exception, psycopg2.Error) as error:
                print("Error in update operation", error)
            finally:
                # closing database connection.
                if (connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

        def deleteData(mobileId):
            try:
                connection = psycopg2.connect(user="postgres",
                                            password="password",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="postgres_db")
                cursor = connection.cursor()
                # Update single record now
                sql_delete_query = """Delete from mobile where id = %s"""
                cursor.execute(sql_delete_query, (mobileId, ))
                connection.commit()
                count = cursor.rowcount
                print(count, "Record deleted successfully ")
            except (Exception, psycopg2.Error) as error:
                print("Error in Delete operation", error)
            finally:
                # closing database connection.
                if (connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")