from candlestick.patterns.candlestick_finder import CandlestickFinder

# Sort by most edge: https://analyzingalpha.com/candlestick-patterns
# https://analyzingalpha.com/bullish-marubozu-candlestick-pattern
# https://analyzingalpha.com/bullish-closing-marubozu
class BullishMarubozu(CandlestickFinder):
    """
        This class includes detecting both a bullish marubozu and a bullish closing
        marubozu pattern. A bullish marubozu pattern is a bullish candlestick pattern 
        with a long green (or white) body, little or no lower shadow, and a no upper 
        shadow. The closing price is equal to the high of the day, 
        indicating strong buying pressure. This pattern represents a strong 
        bullish sentiment in the market, with the bulls in control.
    """
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 1, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]

        close = candle[self.close_column]
        open = candle[self.open_column]
        high = candle[self.high_column]
        low = candle[self.low_column]

        # Conditions for a bullish marubozu pattern
        body_size = abs(close - open)
        is_bullish = close > open
        is_marubozu = body_size / (high - low) >= 0.9
        is_long_body = body_size >= 0.7 * (high - low)

        # Conditions for a bullish closing marubozu pattern
        is_closing_marubozu = close == high and is_bullish and (high - low) >= 0.9 * body_size

        return (is_bullish and is_marubozu and is_long_body) or is_closing_marubozu