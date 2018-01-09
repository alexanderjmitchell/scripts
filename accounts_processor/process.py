"""Accounts processor

Usage:
    process.py <input> <output>
"""
from docopt import docopt

import pandas as pd
from pandas import np

from scripts.accounts_processor import subcategories

if __name__ == '__main__':
    args = docopt(__doc__)
    accounts_data = pd.read_csv(args['<input>'], skiprows=4, encoding='latin_1')

    accounts_data['category'] = np.nan
    accounts_data['Description'] = accounts_data['Description'].str.lower()

    for subcategory in subcategories.all_subcategories:
        accounts_data.loc[accounts_data['Description'].str.contains(subcategory.description_regex),
                          'category'] = str(subcategory.category)

    print(accounts_data[accounts_data.category.notnull()])
