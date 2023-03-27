from candlestick.patterns.candlestick_finder import CandlestickFinder


class Hammer(CandlestickFinder):
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 1, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]

        close = candle[self.close_column]
        open = candle[self.open_column]
        high = candle[self.high_column]
        low = candle[self.low_column]

        is_long_lower_shadow = ((close - low) / (.001 + high - low) > 0.6)

        is_short_upper_shadow = ((open - low) / (.001 + high - low) > 0.6)

        return (((high - low) > 3 * (open - close)) and
                 is_long_lower_shadow and is_short_upper_shadow)
