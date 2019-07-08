import json

import numpy as np
import os

import pandas as pd
import sys
import glob
import matplotlib.pyplot as plt
import util

# utils
a = plt.axes()
sl = util.check_system()['sl']


def start_point():
    folder = 'results/start_point'
    os.makedirs(folder, exist_ok=True)

    start_pos = dict(user=[],
                     sample=[])

    for file in glob.glob('head_movement/*.csv'):
        pathname = util.Pathname(file)
        df = pd.read_csv(file)

        # Find current user
        user, seq = pathname.name.split('_')
        start_pos['user'].append(user)

        # The roll is the better marker for the starter sample
        der_roll = np.gradient(df['correctedRoll'])
        max_droll = der_roll.max()
        position = np.where(der_roll == max_droll)[0][0] + 1
        start_pos['sample'].append(position)

        print(f'User = {user}, position = {position}, roll_value = {df["correctedRoll"][position]}')

    df_start_pos = pd.DataFrame(start_pos)
    df_start_pos.to_csv(f'{folder}{sl}starter_samples.csv', index=False)


def plot2():
    '''
    Plot derivate of corrected samples
    :return:
    '''
    for file in glob.glob('head_movement/*.csv'):
        df = pd.read_csv(file)
        folder = 'results/plot2'
        os.makedirs(folder, exist_ok=True)

        name = os.path.basename(file)
        name = os.path.splitext(name)[0]

        # I=['dt',
        #    'rawTX', 'rawTY', 'rawTZ',
        #    'rawYaw', 'rawPitch', 'rawRoll',
        #    'correctedTX', 'correctedTY', 'correctedTZ',
        #    'correctedYaw', 'correctedPitch', 'correctedRoll',
        #    'filteredTX', 'filteredTY', 'filteredTZ',
        #    'filteredYaw', 'filteredPitch', 'filteredRoll',
        #    'mappedTX', 'mappedTY', 'mappedTZ',
        #    'mappedYaw', 'mappedPitch', 'mappedRoll']

        plt.close()
        fig, ax = plt.subplots(3, 1, sharex='all', dpi=100, figsize=(6, 6))
        ax[0].plot(np.gradient(df['correctedYaw']))
        ax[1].plot(np.gradient(df['correctedPitch']))
        ax[2].plot(np.gradient(df['correctedRoll']))

        ax[0].set_title('derivate of corrected samples')
        ax[2].set_xlabel('samples')

        name_corrected = f'{folder}/{name}_derivate'
        fig.savefig(name_corrected, transparent=True)
        # plt.show()

        print('')


def plot1():
    for file in glob.glob('head_movement/*.csv'):
        df = pd.read_csv(file)
        folder = 'results/plot1'
        os.makedirs(folder, exist_ok=True)

        name = os.path.basename(file)
        name = os.path.splitext(name)[0]

        # I=['dt',
        #    'rawTX', 'rawTY', 'rawTZ',
        #    'rawYaw', 'rawPitch', 'rawRoll',
        #    'correctedTX', 'correctedTY', 'correctedTZ',
        #    'correctedYaw', 'correctedPitch', 'correctedRoll',
        #    'filteredTX', 'filteredTY', 'filteredTZ',
        #    'filteredYaw', 'filteredPitch', 'filteredRoll',
        #    'mappedTX', 'mappedTY', 'mappedTZ',
        #    'mappedYaw', 'mappedPitch', 'mappedRoll']

        # Plotando amostras Raw
        plt.close()
        fig, ax = plt.subplots(3, 1, sharex='all', dpi=100, figsize=(6, 6))
        ax[0].plot(df['rawYaw'])
        ax[1].plot(df['rawPitch'])
        ax[2].plot(df['rawRoll'])

        ax[0].set_title('raw measures')
        ax[2].set_xlabel('samples')

        name_raw = f'{folder}/{name}_raw'
        fig.savefig(name_raw, transparent=True)
        # plt.show()

        # Plotando amostras Corrected
        plt.close()
        fig, ax = plt.subplots(3, 1, sharex='all', dpi=100, figsize=(6, 6))
        ax[0].plot(df['correctedYaw'])
        ax[1].plot(df['correctedPitch'])
        ax[2].plot(df['correctedRoll'])

        ax[0].set_title('corrected measures')
        ax[2].set_xlabel('samples')

        name_corrected = f'{folder}/{name}_corr'
        fig.savefig(name_corrected, transparent=True)
        # plt.show()

        # Plotando amostras mapped
        plt.close()
        fig, ax = plt.subplots(3, 1, sharex='all', dpi=100, figsize=(6, 6))
        ax[0].plot(df['mappedYaw'])
        ax[1].plot(df['mappedPitch'])
        ax[2].plot(df['mappedRoll'])

        ax[0].set_title('mapped measures')
        ax[2].set_xlabel('samples')

        name_mapped = f'{folder}/{name}_mapped'
        fig.savefig(name_mapped, transparent=True)
        # plt.show()
        print('')


def crop_samples():
    folder = 'results/cropped_samples'
    os.makedirs(folder, exist_ok=True)

    df_start_pos = pd.read_csv(f'results/start_point/starter_samples.csv', index_col=0)

    for file in glob.glob('head_movement/*.csv'):
        pathname = util.Pathname(file)
        df = pd.read_csv(file)

        # Find current user
        user = int(pathname.name.split('_')[0])
        # catch his position
        start_pos = int(df_start_pos.loc[user])
        # slice dataframe starting from his position
        new_df = df.loc[start_pos:][['rawYaw', 'rawPitch', 'rawRoll',
                                     'correctedYaw', 'correctedPitch', 'correctedRoll',
                                     'filteredYaw', 'filteredPitch', 'filteredRoll',
                                     'mappedYaw', 'mappedPitch', 'mappedRoll']]
        # saving dataframe
        print(f'Saving {pathname.name}.')
        new_df.to_csv(f'{folder}/{pathname.name}.csv', index=False)


if __name__ == '__main__':
    # plot1()
    # plot2()
    # start_point()
    crop_samples()
