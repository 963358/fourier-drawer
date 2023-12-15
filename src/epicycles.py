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



    def generate_points(cplane, points):
        print("FIRST")
        for dot in points:
            r = points[dot][0]
            cosine = points[dot][1]
            sine = points[dot][2]
            self.add(Dot(cplane.n2p(r*cosine + r*sinej), color = YELLOW))
    
    def construct(self):
        print("SECOND")
        plane = ComplexPlane().add_coordinates()
        self.add(plane)

        generate_points(plane, data)
        #d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        #d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
        

#        self.add(
#            d1,
#            d2,
#        )

    #    gen_epicycles = fourier_epicycles()
            
        #self.play(epicycles(self.fourier))


    #def addPoints():
        
