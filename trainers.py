class Trainer:
    import sqlite3 #the database is called chinook.db. here we're calling sqlite
    import pandas as pd #import pandas which is a library which will allow us read the data in the database


    def __init__():
        connection = sqlite3.connect('computer-pride.db') #this is the database we try to connect to.
        pass



    #CRUD allows us to manipulate data. CRUD stands for Create Retrieve Update Delete
    def create(trainers): #use sql statement to create data for trainers table - we're inserting a trainer's info into the table. pass trainers as a parameter instead of hardcoding.
        sql = '''
            INSERT INTO trainers(id, name, gender) VALUES(?,?,?)
        '''
        
        cur = connection.cursor() #create cursor
        cur.execute(sql, trainers) #tell the cursor to execute something. pass sql statement 
        connection.commit()

        results = pd.read_sql("SELECT * FROM trainers", connection) #result in a variable. here trainers are going to be selected.
        print(results) #then they'll be displayed here

    def retrieveAll(): #retrieves all trainers
        pass

    def retrieveById(id): #specifies by id which trainer's data is to be retrieved.
        cur = connection.cursor() #create cursor
        cur.execute("SELECT id FROM trainers WHERE id="+str(id)) #tell the cursor to execute something. pass sql statement 

        results = cur.fetchall() # save data that's been selected in an object

        for x in results:
            print(x)

            
    def update(id, data): #allows us to udate this table where id is equal to the id that you're passing. pass the id because you need to know which trainer's info you're updating
        sql = 'UPDATE trainers SET name = ?, gender = ? where id = '+str(id)
        cur = connection.cursor() #create cursor
        cur.execute(sql, data) #tell the cursor to execute something. pass sql statement 
        connection.commit()

        results = pd.read_sql("SELECT * FROM trainers", connection) #result in a variable. here trainers are going to be selected.
        print(results) #then they'll be displayed here

    def delete(id): #you have to pass the id because you need to know which one you're deleting
        sql = 'DELETE FROM trainers where id = '+str(id)
        cur = connection.cursor() #create cursor
        cur.execute(sql) #tell the cursor to execute something. pass sql statement 
        connection.commit()

        results = pd.read_sql("SELECT * FROM trainers", connection) #result in a variable. here trainers are going to be selected.
        print(results) #then they'll be displayed here

    #createTables()
    #create((3,'Tomashi', 'M')) #call the function and pass the trainer's info.

    #update(3, ("Maggy", "F")) #call the function and pass the id to know which trainer you're changing.

    #delete(3) #call the function and pass id parameter

    retrieveAll(3)