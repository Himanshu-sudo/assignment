import pandas as pd
import os.path


def reading(roomid):
    read_data = pd.read_csv(roomid.upper()+'.csv')
    print(read_data.to_string())


def writing(roomid):
    list1 , list2 , userlist = [] , [] , []
    # ENTER THE DATE TIME TIMEPERIOD WITH ONLY ONE SPACE IN BETWEEN.
    # DONT GIVE ANY SPACES WHILE ENTERING TIMEPERIOD EX.12:30to13:30
    # GIVING SPACES BETWEEN TIMEPERIOD WILL GIVE ERROR EX.12:30 to 13:30 ERROR!!!
    recordw = list(map(lambda x: x, input("Enter the data in format of Date[Year-mon-day] Time Timeperiod(start_timetoend_time) seperated by 1 space [PLEASE USE 24 HOUR TIME FORMAT]").strip().split()))[:3]
    userlist = recordw[2].split("to")
    temp1 = userlist[0].split(":")
    temp2 = userlist[1].split(":")
    userlist.clear()
    userlist.append(temp1[0]+temp1[1])
    userlist.append(temp2[0] + temp2[1])
    df = pd.read_csv(roomid.upper()+'.csv')

    mask = df['Date'].values == recordw[0]
    df_new = df[mask]
    letter = df_new.Timeperiod.tolist()
    for x in letter:
        start, end = x.split("to")
        start = start.split(":")
        beg = start[0] + start[1]
        list1.append(beg.strip())
        end = end.split(":")
        fin = end[0] + end[1]
        list2.append(fin.strip())
    i = 0
    case = False
    while i < len(list1):
        if (int(userlist[0]) >= int(list1[i]) and int(userlist[0]) < int(list2[i])) or (int(userlist[1]) > int(list1[i]) and int(userlist[1]) < int(list2[i])):
            case = True
        i += 1
    if case :
        print("Sorry,the time slot that you have chosen is occupied kindly check and try again!")
    else:
        writ = pd.DataFrame([recordw])
        writ.to_csv(roomid.upper() + '.csv', mode='a', header=False, index=False)
        print("Your time slot is scheduled successfully!")


def create(roomid):
    cities = pd.DataFrame(columns=['Date', 'Time','Timeperiod'])
    cities.to_csv(roomid.upper()+'.csv', mode='a', index=False)


print("****WELCOME TO SCHEDULE MANAGEMENT SYSTEM****")
choice = True
while choice:
    print("Please Enter the roomid in which you want to schedule your appointment")
    roomy = input()

    if os.path.isfile(roomy.upper()+'.csv'):
        print ("File exist")
        print("Do you want to read or write?")
        op = input()
        if op.upper() == 'WRITE':
            writing(roomy)
        elif op.upper() == 'READ':
            reading(roomy)
        else:
            print("INVALID INPUT!")
    else:
        print ("Creating a File...")
        create(roomy)
        writing(roomy)
    print("Do you want to continue yes/no")
    ch = input()
    if ch.upper() == 'NO':
        choice = False




