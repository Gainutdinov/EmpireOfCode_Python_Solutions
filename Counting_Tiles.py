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
    
def golf(r):
 a=n=i=0;d=int(-(-r//1))
 while i<d:
  for j in range(d):
   if i*i+j*j>r*r:break
   if (i+1)**2+(j+1)**2>r*r:n+=4
   else:a+=4
  i+=1
 return a,n
