import requests
import pandas as pd
import sys
import os


def main():
    if len(sys.argv) < 2:
        raise ValueError('args')

    args = sys.argv[1:]
    root_url = args[0]
    output_path = args[1] if len(args) > 1 else os.path.join('.', 'tmp')
    csv_endpoint = '/clients.csv'
    clients_endpoint = root_url + csv_endpoint
    print(clients_endpoint)

    df = pd.read_csv(clients_endpoint)
    features = df.columns
    print(features)
    clients = df.drop(columns=['sponsor', 'leader', 'startDate', 'endDate'])
    sponsorship = df.loc[:, ['id', 'login', 'sponsor', 'startDate', 'endDate']]
    leadership = df.loc[:, ['id', 'login', 'startDate', 'endDate']]

    clients.to_csv(os.path.join(output_path, 'clients.csv'))
    sponsorship.to_csv(os.path.join(output_path, 'sponsorship.csv'))
    leadership.to_csv(os.path.join(output_path, 'leadership.csv'))


if __name__ == '__main__':
    main()
