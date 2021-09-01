from prometheus_client import Counter

click_counter = Counter('custom_click_counter', 'number of button clicks')


def increment_click_counter():
    click_counter.inc()


def get_current_click_counter_value():
    return click_counter._value.get()
