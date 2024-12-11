#### each individual form ###

# [ [course_1, lecturer_1, time_slot_1,hall],
#   [course_2, lecturer_2, time_slot_2,hall],
#   [course_3, lecturer_1, time_slot_3,hall], and so on ... ]
from fit import *
from select import *
from crossover import *
import random
import dash
from dash import dcc, html
from dash import dash_table
import pandas as pd

time_slots = [
    "Sat 8-10", "Sat 10-12", "Sat 12-2", "Sat 2-4", "Sat 4-6",
    "Sun 8-10", "Sun 10-12", "Sun 12-2", "Sun 2-4", "Sun 4-6",
    "Mon 8-10", "Mon 10-12", "Mon 12-2", "Mon 2-4", "Mon 4-6",
    "Tue 8-10", "Tue 10-12", "Tue 12-2", "Tue 2-4", "Tue 4-6",
    "Wed 8-10", "Wed 10-12", "Wed 12-2", "Wed 2-4", "Wed 4-6",
    "Thu 8-10", "Thu 10-12", "Thu 12-2", "Thu 2-4", "Thu 4-6"
]
lecturers = ["Amr Ghoneim", "Mohammed El-Saeed", "Marwa", "Walid Youssef", "Salwa", "ccc","ccc"]
halls = ["hall-1",
         "hall-2",
         "hall-3",
         "hall-4",
         "hall-5", "hall-6", "hall-7", "hall-8", "hall-9", "hall-10",
         "hall-11", "hall-12", "hall-13", "hall-14", "hall-15", "hall-16", "hall-17"]

# number of time slots per course
course_requirements = {
    "AI": 4,
    "ML": 6,
    "BD": 10,
    "IR": 2,
    "CON.": 10,
    "DB": 4
}


def visualize_timetable(timetable):
    """
    Visualizes a timetable using Dash.

    :param timetable: A list of lists where each sub-list represents a timetable entry
                      in the format [course, lecturer, time_slot, hall].
    """
    # Define column names
    columns = ["Course", "Lecturer", "Time Slot", "Hall"]

    # Convert timetable to a pandas DataFrame
    df = pd.DataFrame(timetable, columns=columns)

    # Create the Dash app
    app = dash.Dash(__name__)

    # Layout for the timetable
    app.layout = html.Div(
        [
            html.H1("Timetable Visualization", style={"textAlign": "center"}),
            dash_table.DataTable(
                data=df.to_dict("records"),
                columns=[{"name": col, "id": col} for col in df.columns],
                style_cell={
                    "textAlign": "center",
                    "fontFamily": "Arial",
                    "fontSize": "16px",
                },
                style_header={
                    "backgroundColor": "rgb(230, 230, 230)",
                    "fontWeight": "bold",
                },
                style_table={"margin": "20px auto", "width": "80%"},
            ),
        ]
    )

    # Run the app
    app.run_server(debug=True)


def generate_population(num_of_individuals):
    population = []

    for _ in range(num_of_individuals):

        individual = []

        for course, slots_needed in course_requirements.items():
            lecturer = random.choice(lecturers)  # assign a lecturer for each course randomly .
            for _ in range(slots_needed):
                hall = random.choice(halls)  # assign a hall for each lecture randomly .
                time_slot = random.choice(time_slots)  # assign a time slot  for each course randomly .

                individual.append([course, lecturer, time_slot, hall])
        population.append(individual)
    return population


#### TEST ####

population = generate_population(10000)
fitness_scores = fitness_scores(population)
