def getCoordinates(point):
    return point[0],point[1]

def euclideanDistance(pointFirst,pointSecond):
    x1,y1 = getCoordinates(pointFirst)
    x2,y2 = getCoordinates(pointSecond)

    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)


def findMinimumDistance(distances):
    minDistance = distances[0]

    for distance in distances:
        if distance<minDistance:
            minDistance = distance

    return minDistance

def main():
    point1= (5, 5)
    point2= (8, 7)

    point3 = (2, 5)
    point4 = (12, 7)

    points = [[point1,point2],[point3,point4]]
    distances = []

    for pointFirst, pointSecond in points:
        distances.append(euclideanDistance(pointFirst,pointSecond))
    
    minimumDistance = findMinimumDistance(distances)
    print(minimumDistance)

if __name__ == "__main__":
    main()
