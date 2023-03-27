import unittest
import pandas as pd
from candlestick import candlestick


class TestBearishMarubozu(unittest.TestCase):
    
    def test_bullish_marubozu_pattern_not_detected(self):
        data = {'open': [30, 20, 10],
                'high': [35, 25, 15],
                'low': [25, 15, 5],
                'close': [25, 15, 5]}
        df = pd.DataFrame(data)
        target = 'bullish_marubozu'
        candles_df = candlestick.bullish_marubozu(df, target=target)
        self.assertTrue((candles_df['bullish_marubozu'] == False).all())

    def test_bullish_marubozu_pattern_detected(self):
        data = {'open': [10, 35, 25, 10],
                'high': [15, 40, 30, 25],
                'low': [5, 10, 15, 5],
                'close': [15, 40, 30, 25]}
        df = pd.DataFrame(data)
        target = 'bullish_marubozu'
        candles_df = candlestick.bullish_marubozu(df, target=target)
        self.assertTrue(candles_df['bullish_marubozu'].iloc[0])

    def test_bullish_marubozu_closing_pattern_detected(self):
        data = {'open': [10, 35, 25, 10],
                'high': [15, 40, 30, 37],
                'low': [5, 10, 15, 20],
                'close': [15, 40, 30, 37]}
        df = pd.DataFrame(data)
        target = 'bullish_closing_marubozu'
        candles_df = candlestick.bullish_marubozu(df, target=target)
        self.assertTrue(candles_df[target].iloc[0])

if __name__ == '__main__':
    unittest.main()