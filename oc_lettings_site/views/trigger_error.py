"""
function to test sentry
"""


def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)
