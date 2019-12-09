#!/usr/bin/python3

file = open('input.txt').read()
segment = []
segm = []
one_counter = 0
two_counter = 0


def draw_msg(ctx):
    color_str = ""
    c_zr = 0
    c_on = 0
    c_tw = 0
    for i in ctx:
        if i == '0':
            c_zr += 1
        elif i == '1':
            c_on += 1
        elif c_tw == '2':
            c_tw += 1
    if c_zr > c_on and c_tw:
        color_str += "&#9619;"
    elif c_on > c_zr and c_tw:
        color_str += "&#9618;"
    elif c_tw > c_zr and c_on:
        color_str += "&#9617;"
    return color_str


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
    print(draw_msg(segm[l]))

# next step was to count the number of ones and twos then multiply the counts to get the answer
# hardcoded the seg with fewest zeroes cba to figure it out automatically
for q in segm[11]:
    if q == '1':
        one_counter += 1
    elif q == '2':
        two_counter += 1

print(one_counter*two_counter)
