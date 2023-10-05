import turtle
import pandas
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
screen = turtle.Screen()
# screen.setup(width=1000, height=1000)
screen.title("U.S. States Game")
screen.bgcolor("black")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#  Use this to get co-ordinates on the map.
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
print(all_states)
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states Correct", prompt="What's another "
                                                                                             "state's name? ").title()

    # First check if the user's input is already in the guessed states
    if answer_state in guessed_states:
        # turtle.hideturtle()
        # turtle.penup()
        # turtle.goto(0, 450)
        # turtle.write(f"{answer_state}, already entered, enter another state", align=ALIGNMENT, font=FONT)
        continue
    # print(correct_state_data)  # This line is to see if the correct thing is being done.
    # print(f"{correct_state_data.x[0]}, {correct_state_data.y[0]}")
    # new_x = int(correct_state_data.x)
    # new_y = int(correct_state_data.y)
    if answer_state == "Exit":
        #  Check if every state is in the guessed state.
        missing_states = [state for state in all_states if state not in guessed_states]  # List to store all the states
        # the user couldn't enter using list comprehension.

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")  # Write to a csv, all the missing data.
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        correct_state_data = data[data.state == answer_state]  # Check and retrieve the row
        # that corresponds to the user's input
        new_turtle.goto(int(correct_state_data.x.iloc[0]), int(correct_state_data.y.iloc[0]))  # Get the x
        # and y values of
        # the retrieved row(state).
        new_turtle.write(correct_state_data.state.item())
# screen.exitonclick()
