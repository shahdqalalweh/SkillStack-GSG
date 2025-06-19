class ItemNotAvailableError(Exception):
    def __init__(self):
        super().__init__('Item is not available.')