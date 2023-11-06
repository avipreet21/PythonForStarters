#lab44
''' 
  Starter project for the lab. The program provides a function to draw one  
  letter using a turtle. 
'''
carbon = int(input("number of the carbon?"))

def hydrogen_output(carbon):
    hydrogens = 2 * carbon + 2
    return hydrogens
import turtle

def draw_letter(t,letter):
    '''
        using the turtle t draw the letter in 20pt Arial font
        the turtle ends up in the same position it started and is 
        also heading in the same direction
    '''

    (start_x, start_y) = t.position()
    start_heading = t.heading()

    if t.heading()== 0.0:
        
        t.penup()
        t.right(90)
        t.forward(15)

    elif t.heading()== 90.0:
       
        t.penup()
        t.left(90)
        t.forward(8)

    elif t.heading()== 270.0:
    
        t.penup()
        t.forward(30)
        t.right(90)
        t.forward(8)

    t.write(letter, move=False, align="left", font=("Arial", 20, "normal"))
    t.setposition(start_x, start_y)
    t.setheading(start_heading)

def draw_hydrogen(t):
    t.pendown()
    t.forward(100)
    t.penup()
    t.forward(20)
    draw_letter(t, 'H')

def draw_molecule(t):
    for i in range(carbon):
        draw_letter(t,'C')
        t.forward(10)
        t.right(90)
        t.forward(20)
        draw_hydrogen(t)
        t.right(180)
        t.forward(160)
        draw_hydrogen(t)
        t.right(180)
        t.forward(140)
        t.left(90)
        t.forward(20)
        t.pendown()
        t.forward(100)
        t.penup()
        t.forward(20)
        
def main():
    
    # Create screen and turtle.
    t = turtle.Turtle()
    t.pensize(3)
    
    screen = turtle.Screen()
    screen.title('Alkane')
    #position the turtle in the left part of the screen
    (width, height) = screen.screensize()
    newx= -width/2
    newy = 0

    t.penup();
    t.goto(newx,newy)
    
    print("number of hydrogens are", hydrogen_output(carbon))
    
    t.right(180)
    draw_hydrogen(t)
    t.right(180)
    t.forward(160)
    draw_molecule(t)
    draw_letter(t,'H')

if __name__ == "__main__":
  main()

