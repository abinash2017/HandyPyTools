from pwcreate import get_password ,current_time
import pymssql
from colorama import Fore


def search_password():
    # Get list of all the application
    app_query = """select use_for_application from Passwords"""
    while True:
        result = cursor.execute(app_query)
        data_list = cursor.fetchall()
        print(data_list)
        print(Fore.CYAN + "Below are the password list" +Fore.RESET)
        for i in data_list:
            print(Fore.CYAN + "", i[0] ,""+Fore.RESET)
        old_apps = input(Fore.BLUE + "plaese write the app name from above list:\n" + Fore.RESET).strip()
            #get the password for specific application
        pwd_query= "select password_creation from Passwords where use_for_application = %s "
        cursor.execute(pwd_query, (old_apps,))
        get_apps = cursor.fetchone()
        print(Fore.GREEN + "password for " + old_apps + " is: " , get_apps[0] ,"" + Fore.RESET)
        # return old_password
        question2 = input(Fore.BLUE + "do you want to see any another password (yes/no):\n" + Fore.RESET).lower().strip()
        if question2 == "yes":
            continue
        else:
            break

def insert_password():
    app = input(Fore.BLUE + "Write the application/website you want to store your password:\n"+Fore.RESET).lower().strip()
    # query
    insert_query = """
    INSERT INTO Passwords (password_creation,time_created,use_for_application)
    VALUES (%s, %s, %s)
    """
    select_query = """
select * from Passwords;"""
    # Data to insert
    data = (f'{get_password(12)}', f'{current_time}', f'{app}')
    # Execute the insert query
    cursor.execute(insert_query, data)

    # Commit the transaction
    conn.commit()
    print(Fore.LIGHTGREEN_EX+"Data inserted successfully!"+Fore.RESET)
    cursor.execute(select_query)
    results = cursor.fetchall()
    for row in results:
        x = row
    print(Fore.GREEN + "your password is:", str(x) + Fore.RESET)

#main logic
# Establish a connection to the database
try: 
    conn = pymssql.connect(server='YOUR_SERVER_NAME',
                       user='YOUR_USERNAME',#Add user and password if needed, if it is a local server remove user , password
                       password='YOUR_PASSWORD',
                       database='YOUR_DATABASE_NAME')
    cursor = conn.cursor()
    choice = input(Fore.BLUE + "Hello, do you want see an old Password or create a new one?(newpwd/oldpwd):\n" + Fore.RESET).lower().strip()
    if choice == "newpwd":
        insert_password()
    elif choice == "oldpwd":
        search_password()
    else:
        print(Fore.RED + "Invalid choice. Exiting." + Fore.RESET)
except pymssql.Error as e:
    print(Fore.RED+"Error connecting to database:"+Fore.RESET, e )

finally:
    # Close the connection
    if conn:
        cursor.close()
        conn.close()