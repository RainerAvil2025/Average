#taking the total amount from the user
amount=int(input("Please enter the amount to withdraw"))
#calculating the number of notes of different denominations
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of hundred rupees",note1)
print("notes of hundred rupees",note2)
print("notes of hundred rupees",note3)