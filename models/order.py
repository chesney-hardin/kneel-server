class Order():
    """blueprint for all order objects"""
    def __init__(self, id, timestamp, metal_id, size_id, style_id):
        self.id = id
        self.timestamp = timestamp
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id

        