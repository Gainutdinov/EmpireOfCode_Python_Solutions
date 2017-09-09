import math

def golf(radius):
    
    circle_radius = radius
    tile_size = 1.

    # Make a square box covering a quarter of the circle
    tile_length_1d = int(math.ceil(circle_radius / tile_size ))

    num_complete_tiles = 0
    num_partial_tiles = 0

    # Now loop over all tile_length_1d x tile_length_1d tiles and check if they
    # are needed
    for i in range(tile_length_1d):
        for j in range(tile_length_1d):
            # Does corner of tile intersect circle?
            intersect_len = ((i * tile_size)**2 + (j * tile_size)**2)**0.5
            # Does *far* corner intersect (ie. is the whole tile in the circle)
            far_intersect_len = (((i+1) * tile_size)**2 + ((j+1) * tile_size)**2)**0.5
            if intersect_len > circle_radius:
                # Don't need tile, continue
                continue
            elif far_intersect_len > circle_radius:
                # Partial tile
                num_partial_tiles += 1
            else:
                # Keep tile. Maybe you want to store this or something
                # instead of just adding 1 to count?
                num_complete_tiles += 1
    #print("You need %d complete tiles" %(num_complete_tiles))
    #print("You need %d partial tiles" %(num_partial_tiles))
    # Multiple by 4 for symmetry
    num_complete_tiles = num_complete_tiles * 4
    num_partial_tiles = num_partial_tiles * 4
    return num_complete_tiles, num_partial_tiles
    
    # 2 star solution
    
import math
def golf(r):
 s=1.
 d=int(math.ceil(r/s))
 a=n=0
 for i in range(d):
  for j in range(d):
   l,f=((i*s)**2+(j*s)**2)**0.5,(((i+1)*s)**2+((j+1)*s)**2)**0.5
   if l>r:break 
   elif f>r:n+=1
   else:a+=1
 a,n=a*4,n*4
 return a,n
