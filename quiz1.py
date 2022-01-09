# patika.dev
# python quiz1

result = []

def func(mixedList):
    for x in mixedList:
        if type(x) != list:
            result.append(x)
            continue
        else:
            func(x)
    

if __name__ == "__main__":
    func([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
    
    print(result)