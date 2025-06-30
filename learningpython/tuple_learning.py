student1 = ("Eva", 7 , "Roblox")
student2 = ("Joy" , 9 , "Fortnite")

def high_score():
    highscore = (("Sam", 12, 490), ("Eva" , 9, 495), ("Jay",10 ,480), ("Justin", 8, 300))
    maxvalue = max(highscore,key=lambda t: t[2])
    print(maxvalue)

high_score()