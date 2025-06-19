class ItemNotFoundError(Exception):
    def __init__(self):
        super().__init__('Item not found.')