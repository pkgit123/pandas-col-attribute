import pandas as pd
from operator import attrgetter

# create sample dataframe, two columns are dates
df_sample = pd.DataFrame({
    'col1': ['apple', 'banana', 'orange'],
    'date2': [pd.Timestamp('2020-01-01'), pd.Timestamp('2020-02-01'), pd.Timestamp('2020-03-01')],
    'date3': [pd.Timestamp('2017-01-01'), pd.Timestamp('2018-02-01'), pd.Timestamp('2019-03-01')],
})

# create another column that calculates the difference in two date columns ... result is timedelta object
df_sample['timedelta_dates'] = (df_sample['date2']-df_sample['date3'])

# convert to number (days) using .apply(attrgetter('attribute_name'))
df_sample['days_diff'] = df_sample['timedelta_dates'].apply(attrgetter('days'))

print(df_sample)
