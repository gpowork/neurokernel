import numpy as np

class Connectivity:

    def __init__(self, mapping):

        self.in_module
        self.out_module

        # 2D array (bool) as shown below:
        #       out1  out2  out3  out4
        # in1 |  x  |  x  |     |  x
        # in2 |     |     |  x  |
        # in3 |     |  x  |     |  x
        if mapping.dtype <> bool:
            raise IOError, "You must provide a mapping as a numpy.darray with \
                            booleans"
        if mapping.ndim <> 2:
            raise IOError, "You must provide a 2D numpy.darray"
        self.map = mapping

        self.syn_parameters

    def add_connectivity(self, connectivity):
        self.connectivities.append(connectivity)

    def rm_connectivity(self, connecivity):
        self.connectivities.remove(connecivity)

    # Gets the output signal in the form (num_inputs, 1) and 
    def get_output(self):
        return self.in_module.neurons.V.get() * self.map

def main():
    m = np.asarray([[1, 1, 0, 1],
                    [0, 1, 0, 1],
                    [0, 0, 0, 1]], dtype = np.bool)
    m = Connectivity(m)
    m.get_output(np.asarray([[1.4, 3.2, 1.7]]))

if __name__ == '__main__':

    # number of neurons per type that will be multiplied by 15
    # average number of synapses per neuron 
    # parameters = 768, 6, 1e-4, 4608, 0, 4608, 0, 1
    main()
