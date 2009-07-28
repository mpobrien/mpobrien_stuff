import ImageDraw
import Image

class CornerMaker:
    def __init__(self, radius, fg_color, bg_color=None):
        self.radius = radius
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.img = Image.new('RGBA', [radius * 2, radius * 2] )
        draw = ImageDraw.Draw(self.img)
        if bg_color: draw.rectangle( [0, 0, radius*2, radius*2], fill=bg_color)
        draw.ellipse( [0,0, radius *2,radius*2], fill=fg_color )

    def pad_corner(self, pad_horz=None, pad_vert=None):
        full_x, full_y = self.radius + ( pad_horz or 0 ), self.radius + ( pad_vert or 0 )
        full_img = Image.new( 'RGBA', [full_x, full_y] )
        draw = ImageDraw.Draw(full_img)
        clear_color = self.fg_color + tuple([0])
        draw.rectangle( [0, 0, full_x, full_y], fill=self.fg_color)
        return full_img

    def top_left(self, pad_right=None, pad_bottom=None ):#{{{
        img_temp = self.pad_corner( pad_right, pad_bottom )
        corner_img = self.img.copy().crop([0,0,self.radius, self.radius])
        img_temp.paste( corner_img, (0,0))
        return img_temp#}}}

    def top_right(self, pad_left=None, pad_bottom=None ):#{{{
        img_temp = self.pad_corner( pad_left, pad_bottom )
        corner_img = self.img.copy().crop([self.radius,0,self.radius*2,self.radius])
        img_temp.paste( corner_img, (img_temp.size[0] - self.radius, 0))
        return img_temp#}}}

    def bottom_right(self, pad_left = None, pad_top = None ):#{{{
        img_temp = self.pad_corner( pad_left, pad_top )
        corner_img = self.img.copy().crop([self.radius,self.radius,self.radius*2, self.radius*2])
        img_temp.paste( corner_img, (img_temp.size[0] - self.radius, img_temp.size[1]-self.radius))
        return img_temp#}}}

    def bottom_left(self, pad_right = None, pad_top = None ):#{{{
        img_temp = self.pad_corner( pad_right, pad_top )
        corner_img = self.img.copy().crop([0,self.radius,self.radius, self.radius*2])
        img_temp.paste( corner_img, (0, img_temp.size[1]-self.radius))
        return img_temp#}}}

def sample():
    cm = CornerMaker(8, (235,162,36), (255,255,255) )
    cm.top_left(100, 0).save("/home/mike/projects/mpobrien_stuff/tl.png")
    cm.top_right(0, 0).save("/home/mike/projects/mpobrien_stuff/tr.png")
    cm.bottom_left(100, 100).save("/home/mike/projects/mpobrien_stuff/bl.png")
    cm.bottom_right(0, 100).save("/home/mike/projects/mpobrien_stuff/br.png")

if __name__ == '__main__': sample()

