import psycopg2 as a

#create connection
conn=None
conn=a.connect(database= "minibank",user= "postgres",password= "1122",host= "localhost",port= "5432")
print("connected to database")

def Caccount():
    user=input("Enter User Id--\n")
    passw=input("Enter Password--\n")
    if user=="7890" and passw=="Nayak@123":
        print("USER LOGIN SUCCESSFULLY")
        w=0
        name=input("Enter customer name:\n")
        accno=input("Enter Account Number:\n")
        dob=input("Enter Date of Birth:\n")
        address=input("Enter Address:\n")
        phone_no=input("Enter customer phone number:\n")
        nominee_Name=input("Enter Nominee Name:\n")
        nominee_dob = input("Enter Nominee dob:\n")
        relation_with_nominee=input("Enter relation:\n")
        ob=int(input("Enter Account Opening balance:\n"))
        ac_op_d=input("Enter account opening date:\n")
        pincode=input("Enter Pincode:\n")
        query1="insert into account values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data1=(name,accno,dob,address,phone_no,ob,nominee_Name,nominee_dob,relation_with_nominee,ac_op_d,pincode)
        query2="insert into amount values (%s,%s,%s)"
        data2=(name,accno,ob)
        query3="insert into miniStatement values(%s,%s,%s,%s)"
        data3=(accno,ob,w,ac_op_d)
        #create cursor
        c=conn.cursor()
        c.execute(query1,data1)
        c.execute(query2,data2)
        c.execute(query3,data3)
        conn.commit()
        print(">--------------------------------------<")
        print("Data Entered Successfully")
        print("Account Created Successfully")
        print("Your Account_No is---",accno)
    else:
        print("Invalid User_Id or Password")


def deAmount():

    wi=0
    de=int(input("Enter Amount which you want to deposit:\n"))
    ac=input("Enter Account Number:\n")
    date=input("Enter Date:\n")
    query1="select balance from amount where accountno=%s"
    data1=(ac,)
    #create cursor
    c=conn.cursor()
    c.execute(query1,data1)
    myresult=c.fetchone()
    t=myresult[0]+de
    query2="update amount set balance=%s where accountno=%s"
    data2=(t,ac)
    c.execute(query2,data2)
    conn.commit()
    queryy3="Insert into miniStatement values(%s,%s,%s,%s)"
    data3=(ac,de,wi,date)
    c=conn.cursor()
    c.execute(queryy3,data3)
    conn.commit()
    print(">-----------------------------<")
    print("Your Amount-----" ,de,"Deposited successfully in your AccountNo----",ac)

    main()

def withdrawAm():
    userid = input("Enter User Id:\n")
    passw = input("Enter Password:\n")
    if userid == "Amres1100" and passw == "Am0011":
        print("LOgin Successfully")
        de=0
        ac=input("enter Account Number:\n")
        am=int(input("Enter Amount Which you want to Withdraw:\n"))
        date=input("Enter Date:\n")
        quer1="select balance from amount where accountno=%s"
        data=(ac,)
        #create cursor
        c=conn.cursor()
        c.execute(quer1,data)
        myresult=c.fetchone()
        t=myresult[0]-am
        query2="update amount set balance=%s where accountno=%s"
        data2=(t,ac)
        c.execute(query2,data2)
        conn.commit()
        query4 ="Insert into ministatement values(%s,%s,%s,%s)"
        data4 =(ac, de, am, date)
        c=conn.cursor()
        c.execute(query4,data4)
        conn.commit()
        print("your amount",am,"Withdrawn Successfully")
    else:
        print("Invalid User_Id or Password")

    main()

def balanceInquiry():
    ac=input("Enter Account Number:\n")

    query1="select balance,name from amount where accountno=%s"
    data=(ac,)  #we create tuple for accessing index
    #create curor
    c=conn.cursor()
    c.execute(query1,data)#
    #print(c)it return cursor object
    myr=c.fetchone()
    i=myr[0]
    j=myr[1]
    print("Your AccountNo----",ac)
    print("A/c Holder Name----",j)
    print("Your Current Balance is",i)

def dah():
    ac=input("Enter Account Number:\n")
    query1="select name,accountno,dob,address,phoneno,accopeningdate,pincode from account where accountno=%s"
    data=(ac,)
    c=conn.cursor()
    c.execute(query1,data)
    my=c.fetchone()
    print(my)
    print(my[0])
    print(my[1])
    print(my[2])
    print(my[3])
    print(my[4])
    print(my[5])
    print(my[6])

def miniState():
    ac=input("Enter Account Number:\n")
    query1="select * from ministatement where account_no=%s"
    data=(ac,)
    #create cursor
    c=conn.cursor()
    c.execute(query1,data)
    my=c.fetchall()
    for i in my:
        print(i[0],i[1],i[2],i[3])

    main()

def FundTransfer():
    o=0
    x=0
    ac=input("Enter Your Account Number:\n")
    w=int(input("Enter Amount which you want to Transfer:\n"))
    date=input("Enter Date:\n")
    ban=input("Enter Benificiary A/c No:\n")
    am=int(input("Enter Transfer Amount:\n"))
    query1="select balance from amount where accountno=%s"
    data=(ac,)
    c=conn.cursor()
    c.execute(query1,data)
    my=c.fetchone()
    t=my[0]-w
    query2="update amount set balance=%s where accountno=%s"
    data2=(t,ac)
    c.execute(query2,data2)
    conn.commit()

    query3="select balance from amount where accountno=%s"
    data3=(ban,)
    c.execute(query3,data3)
    v=c.fetchone()
    u=v[0]+am
    query7="update amount set balance=%s where accountno=%s"
    data7=(u,ban)
    c.execute(query7,data7)
    conn.commit()

#execute statement code

    query4="insert into ministatement values(%s,%s,%s,%s)"
    data4=(ac,o,w,date)
    c=conn.cursor()
    c.execute(query4,data4)
    conn.commit()

    query5="insert into ministatement values(%s,%s,%s,%s)"
    data5=(ban,am,x,date)
    c=conn.cursor()
    c.execute(query5,data5)
    conn.commit()
    print("Transaction Successful")
    query10="select balance from amount where accountno=%s"
    data8=(ac,)
    c=conn.cursor()
    c.execute(query10,data8)
    aso=c.fetchone()
    print(" your current balance is",aso[0])

def deleteAc():
    print(">-------LOG IN WINDOW----------<")
    userid=input("Enter userId:\n")
    passw=input("Enter Password:\n")
    if userid=="Amres1100" and passw=="Am0011":
        print("Login successfully")
        ac=input("Enter Account_no which you want to Delete:\n")
        qu="delete from account where accountno=%s"
        data9=(ac,)
        c=conn.cursor()
        c.execute(qu,data9)
        conn.commit()
        print("Account Deleted Successfully")
    else:
        print("Invalid User_id and Password")
























def main():
    print(">-----------Welcome To Mini__Bank Management System-----------<")
    print("1.Create New Account\n")
    print("2.Deposit Amount\n")
    print("3.Withdraw Amount\n")
    print("4.Balance Enquiry\n")
    print("5.Display Account Holder Details\n")
    print("6.Mini Statement\n")
    print("7.Fund Transfer\n")
    print("8.Delete account\n")

    choice=int(input("Enter your choice(1-6):\n"))
    if choice==1:
        Caccount()
    elif choice==2:
        deAmount()
    elif choice==3:
        withdrawAm()
    elif choice==4:
        balanceInquiry()
    elif choice==5:
        dah()
    elif choice==6:
        miniState()
    elif choice==7:
        FundTransfer()
    elif choice==8:
        deleteAc()


main()
