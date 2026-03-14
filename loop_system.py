print("Welcome to Smart Task Repetition System")
task_name=input("Enter task name: ")
task_repeat=int(input("Task repetition: "))

print()
for i in range(task_repeat):
    print( task_name ,"completed.")


print()
count_number=int(input("Enter countdown number: "))

for i in range(count_number,0,-1):
    print(i)

print()

sessions = ["Morning", "Evening"]
for i in sessions:
    for j in range(1,4):
        print(i,"Task",j)


# Infinite loop testing and Solving:
# num = 5
# while num > 0:
#     print(num)
#     num -=1


