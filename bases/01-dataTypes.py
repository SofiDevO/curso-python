# Data types in Python
stringDataType = "Hola patata"
multipleStringDataType = '''Hola
patata'''
integerDataType = 2
floatDataType = 2.1
listDataType = ['2', True, 4]
setDataType = {'2', 3,'patata'  }
dictionaryDataType = {
    "patata": "frita",
    "zanahoria": "hervida"
}
tuplaDataType = (3, 4,1,4)
print(type(tuplaDataType))
boleanDataType  = True



x = {"name" : "John", "age" : 36}
print(type(x))
x = True
print(type(x))

noneDataType = None #equaxls null in other languajes

# functionDataType = lambda i: print(i)

# print(listDataType[2])
# print(setDataType)
# print(tuplaDataType[1:3])
# print(boleanDataType)

# if boleanDataType:
#     print("Tienes una patata")
if not type(boleanDataType) == str :
    print("tu patata no es boolean")

print(type(boleanDataType))
