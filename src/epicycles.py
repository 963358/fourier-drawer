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



    def generate_points(self, cplane, points):
        print("generating points")
        for dot in points:
            comp = complex(dot[0], dot[1])
            self.add(Dot(cplane.n2p(comp), color = YELLOW))


    def construct(self):
        
        print("constructing plane")
        
        np_polar = np.array(polar)

        
        max_polar = np_polar.max(axis=0)
        
        max_domain = max_polar[0]
        max_range = max_polar[1]

        min_polar = np_polar.min(axis=0)

        min_domain = min_polar[0]
        min_range = min_polar[1]

        print(min_domain, max_domain)
        print(min_range, max_range)
        #plane = ComplexPlane(x_range= [min_domain, max_domain, 20], y_range = [min_range, max_range, 20], x_length = 30, y_length = 30)
        plane = ComplexPlane(x_range= [-200,200,20], y_range = [-200, 200, 20], x_length = 30, y_length = 30)

        self.add(plane)

        self.generate_points(plane, polar)

        
