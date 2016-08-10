'''
This function implements the example in the paper 
A Tutorial on Particle Filters for Online
Nonlinear/Non-Gaussian Bayesian Tracking
M. Sanjeev Arulampalam, Simon Maskell, Neil Gordon, and Tim Clapp
'''

import numpy as np

'''
Models Equation 79 from the reference paper
Noise Less dynamics model of the process
'''
def dynamics_model(prev_state,curr_time):
    curr_state = prev_state*0.5+((25*prev_state)/(1+prev_state**2))+\
            8*np.cos(1.2*curr_time)
    return curr_state

'''
Noise less observation model of the process
'''
def observation_model(curr_state):
    obs = (curr_state**2)/(20.0)
    return obs

'''
Sampling the dynamics model
'''
def sample_dynamics(prev_state,curr_time,num_samples,Q_var = 10):
    samples = np.sqrt(Q_var)*np.random.randn(num_samples)+\
            dynamics_model(prev_state,curr_time)
    return samples

'''
Sampling the observation model
'''
def sample_observation_model(curr_state,curr_time,num_samples,R_var = 1):
    samples = np.sqrt(R_var)*np.random.randn(num_samples)+\
            observation_model(curr_state,curr_time)
    return samples


