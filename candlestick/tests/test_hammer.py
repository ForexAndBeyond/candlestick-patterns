import unittest
import pandas as pd
from candlestick import candlestick


class TestHammer(unittest.TestCase):
    def test_hammer_pattern_not_detected(self):
        data = {'open': [10, 20, 30],
                'high': [15, 25, 35],
                'low': [5, 15, 25],
                'close': [15, 25, 35]}
        df = pd.DataFrame(data)
        target = 'hammer'
        candles_df = candlestick.hammer(df, target=target)
        self.assertTrue((candles_df['hammer'] == False).all())

    def test_green_hammer_pattern_detected(self):
        data = {'open': [35, 30, 25, 20],
            'high': [35, 35, 30, 25],
            'low': [10, 15, 10, 5],
            'close': [32, 25, 15, 20]}
        df = pd.DataFrame(data)
        target = 'hammer'
        candles_df = candlestick.hammer(df, target=target)
        self.assertTrue(candles_df['hammer'].iloc[0])

    def test_green_red_pattern_detected(self):
        data = {'open': [32, 30, 25, 20],
            'high': [35, 35, 30, 25],
            'low': [10, 15, 10, 5],
            'close': [35, 25, 15, 20]}
        df = pd.DataFrame(data)
        target = 'hammer'
        candles_df = candlestick.hammer(df, target=target)
        self.assertTrue(candles_df['hammer'].iloc[0])


if __name__ == '__main__':
    unittest.main()