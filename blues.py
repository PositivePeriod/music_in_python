#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

import numpy as np
from scipy.io import wavfile

import utils

seed = random.randint(10000, 100000)
seed = 89891

version = '1.0'
weightList = [9, 9, 3, 2, 1]

version = '1.1'
noteNum = [2, 3, 4, 3, 4, 1, 5, 3, 4, 5]

version = '1.2'
noteNums = [
    [2, 3, 4, 3, 4, 1, 5, 3, 4, 5, 5, 5, 3, 3, 2, 1],
    [2, 4, 6, 4, 2, 3, 4, 3, 3, 2, 1, 2, 4, 5, 6, 3],
    [2, 4, 3, 4, 5, 4, 6, 3, 2, 4, 3, 4, 5, 4, 6, 3],
]

version = '1.3'
noteA = [
    [2, 3, 4, 3, 4, 1, 5, 3, 4, 5, 5, 5, 3, 3, 2, 1],
    [2, 4, 6, 4, 2, 3, 4, 3, 3, 2, 1, 2, 4, 5, 6, 3],
    [2, 4, 3, 4, 5, 4, 6, 3, 2, 4, 3, 4, 5, 4, 6, 3],
]
noteB = [
    [1, 6, 5, 4, 2, 1, 6, 4, 3, 2, 1, 5, 4, 2, 1, 2],
    [1, 1, 2, 1, 3, 4, 1, 2, 2, 2, 3, 2, 4, 5, 2, 1],
]
noteC = [
    [0, 1, 2, 2, 1, 2, 0, 3, 4, 5, 4, 5, 3, 4, 3, 2],
    [1, 2, 3, 3, 2, 3, 1, 4, 5, 6, 5, 6, 4, 5, 4, 3],
    [2, 3, 4, 4, 3, 4, 2, 5, 6, 5, 6, 5, 4, 6, 2, 1],
]
noteD = [
    [0, 2, 1, 4, 5, 3, 1, 3, 2, 5, 6, 4, 2, 1, 0, 1],
    [2, 0, 3, 4, 3, 5, 5, 6, 4, 2, 1, 0, 1, 3, 2, 2],
]
noteE = [ # twinkle little star
    [5, 3, 3, 5, 3, 1, 2, 4, 2, 1, 3, 5, 1, 5, 1, 3],
    [5, 3, 3, 5, 3, 1, 2, 4, 5, 3, 3, 5, 3, 1, 2, 4],
    [2, 1, 3, 5, 1, 5, 1, 3, 2, 1, 3, 5, 1, 5, 1, 3],
]
noteF = [

]

noteLibStr = 'E'
noteLib = noteE

version = '1.0'
random.seed(seed)

if version == '1.0':
    fileName = f'music/blues_v{version}_{seed}_{weightList}.wav'
elif version == '1.1':
    fileName = f'music/blues_v{version}_{seed}_{noteNum}.wav'
elif version == '1.2':
    fileName = f'music/blues_v{version}_{seed}_{noteNums}.wav'
elif version == '1.3':
    fileName = f'music/blues_v{version}_{seed}_{noteLibStr}.wav'

# 다 라 마 바 사 가 나
# C  D  E  F  G  A  B
# do re mi fa so ra si

A = ['F4', 'g4', 'a4', 'B4', 'C5', 'd5', 'F5']
B = ['G4', 'a4', 'C5', 'c5', 'D5', 'F5', 'G5']
C = ['C4', 'd4', 'F4', 'f4', 'G4', 'a4', 'C5']
# F7 = Bb7 = A, GM7 = B, C7 = C


def randomNote(scale, num):
    return random.choices(scale, weights=[1]*len(scale), k=num)


def randomDuration(length):
    # one bar = 4
    if length == 0:
        return []
    else:
        action = [x for x in [0.25, 0.5, 1, 1.5, 2] if x <= length]
        selectedAction = random.choices(
            action, weights=weightList[:len(action)], k=1)[0]
        return [selectedAction] + randomDuration(length - selectedAction)


def randomMelody():
    scales = [A, A, A, A, A, A, A, A, B, C, A, C]
    note = []
    duration = []
    for scale in scales:
        deltaDuration = randomDuration(4)
        deltaNote = randomNote(scale, len(deltaDuration))
        duration += deltaDuration
        note += deltaNote
        print(deltaNote, deltaDuration)
    return note, duration


def makeMelody():
    scales = [A, A, A, A, A, A, A, A, B, C, A, C]
    note = []
    duration = []
    for scale in scales:
        deltaDuration = randomDuration(4)
        deltaNote = [scale[noteNum[i]] for i in range(len(deltaDuration))]
        duration += deltaDuration
        note += deltaNote
    return note, duration


def makeMelody2():
    scales = [A, A, A, A, A, A, A, A, B, C, A, C]
    note = []
    duration = []
    for scale in scales:
        deltaDuration = randomDuration(4)
        usedNoteNum = random.choice(noteNums)
        for i in range(len(deltaDuration)):
            deltaNote = [scale[usedNoteNum[i]]
                         for i in range(len(deltaDuration))]
        duration += deltaDuration
        note += deltaNote
    return note, duration


def makeMelody3():
    scales = [A, A, A, A, A, A, A, A, B, C, A, C]
    note = []
    duration = []
    for scale in scales:
        deltaDuration = randomDuration(4)
        usedNoteNum = random.choice(noteLib)
        for i in range(len(deltaDuration)):
            deltaNote = [scale[usedNoteNum[i]]
                         for i in range(len(deltaDuration))]
        duration += deltaDuration
        note += deltaNote
    return note, duration


def melody():
    note = A * 8 + B + C + A + C
    duration = [1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] * 12
    return note, duration


def bg():
    note = [
        'F4', 'a4', 'F4', 'F4',
        'a4', 'a4', 'F4', 'F4',
        'G4', 'C4', 'F4', 'C4'
    ]
    duration = [4] * 12
    return note, duration


if version == '1.0':
    melodyNote, melodyDuration = randomMelody()
elif version == '1.1':
    melodyNote, melodyDuration = makeMelody()
elif version == '1.2':
    melodyNote, melodyDuration = makeMelody2()
elif version == '1.3':
    melodyNote, melodyDuration = makeMelody3()

bgNote, bgDuration = bg()

factor = [0.68, 0.26, 0.03, 0., 0.03]
length = [0.01, 0.6, 0.29, 0.1]
decay = [0.05, 0.02, 0.005, 0.1]
sustain_level = 0.1

melodyData = utils.get_song_data(
    melodyNote, melodyDuration, 4, factor, length, decay, sustain_level)
bgData = utils.get_song_data(
    bgNote, bgDuration, 4, factor, length, decay, sustain_level)
data = melodyData + bgData
data = data * (4096/np.max(data))
# exit()

print(seed)
wavfile.write(fileName, 44100, data.astype(np.int16))
