import numpy as np

def save_results(Bresults, Lresults, Presults):
    with open("results/bacteria_sim_results.txt", 'w') as output:
        for i in range(len(Bresults)):
            for j in range(len(Bresults[i])):
                output.write(str(Bresults[i][j]) + ',')

            output.write('\n')

    with open("results/inf_bacteria_sim_results.txt", "w") as output:
        for i in range(len(Lresults)):
            for j in range(len(Lresults[i])):
                output.write(str(Lresults[i][j]) + ',')

            output.write('\n')

    with open("results/phages_sim_run.txt", "w") as output:
        for i in range(len(Presults)):
            for j in range(len(Presults[i])):
                output.write(str(Presults[i][j]) + ',')

            output.write('\n')

    return


def read_file(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array

    f_array = process_array(words)

    return f_array


def process_array(words):
    array_temp = words

    array = []
    for i in range(len(array_temp)):
        array_tempp = str(array_temp[i])[:-1]
        array_string = array_tempp.split(",")
        array_float = [float(num) for num in array_string]
        array.append(array_float)

    return array
