class ReservationError(Exception):
    def __init__(self, message='Reservation failed.'):
        super().__init__(message)