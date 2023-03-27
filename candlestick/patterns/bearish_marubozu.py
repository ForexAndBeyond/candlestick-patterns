from candlestick.patterns.candlestick_finder import CandlestickFinder

# Sort by most edge: https://analyzingalpha.com/candlestick-patterns
# https://analyzingalpha.com/bearish-marubozu-candlestick-pattern
# https://analyzingalpha.com/bearish-closing-marubozu-candlestick-pattern
class BearishMarubozu(CandlestickFinder):
    """
        This class includes detecting both a bearish marubozu and a bearish closing
        marubozu pattern. A bearish marubozu pattern is a bearish candlestick pattern 
        with a long red (or black) body, little or no upper shadow, and a no lower 
        shadow. The closing price is equal to the low of the day, 
        indicating strong selling pressure. This pattern represents a strong 
        bearish sentiment in the market, with the bears in control.
    """
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 1, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]

        close = candle[self.close_column]
        open = candle[self.open_column]
        high = candle[self.high_column]
        low = candle[self.low_column]

        # Conditions for a bearish marubozu pattern
        body_size = abs(close - open)
        is_bearish = open > close
        is_marubozu = body_size / (high - low) >= 0.9
        is_long_body = body_size >= 0.7 * (high - low)

        # Conditions for a bullish closing marubozu pattern
        is_closing_marubozu = close == high and is_bearish and (high - low) >= 0.9 * body_size

        return (is_bearish and is_marubozu and is_long_body) or is_closing_marubozu
