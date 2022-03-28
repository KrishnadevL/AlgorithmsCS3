from Code.TT1.fibonacci import fibonacci
from Code.TT2.factorial import Factorial

main_menu = [
  ["Fibonacci", "Code/TT1/fibonacci.py"],
  ["Factorial", "Code/TT2/factorial.py"],
  ["List", "list.py"]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
  ["Matrix", "Code/TT0/matrix.py"],
  ["Swap", "Code/TT0/sort.py"],
]

pattern_menu = [
  ["tree", "Code/TT0/tree.py"],
  ["ship", "Code/TT0/ship.py"],
	["bird", "Code/TT0/bird.py"],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["General", submenu])
    menu_list.append(["Patterns", patternmenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenuc():
  title = "Class Submenu" + banner
  m = submenus.Menu(title, sub_menu)
  m.menu()

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def patternmenu():
    title = "Function Submenu" + banner
    buildMenu(title, pattern_menu)

# builds console menu
def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user input
    choice = input("Type your choice> ")

    # Process user input
    try:
        choice = int(choice)
        if choice == 0:
            # stops
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                # check main_menu dictionary
                print(f"File not found!: {action}")
    except ValueError:
        # not a number 
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # not one of the numbers listed
        print(f"Invalid choice: {choice}")
  

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
