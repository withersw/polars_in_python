# %%
import polars as pl
from pyarrow import csv
import pyarrow.parquet as pq
# %%
# Let's try to read in the csv at "../data/API_Download_DS2_en_csv_v2_5657328.csv"
# that we downloaded from the world bank about varied country metrics.
# First using native polars

# %%
# it will default to only reading in two columns as the first row has meta information in two cells.
pl.read_csv("../data/API_Download_DS2_en_csv_v2_5657328.csv",  truncate_ragged_lines=True)

# %%
# now we get the data read in.  However, it isn't handling the column types correctly `skip_rows=4`

# %%
# Notice that the world health leaves missing as blanks in the csv. We need to explain that blanks aren't strings but missing values. `null_values=""`

# %%
# We don't like the World Banks wide format.  Let's clean it upt to long format. `dat.melt()`


# %%
# Now let's save our partially cleaned file as a csv and a parquet file `dat_long.write_csv("../data/long.csv")`
