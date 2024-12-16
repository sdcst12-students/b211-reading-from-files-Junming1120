#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""
def find():
    lines = [line.strip() for line in open('task03.txt')]
    i = 0
    largest = []
    while i < len(lines):
        total = 0
        while i < len(lines) and lines[i] != '':
            total += int(lines[i])
            i += 1
        largest.append(total)
        i += 1
    return max(largest)

if __name__ == "__main__":
    print(find())