class character(object):
    """description of class"""

    def __init__(self, name, gender,speciesName,lifeSpan,homePlanetName,movies):
     self.name = name
     self.gender = gender
     self.speciesName = speciesName
     self.lifeSpan = lifeSpan
     self.homePlanetName = homePlanetName
     self.movies = movies

     # getter method
     def get_name(self): 
        return self.name 
      
    # setter method
     def set_name(self, x): 
        self.name = x 

          # getter method
     def get_gender(self): 
        return self.gender
      
    # setter method
     def set_gender(self, x): 
        self.gender = x   # getter method

     def get_speciesName(self): 
        return self.speciesName 
      
    # setter method
     def set_speciesName(self, x): 
        self.speciesName = x  
       
        # getter method
     def get_lifeSpan(self): 
        return self.lifeSpan 
      
    # setter method
     def set_lifeSpan(self, x): 
        self.lifeSpan = x  
       
        # getter method
     def get_homePlanetName(self): 
        return self.homePlanetName 
      
    # setter method
     def set_homePlanetName(self, x): 
        self.homePlanetName = x 

             # getter method
     def get_movies(self): 
        return self.movies 
      
    # setter method
    def set_movies(self, x): 
        self.movies = x 