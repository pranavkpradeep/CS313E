#  File: Geometry.py

#  Description:

#  Student Name: fdsaadafsdfad

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import math
import sys


class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return ("(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")")
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-6
    return ((abs(self.x-other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.center = Point(x, y, z)
    self.radius = radius


  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return "Center: (" + str(self.center.x) + ", " + str(self.center.y) + ", " + str(self.center.z) + "), Radius: " + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return 4.0 * math.pi * (self.radius ** 2)
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return (4/3) * math.pi * (self.radius ** 3)
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    return self.center.distance(other.center) < (self.radius - other.radius)

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    flag = True
    for vertex in a_cube.vertices:
      if not self.is_inside_point(vertex):
        flag = False
    return flag

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    is_outside = self.center.distance(other.center) > (self.radius + other.radius)
    if self.is_inside_sphere(a_cube) is False and is_outside is False:
      return True
    else:
      return False

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    flag = True
    for vertex in a_cube.vertices:
      if self.is_inside_point(vertex):
        flag = False

  if flag == True and self.is_inside_cube(a_cube) == False:
    return True
  else:
    return False


  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    return Cube(self.center.x, self.center.y, self.center.z, math.hypot(self.radius, self.radius))
class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.center = Point(x, y, z)
    self.side = side
    self.vertices = []
    radius = self.side * .5
    
    self.vertex1 = (Point(x + radius, y + radius, z + radius))
    self.vertex2 = (Point(x - radius, y + radius, z + radius))
    self.vertex3 = (Point(x - radius, y - radius, z + radius))
    self.vertex4 = (Point(x - radius, y - radius, z - radius))
    self.vertex5 = (Point(x + radius, y - radius, z - radius))
    self.vertex6 = (Point(x + radius, y - radius, z + radius))
    self.vertex7 = (Point(x - radius, y + radius, z - radius))
    self.vertex8 = (Point(x + radius, y + radius, z - radius))
    
    self.vertices.append(self.vertex1)
    self.vertices.append(self.vertex2)
    self.vertices.append(self.vertex3)
    self.vertices.append(self.vertex4)
    self.vertices.append(self.vertex5)
    self.vertices.append(self.vertex6)
    self.vertices.append(self.vertex7)
    self.vertices.append(self.vertex8)



  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return "Center: (" + str(self.center.x) + ", " + str(self.center.y) + ", " + str(self.center.z) + "), Side: " + str(self.side)
  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number

  def area (self):
    return 6 * (self.side * self.side)
  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return self.side ** 3
  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    flag = True
    if not(self.center.x - (.5 * self.side) < p.x < self.center.x + (.5 * self.side)):
      flag = False
    if not(self.center.y - (.5 * self.side) < p.y < self.center.y + (.5 * self.side)):
      flag = False
    if not(self.center.z - (.5 * self.side) < p.z < self.center.z + (.5 * self.side)):
      flag = False
    return flag


  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    new_cube = Cube(a_sphere.center.x, a_sphere.center.y, a_sphere.center.z, a_sphere.radius * 2)
    return self.is_inside_cube(new_cube)
  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    flag = True
    for vertex in other.vertices:
      if not self.is_inside_point(vertex):
        flag = False
    return flag
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):

    return self.center.distance(other.center) < (abs(self.center.distance(self.vertices[0])) + abs(other.center.distance(other.vertices[0]))) and \
            not self.is_inside_cube(other)

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    length = (.5 * self.side) + (.5 * other.side) - (abs(self.center.x - other.center.x))
    width = (.5 * self.side) + (.5 * other.side) - (abs(self.center.y - other.center.y))
    height = (.5 * self.side) + (.5 * other.side) - (abs(self.center.z - other.center.z))
    return length * width * height

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    radius = self.side / 2
    return Sphere(self.center.x, self.center.y, self.center.z, radius)
class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.center = Point(x, y, z)
    self.radius = radius
    self.height = height
  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return "Center: (" + str(self.center.x) + ", " + str(self.center.y) + ", " + str(self.center.z) + "), Side: " + str(
      self.radius) + ", Height: " + str(self.height)
  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius * self.radius))
  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return (math.pi * self.radius * self.radius * self.height)
  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if self.center.distance(p) < self.radius and (self.center.z - (self.height *.5)) < p.z < (self.center.z + (self.height *.5)):
      return True
    else:
      return False
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    new_cube = Cube(a_sphere.center.x, a_sphere.center.y, a_sphere.center.z, a_sphere.radius * 2)
    return self.is_inside_cube(new_cube)
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    flag = True
    for vertex in a_cube.vertices:
      if not self.is_inside_point(vertex):
        flag = False
    return flag
  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    return other.radius < self.radius and (self.center.distance(other.center)) < (self.radius - other.radius)


def main():
  # read data from standard input


  # read the coordinates of the first Point p
  coord1 = sys.stdin.readline()
  split1 = coord1.split(" ")
  # create a Point object
  p = Point(float(split1[0]), float(split1[1]), float(split1[2]))
  # read the coordinates of the second Point q
  coord2 = sys.stdin.readline()
  split2 = coord2.split(" ")
  # create a Point object
  q = Point(float(split2[0]), float(split2[1]), float(split2[2]))
  # read the coordinates of the center and radius of sphereA
  coord3 = sys.stdin.readline()
  split3 = coord3.split(" ")


  # create a Sphere object
  sphereA = Sphere(float(split3[0]), float(split3[1]), float(split3[2]), float(split3[3]))
  # read the coordinates of the center and radius of sphereB
  coord4 = sys.stdin.readline()
  split4 = coord4.split(" ")
  # create a Sphere object
  sphereB = Sphere(float(split4[0]), float(split4[1]), float(split4[2]), float(split4[3]))
  # read the coordinates of the center and side of cubeA
  coord5 = sys.stdin.readline()
  split5 = coord5.split(" ")
  # create a Cube object
  cubeA = Cube(float(split5[0]), float(split5[1]), float(split5[2]), float(split5[3]))
  # read the coordinates of the center and side of cubeB
  coord6 = sys.stdin.readline()
  split6 = coord6.split(" ")

  # create a Cube object
  cubeB = Cube(float(split6[0]), float(split6[1]), float(split6[2]), float(split6[3]))
  # read the coordinates of the center, radius and height of cylA
  coord7 = sys.stdin.readline()
  split7 = coord7.split(" ")
  # create a Cylinder object
  cylA = Cylinder(float(split7[0]), float(split7[1]), float(split7[2]), float(split7[3]))

  # read the coordinates of the center, radius and height of cylB
  coord8 = sys.stdin.readline()
  split8 = coord8.split(" ")
  # create a Cylinder object
  cylB = Cylinder(float(split8[0]), float(split8[1]), float(split8[2]), float(split8[3]))

  # print if the distance of p from the origin is greater
  # than the distance of q from the origin
  origin = Point()
  if p.distance(origin) > q.distance(origin):
    
  # print if Point p is inside sphereA
  print(sphereA.is_inside_point(p))
  # print if sphereB is inside sphereA
  print(sphereA.is_inside_sphere(sphereB))
  # print if cubeA is inside sphereA
  print(sphereA)
  # print if sphereA intersects with sphereB

  # print if cubeB intersects with sphereB

  # print if the volume of the largest Cube that is circumscribed
  # by sphereA is greater than the volume of cylA

  # print if Point p is inside cubeA

  # print if sphereA is inside cubeA

  # print if cubeB is inside cubeA

  # print if cubeA intersects with cubeB

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA

  # print if the surface area of the largest Sphere object inscribed
  # by cubeA is greater than the surface area of cylA

  # print if Point p is inside cylA

  # print if sphereA is inside cylA

  # print if cubeA is inside cylA
  print(pt1)
  print(pt2)
if __name__ == "__main__":
  main()
