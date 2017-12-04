from interpreter import  interpreter
import numpy as np
from model import model
from confi import  config

class agent():

    def __init__(self, size):
        print('Create Agent')
        self.size = size
        self.setpoint = 50
        self.reward_type = 'classic'
        self.action_type = "discrete"
        self.norm_m = np.array([55.0, 48.7503491, 50.5338077, 49.45048688, 37.50845543, -278.8565897, -166.3312234, 166.3312234])
        self.norm_s = np.array([28.72281323, 12.3103933, 29.90922786, 29.22029113, 31.17247278, 122.0338114, -139.4381673, 139.4381673 ])
        self.interpreter = interpreter(self.setpoint, self.reward_type, self.action_type)
        self.model = model()
        self.observation = self.interpreter.step(2 * np.random.rand(3) - 1)
        self.buffer_states = (self.observation)
        self.equations = config()

        # Buffer inizialisieren mit 30 states und random action
        for buffer in range(size):
            action =  2 * np.random.rand(3) - 1
            self.observation = self.interpreter.step(action)
            for value in range(len(self.observation)):
                # norm_observation.append(self.observation[value][1])
                self.observation[value][1] = (self.observation[value][1] - self.norm_m[value]) / self.norm_s[value]
            self.buffer_states = np.vstack([self.buffer_states, self.observation])

        #print((self.buffer_states))
        self.perform_policy()



    def perform_policy(self, n_trajectories = 1, T = 1000):

        #self.state = np.array(self.buffer_states)
        self.data = np.zeros((n_trajectories, T))


        for k in range(n_trajectories):
            self.interpreter = interpreter(self.setpoint, self.reward_type, self.action_type)
            for t in range(T):
                # Interactionprocess with Interpreter: config, step, observer
                self.interaction_env()
                self.data[k, t] = self.interpreter.env.visibleState()[-1]



    def interaction_env(self):

        #---------------------------------per config---------------------------
        #actions = self.equations.update_policy_all(self.buffer_states)
        policy = 5
        action_one = self.equations.update_policy(self.buffer_states, policy)
        print(action_one)
        # perform action and observe state --> policy 0
        #---------------------------------per hand-----------------------------
        print("per hand")
        velo = -4.29 * self.buffer_states[0][1][1] - 5.50
        gain = -self.buffer_states[2][5][1] + self.buffer_states[2][4][1]
        shift = (-1.92)*self.buffer_states[1][3][1]-2.59*self.buffer_states[5][3][1]+2*self.buffer_states[0][0][1]+0.67
        action_hand = [velo, gain, shift]
        print(action_hand)
        #---------------------------------per hand-----------------------------
        action_random = 2 * np.random.rand(3) - 1
        self.observation = self.interpreter.step(action_one)#actions[0])

        # norm observation
        print("observation")
        norm_observation = []
        for value in range(len(self.observation)):
            #norm_observation.append(self.observation[value][1])
            self.observation[value][1] = (self.observation[value][1] - self.norm_m[value]) / self.norm_s[value]
        #norm_observation_np = (norm_observation_np - self.norm_m)/self.norm_s


        # save new state
        self.buffer_states = np.delete(self.buffer_states, 0,0)
        self.buffer_states = np.vstack([self.buffer_states, self.observation])












