"""
greating = "Greatings to you"
name = input("Please enter your name: ")
greatings = greating+" "+name
print(greatings)


message ="HELLO world"

print(message.capitalize())
print(message.lower())
print(message.title())
print(message.swapcase())
"""
"""
#user data
user_data = " I'm goint to remove on the trailing whitespace"
user_data = user_data.rstrip() 
user_data = user_data+"."
print(user_data)

lower_data = user_data.lower()
print(lower_data)
"""

message = "I HATE THIS CLASS. HATE"
message = message.replace("HATE","LIKE")
print(message)
print(message.find("LIKE"))
print(message.rfind("LIKE"))
message_list = message.split(" ")
print(message_list)
print(message_list[1])
