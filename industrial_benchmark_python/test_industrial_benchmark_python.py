import unittest
from IDS import IDS
import numpy as np
from numpy import genfromtxt


class TestIB(unittest.TestCase):

    def test_example(self):
        # fixed seed for setpoint
        np.random.seed(501)
        p = []
        trajectories = 10
        T = 1000 # perform 1000 actions/ steps

        # generate different values of setpoint
        for value in range(10):
            p.append(np.random.randint(1, 100))

        # perform 1000 actions per trajectory
        for i in range(trajectories):
            # generate IB with fixed seed. If no seed is given, IB is generated with random values
            env = IDS(p[i], inital_seed=1005 + i)
            all_States = []
            operational_States = []

            for j in range(T):
                at = 2 * np.random.rand(3) - 1

                # perform action
                markovStates = env.step(at)
                # get results: all States and all operational costs
                #print(np.array(env.allStates()).tolist())
                all_States = all_States + (np.array(env.allStates()).tolist())
                operational_States.append(env.operational_cost_Buffer())

                # before the actual test: generate files with which all test files can be compared
            #np.savetxt('all_States'+str(i)+'.csv', all_States)
            #np.savetxt('operational_States'+str(i)+'.csv', operational_States)

            #all_States_np =np.asarray(all_States)
            np.savetxt('all_States_test' + str(i) + '.csv', all_States)
            np.savetxt('operational_States_test'+str(i)+'.csv', operational_States)



            # compare files
            compare_file_all_States = genfromtxt('all_States'+str(i)+'.csv', delimiter=',')
            compare_file_operational_States = genfromtxt('operational_States'+str(i)+'.csv', delimiter=',')


            # test files
            test_file_all_States = genfromtxt('all_States_test' + str(i) + '.csv', delimiter=',')
            test_operational_States = genfromtxt('operational_States_test' + str(i) + '.csv', delimiter=',')



            # test if test files and original files are equal
            np.testing.assert_array_almost_equal(compare_file_all_States, test_file_all_States)
            np.testing.assert_array_almost_equal(compare_file_operational_States, test_operational_States)

