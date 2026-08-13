m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
m4 = int(input("Enter marks for Subject 4: "))
m5 = int(input("Enter marks for Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total marks =", total)
print("Percentage =", percentage)

if percentage >= 90:
    print("DISTINCTION")
elif percentage >= 80:
    print("FIRST CLASS")
elif percentage >= 70:
    print("SECOND CLASS")
elif percentage >= 60:
    print("AVERAGE")
else:
    print("FAIL")

