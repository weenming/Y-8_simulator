class Error(Exception):
    pass


class AddressError(Error):
    pass


class Halt(Error):
    pass


class InstructionError(Error):
    pass
