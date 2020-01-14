# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

def run(name):
    print(f"{name} ran wild abandon!")
def swing(name):
    print(f"{name} loved to swing more than anything.")
def slide(name):
    print(f"{name} gets a running start and slides across the slick floor.")
def hide_and_seek(name):
    print(f"{name} is too good at hide and seek- they remain hidden for days!")


# For example, Jay ran like a fool! or Chantelle slid down the slide!.

# The following lists of children should be iterated, and the names sent to the appropriate functions.
running_kids = ["Pam", "Sam", "Andrea", "Will"]
for kids in running_kids:
    run(kids)
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
for kids in swinging_kids:
    swing(kids)
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
for kids in sliding_kids:
    slide(kids)
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"] 
for kids in hiding_kids:
    hide_and_seek(kids)