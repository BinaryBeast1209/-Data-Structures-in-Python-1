class Robot:

    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

    def introduce(self):
        print("Hello!")
        print("My name is", self.name)
        print("My purpose is", self.purpose)


robot1 = Robot("Robo", "Helping Students")

robot1.introduce()
