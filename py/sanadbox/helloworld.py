
""" a = input("enter number1")
b = input("enter number 2")

print(float(a)/float(b))
print("Hello world") """

""" name = ["Shreya", "Prashant","Kumar","Prem",1,4,"Shreya"]
print(name)
name[2] = "Swamy"
print(name)
print(tuple(name))
tuple_name = tuple(name) """

#tuple_name[2] = "Swamy"

student1 = { 
    "name": "Prem", 
    "dob": "1-2-1992",
    "roll": 1245,
    "finalPercentage": 45.5,
    "isActive": True
    }
student2 = { 
    "name": "Prashant", 
    "dob": "11-8-1995",
    "roll": 423,
    "finalPercentage": 40.5,
    "isActive": True,
    "subjectMarks": [32,45,78.7]
    }

print(student2.get("subjectMarks"))
