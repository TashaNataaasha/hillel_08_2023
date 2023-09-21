from multiprocessing import Process
from threading import Thread

from kitchen import Kitchen, Dish, DishSize

pizza = Dish(
    name="Peperoni",
    size=DishSize.M,
    ingredients=["tomato", "cheese", "peperoni", "dough"],
)

salad = Dish(
    name="Caesar",
    size=DishSize.S,
    ingredients=["tomato", "cheese", "chicken", "dough"],
)


dishes = [pizza, salad]

if __name__ == "__main__":
    pass
    # main()

# regular execution
# for dish in dishes:
#     Kitchen.cook(dish)

# concurrent execution
# threads = [
#     Thread(
#         target=Kitchen.cook,
#         args=(dish,),
#     )
#     for dish in dishes
# ]

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

# processes
# tasks = [Process(target=Kitchen.cook, args=[dish]) for dish in dishes]

# for task in tasks:
#     task.start()

# for task in tasks:
#     task.join()