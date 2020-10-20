#!/usr/bin/env python
# coding: utf-8

# In[44]:


#  This script takes an .svg file (containing one path), reduces the number of line segments,
# connnects the vertices together, and outputs an optimized .svg file with fewer vertices.


from svgpathtools import svg2paths, Path, Line, wsvg

input_file = 'PixelScaled.svg' # input file
paths, attributes = svg2paths(input_file)

path = paths[0]
reduce_factor = int(input("enter optimization_factor:" )) # has to be a positive integer > 0
reduced_path = path[::reduce_factor] # this reduces the line segments in the path by the 'reduce_factor'

orig_start = [] 
new_start = []
end = []
for lines in reduced_path:
    orig_start.append(lines[0])
    end.append(lines[1])

new_start.append(orig_start[0])
new_start.extend(end)
end.append(new_start[0])
line_segments = list(zip(new_start, end)) 

optimized_path = Path()
for points in line_segments:
    segments = Line(points[0], points[1])
    optimized_path.append(segments)

wsvg(optimized_path, filename = 'Optimized_SVG.svg', openinbrowser=True) # output file

    
   

