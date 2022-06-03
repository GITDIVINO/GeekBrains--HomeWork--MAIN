"""Here are all functions from Lesson 1"""


def make_better_view(duration):
    """The function takes value and returns date in format <d> days <h> hours <m> minutes <s> seconds """

    if duration <= 60:
        return f'{duration} sec(s)'

    elif 60 < duration <= 3600:
        min = duration // 60
        sec = duration - 60 * min
        return f'{min} min(s) {sec} sec(s)'

    elif 3600 < duration <= 86400:
        hour = duration // 3600
        min = (duration - 3600 * hour) // 60
        sec = duration - 3600 * hour - 60 * min
        return f'{hour} hour(s) {min} min(s) {sec} sec(s)'

    else:
        day = duration // 86400
        hour = (duration - 86400 * day) // 3600
        min = (duration - 86400 * day - 3600 * hour) // 60
        sec = duration - 86400 * day - 3600 * hour - 60 * min
        return f'{day} day(s) {hour} hour(s) {min} min(s) {sec} sec(s)'
