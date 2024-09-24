total_candies = int(input("Enter the number of candies Shinchan has: "))
 
friends = ['Masao', 'Nene', 'Bo', 'Kazama']
 
while total_candies > 0:
    for friend in friends:
        if total_candies <= 0:
            break
       
        print(f"Give 1 candy to {friend}")
        total_candies -= 1
       
        if total_candies > 0 and total_candies % 5 == 0:
            print(f"{friend} gets a candy! You are good.")
        else:
            print(f"{friend} gets a candy!",total_candies ," are left")
 
if total_candies <= 0:
    print("No candies left. Shinchan: 'SORRY'")
 
