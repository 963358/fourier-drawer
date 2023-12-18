from manim import *

class createEpicycles(Scene):
    
    def accessData(self, filename, data, shape):
        
        global complx
        global image_path
        global image_shape
        
        image_path = filename
        complx = data
        image_shape = shape

    def setup(self): #don't use init
            
        #config.pixel_width = image_shape[1]
        #config.pixel_height = image_shape[0]
        


        config.quality = "low_quality"
        config.quiet = True
        config.open = True



    def generate_points(self, cplane, points):
        print("generating points... might take a while :( ")
        
        for dot in points: 
            self.add(Dot(cplane.n2p(dot), color = YELLOW))


    def construct(self):
        
        print("constructing plane")
        
        np_complx = np.array(complx)

        
        max_domain = np_complx.real.max()
        max_range = np_complx.imag.max()

        min_domain = np_complx.real.min()
        min_range = np_complx.imag.min()
        
        print("range: ", min_range, max_range)
        print("domain: ", min_domain, max_domain)

        plane = ComplexPlane(x_range= [min_domain - 200, max_domain + 200, 50], y_range = [min_range - 200, max_range + 200, 50], x_length = 10, y_length = 10)
        

        self.add(plane)

        self.generate_points(plane, complx)

        
