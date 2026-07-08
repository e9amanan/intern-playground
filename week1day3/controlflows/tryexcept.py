class datavalidationerror(Exception):
    """ custom exception for bad data """
    pass

def calculatingaverage(numbers_list):
    try:
        total=sum(numbers_list)
        count=len(numbers_list)

        if count ==0:
            raise datavalidationerror("cannot calculate average of empty list")
        return total/count
    
    except TypeError:
        print("error:list contains non numeric values")

    except datavalidationerror as e:
         print(f"validation error:{e}")

    else:
        print("calculation succesful")
        return result
    
    finally:
           print("executionfinished")


    

    