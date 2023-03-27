import unittest
import pandas as pd
from candlestick import candlestick


class TestBearishMarubozu(unittest.TestCase):
    
    def test_bearish_marubozu_pattern_not_detected(self):
        data = {'open': [10, 20, 30],
                'high': [15, 25, 35],
                'low': [5, 15, 25],
                'close': [15, 25, 35]}
        df = pd.DataFrame(data)
        target = 'bearish_marubozu'
        candles_df = candlestick.bearish_marubozu(df, target=target)
        self.assertTrue((candles_df['bearish_marubozu'] == False).all())

    def test_bearish_marubozu_pattern_detected(self):
        data = {'open': [35, 10, 25, 35],
            'high': [35, 25, 30, 40],
            'low': [10, 5, 15, 20],
            'close': [10, 10, 15, 20]}
        df = pd.DataFrame(data)
        target = 'bearish_marubozu'
        candles_df = candlestick.bearish_marubozu(df, target=target)
        self.assertTrue(candles_df['bearish_marubozu'].iloc[0])

    def test_bearish_marubozu_closing_pattern_detected(self):
        data = {'open': [35, 10, 25, 35],
                'high': [37, 25, 30, 40],
                'low': [10, 5, 15, 20],
                'close': [10, 10, 15, 20]}
        df = pd.DataFrame(data)
        target = 'bearish_closing_marubozu'
        candles_df = candlestick.bearish_marubozu(df, target=target)
        self.assertTrue(candles_df[target].iloc[0])

if __name__ == '__main__':
    unittest.main()