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


if __name__ == '__main__':
    # plot1()
    # plot2()
