# These tests verify the material parser script performance
from eleread import data_parse
from nose.tools import assert_equal
from nose.tools import assert_raises

def density_test():
    file = open('elelib.std')
    data = data_parse(file)
    exp = str('0.899000E-04')
    obs = data['h']['Density']
    assert_equal(obs,exp)

def isotope_abundance_test():
    file = open('elelib.std')
    data = data_parse(file)
    exp = str('0.789900E+02')
    obs = data['mg']['Isotope Data']['24']['Abundance']
    assert_equal(obs,exp)
