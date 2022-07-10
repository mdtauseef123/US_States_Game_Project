import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
attempts = 1
correct_attempt = 0
guessed_states = []
data = pandas.read_csv("50_states.csv")
states_names = data["state"].to_list()
while attempts <= 50:
    answer_state = screen.textinput(title=f"{correct_attempt}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in states_names:
        guessed_states.append(answer_state)
        correct_attempt += 1
        state_move = turtle.Turtle()
        state_move.penup()
        state_move.hideturtle()
        state_move.color("black")
        ans_state = data[data.state == answer_state]
        x_pos = int(ans_state["x"])
        y_pos = int(ans_state["y"])
        state_move.goto(x=x_pos, y=y_pos)
        state_move.write(f"{answer_state}", align="center", font=('Arial', 8, 'normal'))
    attempts += 1

missed_states = []
for state in states_names:
    if state not in guessed_states:
        missed_states.append(state)

missed_states_data = pandas.DataFrame(missed_states)
missed_states_data.to_csv("states_to_learn.csv")
#As the user hit Exit then the gaming console should end without even a click, so we commented below line
#screen.exitonclick()
