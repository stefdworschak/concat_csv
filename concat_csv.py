import argparse
from argparse import RawTextHelpFormatter
import os
import pandas as pd

FF_DEFAULT = 'file1.csv'
SF_DEFAULT = 'file2.csv'
DEFAULT_JOIN = 'outer'

def main():
    parser = argparse.ArgumentParser(description='Concatenating two csv files',
                                     formatter_class=RawTextHelpFormatter)

    parser.add_argument('-ff', '--first_file',
                        action='store',
                        help='path to first file. default: ./file1.csv',
                        #required=True
                        )
    parser.add_argument('-sf', '--second_file',
                        action='store',
                        help='path to second file. default: ./file2.csv',
                        #required=True
                        )
    parser.add_argument('-c', '--col',
                        action='store',
                        nargs='+', 
                        help=('column to use for merge (needs to be the same\n'
                              'in both files if `-scol` is not specified)'),
                        required=True)
    parser.add_argument('-scol', '--second_col',
                        action='store',
                        nargs='+',
                        help=('column in the second file to use for merge\n'
                              'if they are not the same'))
    parser.add_argument('-j', '--join',
                        action='store',
                        help=('type of join (left, right, outer, inner).'
                              ' default: outer'))
    args = parser.parse_args()

    first_file = args.first_file or FF_DEFAULT
    second_file = args.second_file or SF_DEFAULT
    join = args.join or DEFAULT_JOIN

    df1 = pd.read_csv(first_file)
    df2 = pd.read_csv(second_file)


    if args.second_col:

        if len(args.col) != len(args.second_col):
            raise ValueError('Not the same number of columns provided in col and second_col.')

        if isinstance(args.second_col, str):
            args.second_col = [args.second_col]

        for idx, scol in enumerate(args.second_col):
            if args.col[idx] not in list(df2.columns):
                print(str(args.col[idx]))
                print(list(df2.columns))
                print(str(args.col[idx]) not in list(df2.columns))
                df2.rename(columns={scol: args.col[idx]}, inplace=True)

    
    merged_df = df1.merge(df2, how=join, on=args.col)
    merged_df.to_csv('merged_results.csv', index=False)
    print("Succesfully merged files.")

if __name__ == '__main__':
    main()