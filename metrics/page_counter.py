from prometheus_client import Counter

page_counter = Counter('custom_page_counter', 'number of times page is hit')


def increment_page_counter():
    page_counter.inc()


def get_current_page_counter_value():
    return page_counter._value.get()
