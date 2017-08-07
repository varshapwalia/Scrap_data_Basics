# to concatenate csv files in order

import pandas
filenames = ["ANGEL_INDIA_ALL_email_5-05_first.csv", "ANGEL_INDIA_ALL_email_5-05_lastfew.csv"] # Fill in csv files to be concatenated.
df = pandas.DataFrame()
for filename in filenames:
    df = df.append(pandas.read_csv(filename))
df.to_csv('ANGEL_INDIA_ALL_emailids_weburls_6-05.csv', index=False, encoding="UTF-8") # Change the final concatenated file name
print 'done!'