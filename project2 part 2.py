#project2 part:1
""" Author - Avipreet singh """
def drawCircles(t, circle_size, num_circles, size_reduce):
    
    """This function creates number of circles in one direction"""
    """ Parameters are discribed as followed"""
    
    for a in range(num_circles): # num_circles(number of circles),
        t.circle(circle_size) #cicle_size(reprsents the size of the circle)
        circle_size= circle_size- size_reduce # size_reduce(how much size should be reduced in next circle)
        
def drawSpecial(t, num_petals, circle_size, num_circles, size_reduce):
    
    """This function crated the number of petals of mandala in different direction"""
    """ Parameters are discribed as followed"""
    
    for b in range(num_petals): # num_petals(number of petals)
        drawCircles(t, circle_size, num_circles, size_reduce) # first function called here
        t.right(360/num_petals) # number of angles will be equal to the number of the petals
        
        

def main():
    import turtle
 
    """screen attributes"""
    win = turtle.Screen() 
    win.bgcolor('black') # screen color is set to black
    
    """turtle attributes"""
    albert = turtle.Turtle()
    albert.speed(0) # speed set to 0
    
    """Parameters"""
    circle_size_list = [140,120,110,90,80,70,60]
    num_petals = 10  # number of petals 
    colors_list = [ 'blue','blue','yellow' ,'yellow','white', 'orange', 'pink'] # colors for the next size
    num_circles_list = [10, 10, 5, 4, 4, 4, 4]
    size_reduce_list = [4, 4, 5, 10, 5, 19, 20]
    p1 = 0 # list position
    
    
    for colors in colors_list:
        albert.color(colors)
        drawSpecial(albert, num_petals, circle_size_list[p1], num_circles_list[p1], size_reduce_list[p1]) # function 2 is called here
        p1= p1 +1 # pass to next position
    win.exitonclick()
if __name__ == "__main__":
    main()