class Order():
    """blueprint for all order objects"""
    def __init__(self, id, time_stamp, metal_id, size_id, style_id):
        self.id = id
        self.time_stamp = time_stamp
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.metal = None
        self.size = None
        self.style = None

        