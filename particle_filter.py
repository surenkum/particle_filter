'''
Main class which includes various variants of particle filter
'''


class Particle_Filter():

    def __init__(self,process_model,observation_model):
        self.num_samples = _num_samples # Total number of samples
        self.curr_samples = None # Current samples
        # Initialize current weights
        self.curr_weights = (1.0/self.num_samples)*np.ones((self.num_samples,))

    
    # Normalize and make sure the weights add to 1
    def renormalize_weights(self):
        self.curr_weights = (1.0/np.sum(self.curr_weights))*self.curr_weights

    def resample(self):


