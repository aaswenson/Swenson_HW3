# These tests verify the material parser script performance
from matread import data_par
from nose.tools import assert_equal
from nose.tools import assert_raises

def density():
    file = open('matlib.std')
    data = data_par(file)
    exp = 1.00
    obs = data['water']['Density']
    assert_equal(obs,exp)

def massfrac():
    file = open('matlib.std')
    data = data_par(file)
    exp = str('0.73000e+00')
    obs = data['WALLOY']['Composition Data']['Fe']['Mass Fraction']
    assert_equal(obs,exp)
