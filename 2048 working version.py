"""
Clone of 2048 game.
Uruchamiac w srodowisku Coursera
"""

import poc_2048_gui
import random
#import poc_simpletest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 

#
def sort_zeros(line):
    """
    This function moves all zeros on the end of table
    """
    
    #flag means is number in column a zero 
    is_zero = False
    if line[0]==0:
        is_zero=True
    #last position when the number is positive
    last_position = 0
    
    for index in range(len(line)):
        if line[index]==0:
            if is_zero == False:
                is_zero=True
                last_position = i
            #print "poz", i
        else:    
            if is_zero == False:
                continue 
            line[last_position]=line[i]
            line[i]=0
            last_position+=1    
    
    
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """   
    sort_zeros(line)
       
    #merge sorted line
    len_line = len(line)
    for i in range(len_line): 
            if i+1 == len_line:
                break
            if line[i]==0:
                continue
 
            if line[i]==line[i+1]:
                line[i]+=line[i+1]
                line[i+1]=0 
                
    sort_zeros(line)        
                   
    return line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):

        self._grid_width=grid_width
        self._grid_height=grid_height
                
        self.reset()
        
        #up_row
        up_row =[]
        down_row=[]
        left_row=[]
        right_row=[]
        
        height=self.get_grid_height()
        width=self.get_grid_width()
        
        #up and down rowe
        for i in range(0,width):
            up_row.append((0,i))
            down_row.append((height-1,i))
        
        #left_row
        for i in range(0,height):
            left_row.append((i,0))
            right_row.append((i, width-1))
        
        
        self.INDICIES = {UP: up_row, 
           DOWN: down_row, 
           LEFT: left_row, 
           RIGHT: right_row} 

    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """

        self.grid = [[0 for dummy_col in range(self.get_grid_width())] for dummy_row in range(self.get_grid_height())]
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        return str(self.grid)


    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        #initial title - first cells of rows/colums being changed
        
        indi=self.INDICIES[direction]
        
        for i in range(len(indi)):
            table=[]
            start = list(indi[i])
            
            
            #p - pointer
            p = start
            
            #chose what direction
            if direction == UP or direction == DOWN:
                #print "UP, down"
                n = 0 #so p[o] and direction[0]
                iter_range = self.get_grid_height()-1
            if direction == LEFT or direction == RIGHT:  
                #print "left, right"
                n = 1 #so p[o] and direction[0]
                iter_range = self.get_grid_width()-1            
            
            #iterate over table to get values of tiles
            tile_value = self.get_tile(p[0],p[1])
            table.append(tile_value)
            for dummy_i in range(iter_range):
                #move pointer with offset on direction
                #pointer points to next value in grid
                p[n]+=OFFSETS[direction][n]    
                tile_value = self."work_on_tile(self.get_tile, p)
                table.append(tile_value)
                        
            #merge table with values taken from grid
            merge(table)

                       
            #iterate over merge table to write tiles from table values
            row, col = p[0],p[1]
            self.set_tile(row, col, table.pop())             
            for i_dummy in range(iter_range):
                #move pointer with offset on direction
                #pointer points to next value in grid
                p[n]-=OFFSETS[direction][n]    
                row, col = p[0],p[1]
                self.set_tile(row, col, table.pop())
           
            #print "table ", table
        self.new_tile()               
                   
            
    def "work_on_tile(self, func, p, value=None):
        
        """
        "work_on_tile - chose funtion that will be used on p
        func - funcion that does job on p(point on grid)
        """    
        if value == None:
            return func(p[0],p[1])
        else:
            return func(p[0],p[1], value)
    

                

    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # chose random point in grid
        #if empty write value
        zero_value = []
        for row in range(0,self.get_grid_height()):
            for col in range(0,self.get_grid_width()):
                value = self.get_tile(row,col)
                if value ==0:
                    zero_value.append((row,col))
        
        if zero_value == []:
            return None
        
        (random_row, random_col) = random.choice(zero_value)               

        value=random.randint(1,10)
        if value==1:    
            value=4
        else:       
            value=2
        self.set_tile(random_row, random_col,value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        

        if row > self.get_grid_height():
            return False
        if col > self.get_grid_width():
            return False
        
        self.grid[row][col]=value


    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        if row > self.get_grid_height() or row < 0:
            return None
        if col > self.get_grid_width() or row < 0:
            return None
        
        return self.grid[row][col]
 


#def run_test_merge(format_function):
    """
        testing function
    """
    #suite = poc_simpletest.TestSuite()
    
    
    #suite.run_test(format_function([2, 0, 2, 4]), [4, 4, 0, 0], "Test #1:")
    #suite.run_test(format_function([0, 0, 2, 2]), [4, 0, 0, 0], "Test #2:")
    #suite.run_test(format_function([2, 2, 0, 0]), [4, 0, 0, 0], "Test #3:")
    #suite.run_test(format_function([2, 2, 2, 2]), [4, 4, 0, 0], "Test #4:")
    #suite.run_test(format_function([8, 16, 16, 8]), [8, 32, 8, 0], "Test #4:")
    #suite.report_results()

#run_test_merge(merge)    
    
grid = TwentyFortyEight(3, 5)  

poc_2048_gui.run_gui(TwentyFortyEight(3,5))

print str(grid)

   