# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
transactions_MES_filtered = dataiku.Dataset("transactions_MES_filtered")
transactions_MES_filtered_df = transactions_MES_filtered.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

output_df = transactions_MES_filtered_df # For this sample code, simply copy input to output


# Write recipe outputs
output = dataiku.Dataset("output")
output.write_with_schema(output_df)
