import mysql.connector      

class myClass:
     
    def fun(self):  
        conn = mysql.connector.connect(host="localhost",port='3306',user="root",password="",database="healthyhead")    
        cursor=conn.cursor()        

        selectquery = "select name, email from healthyhead"    

        cursor.execute(selectquery)
        records= cursor.fetchall()      
        row=[str(records)]              
        with  open("maintext.txt", "w") as f: 
            d= f.write(str(row))
        with open("maintext.txt","r") as e:     
            f= e.read(d)
            print(f)
            return f
