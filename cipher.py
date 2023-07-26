# add your code here
# Will do the caesar cipher converting uppercases to lowercases
lowercases = "abcdefghijklmnopqrstuvwxyz"
msgtoencrypt = input("Please enter a sentence:")
msgtoencrypt = msgtoencrypt.lower()
msgencrypted = ''
for i in range(len(msgtoencrypt)):
    if msgtoencrypt[i] not in lowercases:
        msgencrypted += msgtoencrypt[i]
    else:
        msgencrypted += lowercases[(lowercases.index(msgtoencrypt[i]) + 5) % 26]
print("The encrypted sentence is:", msgencrypted)



