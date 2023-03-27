import unittest
import pandas as pd
from candlestick import candlestick


class TestInvertedHammer(unittest.TestCase):
    def test_inverted_hammer_pattern_not_detected(self):
        data = {'open': [10, 20, 30],
                'high': [15, 25, 35],
                'low': [5, 15, 25],
                'close': [15, 25, 35]}
        df = pd.DataFrame(data)
        target = 'inverted_hammer'
        candles_df = candlestick.inverted_hammer(df, target=target)
        self.assertTrue((candles_df['inverted_hammer'] == False).all())

    def test_red_inverted_hammer_pattern_detected(self):
        data = {'open': [30, 25, 20, 15],
                'high': [50, 30, 25, 25],
                'low': [25, 10, 5, 5],
                'close': [25, 15, 20, 20]}
        df = pd.DataFrame(data)
        target = 'inverted_hammer'
        candles_df = candlestick.inverted_hammer(df, target=target)
        self.assertTrue(candles_df['inverted_hammer'].iloc[0])

    def test_green_inverted_hammer_pattern_detected(self):
        data = {'open': [25, 25, 20, 15],
                'high': [50, 30, 25, 25],
                'low': [25, 10, 5, 5],
                'close': [30, 15, 20, 20]}
        df = pd.DataFrame(data)
        target = 'inverted_hammer'
        candles_df = candlestick.inverted_hammer(df, target=target)
        self.assertTrue(candles_df['inverted_hammer'].iloc[0])

if __name__ == '__main__':
    unittest.main()