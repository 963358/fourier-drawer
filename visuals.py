from manim import * 


class visuals(Scene):
    def construct(self):
         circle = Circle()
         circle.set_fill(PINK, opacity=0.5)
         self.play(Create(circle))
         self.wait()
