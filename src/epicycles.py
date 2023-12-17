from manim import *

class createEpicycles(Scene):
    
    def accessData(self, filename, data, shape):
        
        global polar
        global image_path
        global image_shape

        image_path = filename
        polar = data
        image_shape = shape
        
    def setup(self): #don't use init
            
        config.quiet = True
        config.quality = "low_quality"
        config.open = True

    #def gen_epicyles():



    def generate_points(self, cplane, points):
        print("generating points")
        for dot in points:
            comp = complex(dot[0], dot[1])
        #for dot in points:
        #    r = dot[0]
        #    cosine = dot[1]
        #    sine = dot[2]

        #    comp = complex(r*cosine, r*sine)
            self.add(Dot(cplane.n2p(comp), color = YELLOW))


    def construct(self):
        
        print("constructing plane")
        
        min_range = min(polar[:][1])
        max_range = max(polar[:][1])

        min_domain = min(polar[:][0])
        max_domain = max(polar[:][0])
        
        print(min_domain)
        plane = ComplexPlane(x_range= [min_domain, max_domain, 20], y_range = [min_range, max_range, 20], x_length = 30, y_length = 30)

        self.add(plane)

        self.generate_points(plane, polar)

        #d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        #d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
        

#        self.add(
#            d1,
#            d2,
#        )

    #    gen_epicycles = fourier_epicycles()
            
        #self.play(epicycles(self.fourier))


    #def addPoints():
        
