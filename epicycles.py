from manim import *

class epicycles(Scene):
    def __init__(self, filename, data):
        self.filename = filename
        print(self.filename)
        
        config.quiet = True
        config.quality = "480p15"
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
            
        self.play(epicycles(self.fourier))


