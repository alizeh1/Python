#import pypyodbc

## Connection string including the database
#connection_string = 'Driver={SQL Server};Server=192.168.1.84;Database=Alisha_User;uid=sa;pwd=synergy@12'

#try:
#    # Establish a connection
#    connection = pypyodbc.connect(connection_string)

#    if connection:
#        print("Connected to MS SQL Server successfully")

#    # Optionally, you can execute a test query
#    cursor = connection.cursor()
#    # cursor.execute("SELECT 1")
#    # result = cursor.fetchone()
#    # print("Query result:", result)

#    # SQL Query
#    SQLCommand = ("INSERT INTO Employees(FirstName,LastName,Gender,Salary,DepartmentId) VALUES ('Sourabh','Patil','Male',25000,1)")
    
#    # Processing Query
#    cursor.execute(SQLCommand)
    
#    # Commit any pending transaction to the database
#    connection.commit()
    
#    # Closing connection
#    connection.close()
    
#    print("Data Successfully Inserted")

#except pypyodbc.Error as e:
#    print(f"Error: {str(e)}")


#***************************************************Another way**********************************************
##importing module  
#import pypyodbc  
##creating connection Object which will contain SQL Server Connection  
#connection = pypyodbc.connect('Driver={SQL Server};Server=192.168.1.84;Database=Alisha_User;uid=sa;pwd=synergy@12')  
##Creating Cursor  
#cursor = connection.cursor()   
##############Database Parameters##########  
#FirstName= "Akash"  
#LastName='Shinde'
#Gender='Male' 
#Salary=30000
#DepartmentId=1
###########################################  
  
##SQL Query  
#SQLCommand = ("INSERT INTO Employees(FirstName, LastName, Gender, Salary,DepartmentId) VALUES (?,?,?,?,?)")  
#Values = [FirstName,LastName,Gender,Salary,DepartmentId]  
  
##Processing Query  
#cursor.execute(SQLCommand,Values)   
##Commiting any pending transaction to the database.  
#connection.commit()  
##closing connection  
#connection.close()  
#print("Data Successfully Inserted")



#*****************************************Data read from user and inserted into the database********************************************

#importing module  
import pypyodbc  
#creating connection Object which will contain SQL Server Connection  
connection = pypyodbc.connect('Driver={SQL Server};Server=192.168.1.84;Database=Alisha_User;uid=sa;pwd=synergy@12')  
#Creating Cursor  
cursor = connection.cursor()   
#############Database Parameters##########  
#FirstName= input("Please Enter Name:")  
#LastName=input("Please Enter Last Name:")  
#Gender=input("Please Enter Gender:")  
#Salary=input("Please Enter salary:")  
#DepartmentId=input("Please Enter DepartmentId:")
###########################################  
  
##SQL Query  
#SQLCommand = ("INSERT INTO Employees(FirstName,LastName,Gender,Salary,DepartmentId) VALUES (?,?,?,?,?)")  
#Values = [FirstName,LastName,Gender,Salary,DepartmentId]  
  
##Processing Query  
#cursor.execute(SQLCommand,Values)   
##Commiting any pending transaction to the database.  
#connection.commit()  
##closing connection  
#connection.close()  
#print("Data Successfully Inserted")  

#*************************Update data*************************************
##SQL Query  
#SQLCommand = ("Update Employees set FirstName='Dhananjay' where Id=9")  
##Processing Query  
#cursor.execute(SQLCommand)   
##Commiting any pending transaction to the database.  
#connection.commit()  
##closing connection  
#connection.close()  
#print("Updated Successfully")  

#********************************Delete data**********************************
#SQL Query  
SQLCommand = ("Delete from Employees where Id=9")  
#Processing Query  
cursor.execute(SQLCommand)   
#Commiting any pending transaction to the database.  
connection.commit()  
#closing connection  
connection.close()  
print("Deleted Successfully") 




#*************************************End***************************
