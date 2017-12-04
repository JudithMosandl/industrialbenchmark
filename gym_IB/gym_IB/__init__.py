from gym.envs.registration import register

register(
    id='gym_IB',
    entry_point='gym_IB.envs:IB_env',#industrial_benchmark_python:IDS
)
