# %%
from IPython.core.display import display, HTML
from string import Template
import pandas as pd
import json
import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# %%
from client.meta_data_client import MetaDataClient

cli = MetaDataClient("http://localhost:8000/graphql/")
cli.authenticate("test", "test1234")

objects = cli.get_time_series("activities", "distance", "start_date")
# %%
len(objects)

# %%
# Data for plotting

series = [(
    datetime(obj.datetimeAttributes[0].value),
    obj.floatAttributes[0].value
) for obj in filter(lambda x: hasattr(x, "datetimeAttributes"), objects)]

# %%

data = list(map(list, zip(*series)))

# %%

t = data[0]
s = data[1]

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='distance',
       title='About as simple as it gets, folks')
ax.grid()

plt.show()
