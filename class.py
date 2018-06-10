# create base food class
class Food:

    def __init__(self, initial_x1, initial_x2, initial_y):
        # x1 value
        self.x1 = initial_x1
        # x2 value
        self.x2 = initial_x2
        # y value
        self.y = initial_y

    def check_on_plate(self, plate_x1, plate_x2):
        if (self.x2 < plate_x1 or self.x1 > plate_x2):
            return False
        else:
            return True
        
    def draw_food(self, screen):
        screen.create_rectangle(self.x1, self.y, self.x2, self.y2, fill="blue")

# create a butter class that is also a food
# we can use all the stuff that Food has in our Butter
class Butter(Food):
    
    image = "butter.jpg"
    
    def __init__(self, initial_x1, initial_x2, initial_y, image_url):
        # call the base food class to initialize the x and y values
        Food.__init__(self, initial_x1, initial_x2, initial_y)
        # String containing image url or whatever you want
        self.image = image_url

my_new_food = Food(1, 3, 10)
my_new_butter = Butter(6, 8, 10, "butter.jpg")
plate_x1 = 2
plate_x2 = 4
food = []
food.append(my_new_food)
food.append(my_new_butter)

def draw_all_food():
    for i in range(num):
        food[i].draw_food(s)


print("my_new_food :")
print(my_new_food.x1)
print(my_new_food.x2)
print(my_new_food.y)
print(my_new_food.check_on_plate(plate_x1, plate_x2))


print("my_new_butter :")
print(my_new_butter.x1)
print(my_new_butter.x2)
print(my_new_butter.y)
print(my_new_butter.image)
print(my_new_butter.check_on_plate(plate_x1, plate_x2))
