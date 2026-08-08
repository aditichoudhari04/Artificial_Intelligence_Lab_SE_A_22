from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(likes='Graphics'), StudentFacts(likes='Maths'))
    def civil(self):
        print("Suggested Career Path: Civil Engineering")
    @Rule(StudentFacts(likes='Art'), StudentFacts(likes='Design'))
    def graphicdesign(self):
        print("Suggested Career Path: Graphic Design")
    @Rule(StudentFacts(likes='Statistics'), StudentFacts(likes='Maths'))
    def dataanalysis(self):
        print("Suggested Career Path: Data Analysis")
def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("ENTER THE SUBJECTS FROM THIS LIST")
    print("Maths\nPhysics\nProgramming\nBiology\nChemistry\nMechanical\nComputer\nElectronics")
    interests = input("Enter your any 2 interests separated by commas(start the words with a capital subject):").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()
