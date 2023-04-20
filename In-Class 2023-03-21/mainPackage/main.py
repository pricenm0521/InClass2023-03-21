# main.py

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
# the above code creates a connection to the db, if no response then it works, if it doesn't it will crash
# below code is submitting a query to the sql server instance and stores the results in the cursor object

'''
cursor = conn.cursor()
cursor.execute("SELECT * FROM tAmericanAthleticConference")

total_enrollment = 0
# Step through all the rows in the results set
for row in cursor:
    print(row);     # All columns in the row
    print (row[1]); # Second column
    print (row[2]); # Third column
    print (row[3]); # Fourth column
    total_enrollment = total_enrollment + int(row[2])   # running sum of enrollments
    

print ("Total enrollment = " + str(total_enrollment))
'''
'''
cursor = conn.cursor()
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference') # better SQL syntax
for row in cursor:
    print(row.University)
'''
'''
# three ways to print only the schools that are private, one is cheating, never do it
cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
cursor.execute('SELECT University FROM tAmericanAthleticConference WHERE IsPrivate=1')
for row in cursor:
    print(row.University)
# example 2 
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')
for row in cursor:
    if row.IsPrivate == 1:
        print(row.University)
# example 3, very bad idea to hard code it
cursor.execute("SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference WHERE University = 'Tulane'")
for row in cursor:
    print(row.University)
'''
cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')
#for row in cursor:
#    print(row.University)

# The column names are case sensitive!
universities = [myRow.University.strip() for myRow in cursor.fetchall()]
print (universities)

# Need to re-read the data
# total enrollment of just the private schools please update below code
# original
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')    # Submit a query to the SQL Server instance and store the results in the cursor object
totalEnrollment = sum([int(myRow.Enrollment) for myRow in cursor.fetchall()])
print (totalEnrollment)
# private school enrollment
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference WHERE IsPrivate = 1')    # Submit a query to the SQL Server instance and store the results in the cursor object
totalEnrollment = sum([int(myRow.Enrollment) for myRow in cursor.fetchall()])
print (totalEnrollment)
# another example
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')    # Submit a query to the SQL Server instance and store the results in the cursor object
totalEnrollment = sum([int(myRow.Enrollment) for myRow in cursor.fetchall() if myRow.IsPrivate == 1])
print (totalEnrollment)

# print schools where enrollment is less than 50K in a set
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')  
enrollments = [int(myRow.Enrollment)
                for myRow in cursor.fetchall()
                if myRow.Enrollment < 50000]
# print(enrollments)
print(set(enrollments))
    