# Connor Wertz, TRLM 8522, Assignment 1, Hello World
print("Hello, World!")

# Ask for user's first and last name
print("What is your first name?")
firstName = input()
print("What is your last name?")
lastName = input()
print("How's it going,", firstName + "", lastName,"?")

# Ask for user's favorite numbers. I looked this up on google, it looks like a cooler way to get user input than what I put above^
firstFavNumber = int(input("What is your favorite number? "))
secondFavNumber = int(input("I see... what about your second favorite number? "))

# Carry out various equations based on the two user provided inputs
print("Let's multiply those two numbers together!", firstFavNumber, "*", secondFavNumber, "=", (firstFavNumber * secondFavNumber))
print("Next, let's add the two numbers together!", firstFavNumber, "+", secondFavNumber, "=", (firstFavNumber + secondFavNumber))
print("Finally, let's subtract the two from each other!", firstFavNumber, "-", secondFavNumber, "=", (firstFavNumber - secondFavNumber))
print("Pretty cool, right?")
response = input()
#getting a little cheeky with this, kind of unnecessary
print("Really? You think", response, "? I appreciate your honesty! Here's a few more equations for you!")
print("How about some division?", firstFavNumber, "/", secondFavNumber, "=", (firstFavNumber / secondFavNumber))
print("Next we can take", firstFavNumber, "to the power of", secondFavNumber, "which is equal to", firstFavNumber ** secondFavNumber)
print("And lastly, let's do some floor divison!", firstFavNumber, "//", secondFavNumber, "=", (firstFavNumber // secondFavNumber))

#The next part of the problem on canvas asks for us to present the user something in the browser window? How do you do that? So far i've only been able to do stuff in terminal.