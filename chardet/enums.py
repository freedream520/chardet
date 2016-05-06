"""
All of the Enums that are used throughout the chardet package.

:author: Dan Blanchard (dan.blanchard@gmail.com)
"""


class InputState(object):
    """
    This enum represents the different states a universal detector can be in.
    """
    pure_ascii = 0
    esc_ascii = 1
    high_byte = 2


class LanguageFilter(object):
    """
    This enum represents the different language filters we can apply to a
    ``UniversalDetector``.
    """
    chinese_simplified = 0x01
    chinese_traditional = 0x02
    japanese = 0x04
    korean = 0x08
    non_cjk = 0x10
    all = 0x1F
    chinese = chinese_simplified | chinese_traditional
    cjk = chinese | japanese | korean


class ProbingState(object):
    """
    This enum represents the different states a prober can be in.
    """
    detecting = 0
    found_it = 1
    not_me = 2


class MachineState(object):
    """
    This enum represents the different states a state machine can be in.
    """
    start = 0
    error = 1
    its_me = 2


class SequenceLikelihood(object):
    """
    This enum represents the likelihood of a character following the previous one.
    """
    negative = 0
    unlikely = 1
    likely = 2
    positive = 3

    @classmethod
    def get_num_categories(cls):
        """:returns: The number of likelihood categories in the enum."""
        return 4