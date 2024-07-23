#!/usr/bin/python3
"""Module for calculating minimal coin change"""


def makeChange(coins, total):
    """Calculate the fewest coins needed to reach a given total"""
    if total <= 0:
        return 0
    remAmt = total
    coinCnt = 0
    coinIdx = 0
    srtCoins = sorted(coins, reverse=True)
    numCoins = len(coins)
    while remAmt > 0:
        if coinIdx >= numCoins:
            return -1
        if remAmt - srtCoins[coinIdx] >= 0:
            remAmt -= srtCoins[coinIdx]
            coinCnt += 1
        else:
            coinIdx += 1
    return coinCnt
