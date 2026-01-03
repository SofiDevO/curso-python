from typing import Callable, Any

# Data types in Python
stringDataType = "Hola patata"
integerDataType = 2
floatDataType = 2.1
listDataType:list[str | bool | int] = ['2', True, 4]
setDataType:set[str | int |str] = {'2', 3,'patata'  }
tuplaDataType = (3, 4,1,4)
dictionaryDataType = {
    "patata": "frita",
    "zanahoria": "hervida"
}

boleanDataType  = []
noneDataType = None #equaxls null in other languajes

functionDataType: Callable[[Any], None] = lambda i: print(i)

# print(listDataType[2])
# print(setDataType)
# print(tuplaDataType[1:3])
# print(boleanDataType)

# if boleanDataType:
#     print("Tienes una patata")
if not type(boleanDataType) == str :
    print("tu patata no es boolean")

print(type(boleanDataType))
