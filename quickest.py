# junction : FIFTH_JUNCTION
# vehicle counter program
# records that stores the data of vehicle
records = [
    {
        "date": "2026-05-21",
        "time": "08:00",
        "from": "PRE_FAR_JUNCTION",
        "to": "FIFTH_JUNCTION",
        "count": 5
},
    {
        "date": "2026-05-21",
        "time": "08:00",
        "from": "FAR_JUNCTION",
        "to": "FIFTH_JUNCTION",
        "count": 3
    },
    {
        "date": "2026-05-21",
        "time": "08:00",
        "from": "PRE_FOR_JUNCTION",
        "to": "FIFTH_JUNCTION",
        "count": 2
    },
    {
        "date": "2026-05-21",
        "time": "08:00",
        "from": "NEXT_JUNCTION",
        "to": "FIFTH_JUNCTION",
        "count": 4
    }
]
def vehicle_count(date , time):#takes the date and time from the input
    pre_far = 0
    far = 0
    pre_for = 0
    nxt = 0
    found = False # checks if the vehicle exits in that time
    for r in records :
        if r["date"] == date and r["time"] == time :
            found = True
            if r["from"] == "PRE_FAR_JUNCTION" :
                pre_far = pre_far + r["count"]
            elif r["from"] == "FAR_JUNCTION" :
                far = far + r["count"]
            elif r["from"] == "PRE_FOR_JUNCTION" :
                pre_for = pre_for + r["count"]

    if found == False :#if no matches are found in that given time and date
        print("no data found for" , date , time)
        return
    print("At FIFTH_JUNCTION From PRE_FAR_JUNCTION :" , far , "vehicles")
    print("At FIFTH_JUNCTION From FAR_JUNCTION :"      , pre_far , "vehicles")
    print("At FIFTH_JUNCTION From PRE_FOR_JUNCTION :"  , pre_for , "vehicles")
    print("At FIFTH_JUNCTION From NEXT_JUNCTION :"     , nxt , "vehicles")

#function call
vehicle_count("2026-05-21" , "08:00")
