class BaseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ShowNotFound(BaseError):
    pass


class IDNotFound(BaseError):
    pass


class ScheduleNotFound(BaseError):
    pass


class EpisodeNotFound(BaseError):
    pass


class NoEpisodesForAirdate(BaseError):
    pass


class CastNotFound(BaseError):
    pass


class ShowIndexError(BaseError):
    pass


class PersonNotFound(BaseError):
    pass


class CreditsNotFound(BaseError):
    pass


class AKASNotFound(BaseError):
    pass


class GeneralError(BaseError):
    pass


class MissingParameters(BaseError):
    pass

