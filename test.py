import randomizer
import gym
import numpy as np
from randomizer.wrappers import RandomizedEnvWrapper
import time

env_name = 'FetchPushRandomizedEnv-v0'


env=RandomizedEnvWrapper(gym.make(env_name), seed=123)
# env=gym.make('HalfCheetah-v2')q
# params = env.randomize(env.randomized_default, return_env_params=True)
obs = env.reset()
for i in range(2000):
    obs, r, done, _ = env.step(np.zeros(1))
    env.render()
    if done:
        env.reset()
    # if i % 100 == 0:
    #     params = env.randomize(env.randomized_default, return_env_params=True)
    #     env.reset()
