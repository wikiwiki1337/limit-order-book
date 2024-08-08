# limit_order_book.py
class LimitOrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []

    def add_order(self, side, price, size):
        if side == 'buy':
            self.bids.append((price, size))
            self.bids.sort(reverse=True)  # Highest bid price first
        elif side == 'sell':
            self.asks.append((price, size))
            self.asks.sort()  # Lowest ask price first

    def __str__(self):
        return f"Bids: {self.bids}\nAsks: {self.asks}"

# Create an instance of the order book and add some orders
lob = LimitOrderBook()
lob.add_order('buy', 100, 10)
lob.add_order('sell', 101, 5)
print(lob)
