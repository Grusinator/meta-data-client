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


# %%
metaobj = cli.get_all_objects(schema_label="strava")

# %%
objects = cli.get_time_series("activities", "duration", "start_date")
# %%
len(objects)

# %%

url = cli.export_schema_to_rdf("strava")

url

# %%
# Data for plotting

series = [(
    obj.datetimeAttributes[0].value,
    obj.floatAttributes[0].value
) for obj in objects]

# filter(
#     lambda x: hasattr(x, "datetimeAttributes") and
#     hasattr(x, "floatAttributes"),

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

# %%

series[5:]
