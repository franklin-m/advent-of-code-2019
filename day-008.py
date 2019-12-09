#!/usr/bin/python3

file = open('day8.txt').read()
segment = []
segm = []
one_counter = 0
two_counter = 0


def draw(ctx):
    color_str = ""
    color_arr = []
    for i in range(len(ctx)):
        for j in ctx[i]:
            if j == '0':
                color_str += "#"
            if j == '1':
                color_str += "%"
            if j == '2':
                color_str += " "
        color_arr.append(color_str)
        color_str = ""
    return color_arr


# counts zeroes of input
def count_zeroes(ctx):
    counter = 0
    for j in ctx:
        if j == '0':
            counter += 1
    return counter


# parse through the file to separate segments
# start
def iterate(ctx):
    p = ""
    for j in range(ctx, ctx+(6*25)):
        p += file[j]
    return p


for k in range(0, len(file), 6*25):
    segment.append(k)

for i in range(len(segment)):
    segm.append(iterate(segment[i]))
# end


# did this to find which segment had the fewest zeroes
for l in range(len(segm)):
    print(f"index: {l}\t Zeroes: {count_zeroes(segm[l])}")


# next step was to count the number of ones and twos then multiply the counts to get the answer
# hardcoded the seg with fewest zeroes cba to figure it out automatically
for q in segm[11]:
    if q == '1':
        one_counter += 1
    elif q == '2':
        two_counter += 1

print(one_counter*two_counter)


# I drew part 2 by hand
"""
  ##  ##  #### ###   ##  
   # #  # #    #  # #  # 
   # #  # ###  #  # #  # 
   # #### #    ###  #### 
#  # #  # #    # #  #  # 
 ##  #  # #    #  # #  # 
"""
