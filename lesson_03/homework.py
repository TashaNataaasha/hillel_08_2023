results = []

with open("user_homework.txt") as file:
    for line in file:
        if "user" in line:
            print(line)
            decision = input("Do you want to add this line to the results? (yes/no): ")
            if decision.lower() == "yes":
                results.append(line)
                # print("Results: ",results)
            else:
               pass
                
print("Results: ",results)       
print("Amount of added lines:", len(results))
