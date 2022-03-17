import sys
import os

import pandas as pd


def main():
    if len(sys.argv) < 2:
        raise ValueError('args')

    args = sys.argv[1:]
    root_url = args[0]

    if len(args) > 1:
        output_dirpath = args[1]
    else:
        output_dirpath = os.path.join('.', 'out')
        if not os.path.exists(output_dirpath):
            os.mkdir(output_dirpath)

    csv_endpoint = '/clients.csv'
    clients_endpoint = root_url + csv_endpoint
    print(clients_endpoint)

    df = pd.read_csv(clients_endpoint, delimiter=',')
    features = df.columns
    print(features)
    clients = df.drop(columns=['sponsor', 'leader', 'startDate', 'endDate'])
    clients = clients.convert_dtypes()
    print(clients.dtypes)

    sponsorship = df.loc[:, ['id', 'login', 'sponsor', 'startDate', 'endDate']]
    leadership = df.loc[:, ['id', 'login', 'startDate', 'endDate']]

    clients.to_csv(os.path.join(output_dirpath, 'clients.csv'), index=False)
    sponsorship.to_csv(os.path.join(output_dirpath, 'sponsorship.csv'), index=False)
    leadership.to_csv(os.path.join(output_dirpath, 'leadership.csv'), index=False)


if __name__ == '__main__':
    main()
