class SuperHero():
    def __init__(self,name,superpower):
        self.name = name
        self.superpower = superpower

    def get_superpower(self):
        print(f"I am {self.name} and My Power is {self.superpower}")    
        
batman = SuperHero("Batman","Shadow Effect")
superman = SuperHero("Super Man","Super effect")

batman.get_superpower()
superman.get_superpower()
