import csv
with open("people.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","age"])
    for _ in range(2):
        name=input()
        age=int(input())
        writer.writerow([name,age])
print("Data written on csv file")
