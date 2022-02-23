<h2>'Python Temel' Patikasi</h2>
Python Temel patika'sindaki bitirme projesi olarak
sorulan 2 soru icin yazdigim cozumler;

<h3>Soru 1</h3>
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

<b>input</b>: `[[1,'a',['cat'],2],[[[3]],'dog'],4,5]`

<b>output</b>: `[1,'a','cat',2,3,'dog',4,5]`

<h3>Cozum;</h3>

```
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
```

<h3>Soru 2</h3>
Verilen listenin içindeki elemanları tersine
döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste
içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

<b>input</b>: `[[1, 2], [3, 4], [5, 6, 7]]`

<b>output</b>: `[[[7, 6, 5], [4, 3], [2, 1]]`

<h3>Cozum;</h3>

```
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
```
