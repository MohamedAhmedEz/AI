# find if lecturer assinged to more than time slot
def lecturer_timeSlot(individual):
    penalty = 0
    lecturer_time_slot = {}
    for course, lecturer, time_slot, hall in individual:
        if (lecturer, time_slot) in lecturer_time_slot:
            penalty += 1
        else:
            lecturer_time_slot[(lecturer, time_slot)] = course

    return penalty


# find if hall contain more than one slot in the same time
def hall_timeSlot(individual):
    penalty = 0
    hall_time_slot = {}
    for course, lecturer, time_slot, hall in individual:
        if (hall, time_slot) in hall_time_slot:
            penalty += 1
        else:
            hall_time_slot[(hall, time_slot)] = course

    return penalty


# find if the course is teached more than one in the same time slot
def course_timeSlot(individual):
    penalty = 0
    course_time_slot = {}
    for course, lecturer, time_slot, hall in individual:
        if (course, time_slot) in course_time_slot:
            penalty += 1
        else:
            course_time_slot[(course, time_slot)] = hall

    return penalty


# calculate the total score as a negative value (the less score is the worst )
def total_fitness_score(individual):
    lts = lecturer_timeSlot(individual)
    hts = hall_timeSlot(individual)
    cts = course_timeSlot(individual)

    total_score = lts + hts + cts

    return total_score


# calculate the fitness scores of all population
def fitness_scores(population):
    scr_lst = []
    for ind in population:
        scr_lst.append(total_fitness_score(ind))
    return scr_lst



def inverted_fitness(fitness_scores):
    # Invert the fitness values to favor individuals with lower fitness
    max_fitness = max(fitness_scores)
    inverted_scores = [max_fitness - fitness for fitness in fitness_scores]
    return inverted_scores