dir = "day1"

input = open(dir + '/input.txt', 'r')
lines = input.readlines()

prev_slide = 0
inc_count = -1
slides = [0, 0, 0]
counter = 1

for line in lines:
    num = int(line)

    if counter == 1:
        slides[0] = num
    elif counter == 2:
        slides[0] += num
        slides[1] = num
    else:
        slides = [x+num for x in slides]
        complete_slide = counter % 3
        if slides[complete_slide] > prev_slide:
            inc_count += 1
        prev_slide = slides[complete_slide]
        slides[complete_slide] = 0
        
    counter += 1

with open(dir + '/output.txt', 'w') as output:
    output.write(str(inc_count))
