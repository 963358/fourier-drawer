from manim import *

class createEpicycles(Scene):
    
    def accessData(self, filename, data):
        
        global polar
        global image_path

        image_path = filename
        polar = data

    def setup(self): #don't use init
            
        config.quiet = True
        config.quality = "low_quality"
        config.open = True

    #def gen_epicyles():


    def construct(self):
        plane = ComplexPlane().add_coordinates()
        self.add(plane)
        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
        

        self.add(
            d1,
            d2,
        )

    #    gen_epicycles = fourier_epicycles()
            
        #self.play(epicycles(self.fourier))


    #def addPoints():
        
