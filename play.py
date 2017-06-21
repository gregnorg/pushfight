# -----------------
# |   | b8| c8|   |
# -----------------
# | a7| b7| c7|   |
# -----------------
# | a6| b6| c6| d6|
# -----------------
# | a5| b5| c5| d5|
# -----------------
# | a4| b4| c4| d4|
# -----------------
# | a3| b3| c3| d3|
# -----------------
# |   | b2| c2| d2|
# -----------------
# |   | b1| c1|   |
# -----------------


# a board state consists of 10 board locations and an asterix
# The three white pushers, two white diers, three black pushers, two black diers
# The asterix marks the anchor



# Example file for working with classes
class BoardState():
  neighbors = ({'b1':{'b2','c1'},
                'c1':{'b1','c2'},
                'b2':{'b1','c2','b3'},
                'c2':{'c1','d2','c3','b2'},
                'd2':{'c2','d3'},
                'a3':{'b3','a4'},
                'b3':{'b2','c3','b4','a3'},
                'c3':{'c2','d3','c4','b3'},
                'd3':{'d2','d4','c3'},
                'a4':{'b4','a3','a5'},
                'b4':{'b3','c4','b5','a4'},
                'c4':{'c3','d4','c5','b4'},
                'd4':{'d3','d5','c4'},
                'a5':{'b5','a4','a6'},
                'b5':{'b4','c5','b6','a5'},
                'c5':{'c4','d5','c6','b5'},
                'd5':{'d4','d6','c5'},
                'a6':{'b6','a5','a7'},
                'b6':{'b5','c6','b7','a6'},
                'c6':{'c5','d6','c7','b6'},
                'd6':{'d5','c6'},
                'a7':{'a6','b7'},
                'b7':{'b6','c7','b8','a7'},
                'c7':{'c6','c8','b7'},
                'b8':{'b7','c8'},
                'c8':{'c7','b8'},
                })

  def __init__(self,startStr):
    self.stateStr = startStr

  def method1(self):
    print "Guru99"

  def method2(self,someString):    
    print self.stateStr + someString


def main():           
  # exercise the class methods  
  c = BoardState('TestString')
  c.method1()
  c.method2(" Testing is fun")
  print BoardState.neighbors['b4']

if __name__== "__main__":
  main()