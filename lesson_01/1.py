# print ("Homework done")

# class Point:
#     color = "red"
#     circle = 2

# a = Point()
# a.color = "black"
# print(a.color)


# class Point:
#     def set_coords(self):
#         print("call set coords")
    

# pt = Point()
# pt.set_coords()

class Point:
    def set_coords(self, x,y):
        self.x = x
        self.y = y
        
pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)
