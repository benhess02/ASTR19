class Lizard:
    
    def __init__(self):
        self.armLength = 2.0
        self.legLength = 2.0
        self.eyeCount = 2
        self.hasTail = True
        self.isFurry = False

    def describe(self):
        print("A %slizard with %s%s inch arms, %s inch legs, and %s eyes." 
              % ("furry " if self.isFurry else "", "a tail, " if self.hasTail else "",
                 self.armLength, self.legLength, self.eyeCount))

def main():
    Lizard().describe()

if __name__ == "__main__":
    main()