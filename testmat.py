# These tests verify the material parser script performance
from matread import data_par
from nose.tools import assert_equal
from nose.tools import assert_raises

def density_test():
    file = open('matlib.std')
    data = data_par(file)
    exp = str('1.00')
    obs = data['water']['Density']
    assert_equal(obs,exp)

def massfrac_test():
    file = open('matlib.std')
    data = data_par(file)
    exp = str('0.73000e+00')
    obs = data['WALLOY']['Composition Data']['fe']['Mass Fraction']
    assert_equal(obs,exp)

def number_elements_test():
    file = open('matlib.std')
    data = data_par(file)
    exp = 9
    obs = data['R-EPXY']['Number of Elements']
    assert_equal(obs,exp)

