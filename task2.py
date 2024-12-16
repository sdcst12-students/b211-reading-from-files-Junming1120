"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

def find():
    lines = [line.strip() for line in open('task02c.txt')]
    output = 0
    for i in range(0, len(lines), 4):
        triplet = list(map(int, [lines[i], lines[i+1], lines[i+2]]))
        hypotenuse = max(triplet)
        triplet.remove(hypotenuse)
        total = 0
        for j in triplet:
            total += j**2
        if total == hypotenuse**2:
            output += 1
    return output

if __name__ == "__main__":
    print(find())