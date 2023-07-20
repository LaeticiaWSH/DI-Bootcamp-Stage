matrix =[
    [7,'i','i'],
    ['T','s','x'],
    ['h','%','?'],
    ['i','#','#'],
    ['s','M','#'],
    ['$','a','#'],
    ['#','t','%'],
    ['^','r','!']
]
secret_message = []
message = " "
i = 0
while i <= 2:
    for items in range(0,len(matrix)):
        x = str(matrix[items][i])
        # print(x)
        if x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            message = message + x
            secret_message.append(matrix[items][i])
        else:
            message = message + " "

    i += 1
        
print(secret_message)
print("The message is: ")
print(message)