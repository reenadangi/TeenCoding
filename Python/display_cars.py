def findBMW(cars):
    for car in cars:
        if car=="BMW":
            return True
    return False
cars=["BMW","Audie","MERC"]
cars2=["Audie","BM","MERC"]
print(findBMW(cars2))

