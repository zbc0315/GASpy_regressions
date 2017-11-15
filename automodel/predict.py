
# coding: utf-8

# In[ ]:

# Importing
import pdb
import sys
from gaspy_regress.regressor import GASpyRegressor
from gaspy_regress import gpickle, plot, transform
sys.path.insert(0, '../')
from gaspy.utils import vasp_settings_to_str

VASP_SETTINGS = vasp_settings_to_str({'gga': 'RP',
                                      'pp_version': '5.4',
                                      'encut': 350})


# In[ ]:

import copy
from tpot import TPOTRegressor
from sklearn.gaussian_process import GaussianProcessRegressor


# In[ ]:

model_name = 'GP_around_TPOT'
features = ['coordcount']
outer_features = ['neighbors_coordcounts']
responses = ['energy']
blocks = ['adsorbate']
fingerprints = {'neighborcoord': '$processed_data.fp_final.neighborcoord'}


# In[ ]:

H = gpickle.load_model(model_name, features+outer_features, responses, blocks)


# In[ ]:

regressor = H
regressor_block = ('CO',)
adsorbate = 'CO'
excel_file_path = 'volcanos_parsed.xlsx'
system = 'CO2RR'
scale = 'log'


# In[ ]:

data = transform.volcano(H, regressor_block, system, excel_file_path, scale, 'CO')


# In[ ]:

gpickle.dump_predictions(data, regressor=H, system=system)

