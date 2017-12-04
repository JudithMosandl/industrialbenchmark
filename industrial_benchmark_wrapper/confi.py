import json
from pprint import pprint
import numpy as np


class config():

    def __init__(self):
        self.amount = 6 # amount of equations
        self.data = {
            "equation0": {
                "velocity": [('v', 0, -4.29), ('konstante',0, -5.50)],
                "gain": [('c', 2, -1), ('f', 2, 1)],
                "shift": [('h', 1, -1.92), ('h', 5, -2.59), ('p', 0, 2),('konstante',0,0.67)]

            },

            "equation1": {
                "velocity": [('v', 6, -1), ('konstante',0, -1.22)],
                "gain": [('c', 6, -2), ('f', 4, 2), ('g', 9, 1)],
                "shift": [('h', 3, -4.72), ('p', 0, 2), ('konstante',0, 0.69)]

            },
            "equation2": {
                "velocity": [('f', 0, 2), ('p', 0, -1), ('v', 12, -1)],
                "gain": [('f', 4, 1), ('p', 0, -0.44), ('konstante',0, 0.53)],
                "shift": [('h', 4, -2.50), ('p', 0, 1), ('konstante',0, 0.49)]

            },
            "equation3": {
                "velocity": [('f', 0, 1), ('v', 0, -1)],
                "gain": [('c', 14, -2.58), ('f', 3, 1.58), ('g', 18, 1)],
                "shift": [('h', 3, -4.47), ('p', 0, 2), ('konstante',0, 0.76)]

            },
            "equation4": {
                "velocity": [('v', 9, -1), ('konstante',0, -1.10)],
                "gain": [('c', 1, -2), ('f', 4, 2), ('g', 10, 1)],
                "shift": [('f', 4, -1), ('h', 3, -4.74), ('p', 0, 2.13)]

            },
            "equation5": {
                "velocity": [('v', 5, -1), ('konstante',0, -1.09)],
                "gain": [('f', 2, 1), ('f', 6, 1), ('p', 0, -1), ('konstante',0, 1.06)],
                "shift": [('h', 3, -6.92), ('p', 0, 3.46), ('konstante',0, 1.14)]

            }
        }
        data1 = {"equation0":{ "velocity":[('f', 0 , 2),('h', 1 , 5),('g', 6 , 10)],"shift": [('f', 6 , 2),('h', 3 , 9),('g', 1 , 9)],"gain": [('f', 1 , .10),('h', 5 , 3),('g', 0 , 7)]},"equation1":{ "velocity":[('f', 0 , 2),('h', 1 , 5),('g', 6 , 10)],"shift": [('f', 6 , 2),('h', 3 , 9),('g', 1 , 9)],"gain": [('f', 1 , .10),('h', 5 , 3),('g', 0 , 7)]}}


    def update_policy(self, states, policy):
        states = states
        i = policy
        # read all actions/ equations
        self.action_array = []
        array_velocity = self.data["equation" + str(i)]["velocity"]
        array_gain = self.data["equation" + str(i)]["gain"]
        array_shift = self.data["equation" + str(i)]["shift"]
        velocity = self.calculate_next_action(array_velocity, states)
        gain = self.calculate_next_action(array_gain, states)
        shift = self.calculate_next_action(array_shift, states)
        action = [np.tanh(velocity), np.tanh(gain), np.tanh(shift)]



        return action



    def update_policy_all(self, states):
        states = states
        # read all actions/ equations
        self.action_array = []
        for i in range(self.amount):
            array_velocity = self.data["equation" + str(i)]["velocity"]
            array_gain = self.data["equation" + str(i)]["gain"]
            array_shift = self.data["equation" + str(i)]["shift"]

            # calculate action i

            velocity = self.calculate_next_action(array_velocity, states)
            gain = self.calculate_next_action(array_gain, states)
            shift = self.calculate_next_action(array_shift, states)
            action = [velocity, gain, shift]
            self.action_array.append(action)
        return self.action_array


    def calculate_next_action(self, array, states):
        action = 0
        for j in range(len(array)):
            parameter = array[j][0]
            time = array[j][1]
            number = array[j][2]


            if parameter == 'f':
                action = action + number * states[time][4][1]
            elif parameter == 'v':
                action = action + number * states[time][1][1]
            elif parameter == 'h':
                action = action + number * states[time][3][1]
            elif parameter == 'p':
                action = action + number * states[time][0][1]
            elif parameter == 'g':
                action = action + number * states[time][2][1]
            elif parameter == 'c':
                action = action + number * states[time][5][1]
            else:
                action = action+number

        return action