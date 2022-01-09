# patika.dev
# python quiz2

result = []

def func(mixedList):
    for x in mixedList[::-1]:
         if type(x) != list:
             result.append(x)
             continue
         else:
             result.append(x[::-1])
    

if __name__ == "__main__":
    func([[1, 2], [3, 4], [5, 6, 7]])
    
    print(result)