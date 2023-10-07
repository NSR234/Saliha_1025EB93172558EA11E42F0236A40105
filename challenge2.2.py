#Define the base class player


class player:

  def play(self):
    print("The player is playing cricket.")


#Define the derived class player
class Batsman(player):

  def play(self):
    print("The batsman is batting.")


#Define the derived class player
class Bowler(player):

  def play(self):
    print("The bowler ia bowling.")


#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()
