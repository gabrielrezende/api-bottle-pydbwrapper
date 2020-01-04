import random

class Utils:

    @staticmethod
    def get_random_color():
        r = random.randint(0,18)
        colors = ['#7F0000', '#560027', '#12005E', '#000063', '#000051', '#002171', '#002F6C',    
                  '#00363A', '#00251A', '#003300', '#003D00', '#524C00', '#BC5100', '#C43E00', 
                  '#AC1900', '#870000', '#1B0000', '#000000', '#000A12']
        

        return colors[r]