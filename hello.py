name = input("What is your name? ")
if name == ("daniel") :
    how = input ("Hello daniel, how are you? ")
else:
    print ("hello " + name)
music = input("whats your favorite kind of music? ")
if music == ("Metal"):
    print ("Wow " + name + " I love Metal ")
elif music == ("metal"):
     print("Wow " + name + " I love Metal ")
else:
    print("Oh " + name + " ,why would you pick " + music)
color = input ("whats your favorite color? ")
if color == ("black") :
    print ("black is my favorite too")
else:
    print ("im not a fan of " + color)
movie = input("whats your favorite movie or series? ")
if movie == ("austin powers") :
    print (movie + " is a very good series")
elif movie == ("monty python and the holy grail") :
    print (movie + " is my favorite movie")
else:
    print ("i've never heard of " + movie)
season = input("whats your favorite season " + name + " ")
if season == ("winter") :
    print ("i love winter")
else:
    print ("im not a fan of " + season)
print("it was nice talking to you",name,", i learned a lot, like how your favorite music is",music,",your favorite color is",color,",your favorite movie or series is",movie,"and your favorite season is",season,)
bye = input ("bye " + name + " ")
if name == ("daniel") and how == ("meh") and music == ("metal") and color == ("black") and movie == ("monty python and the holy grail") and season == ("winter") and bye == ("cya") :
    print ("y'know you and i like a lot of the same stuff daniel")
