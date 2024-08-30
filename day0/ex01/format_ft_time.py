import time


def format_ft_time():
    timestamp = time.time()
    formatted_time = time.strftime(
        f"Seconds since January 1, 1970: {timestamp:,.2f}"
        f" or {timestamp:.2e} in scientific notation\n"
        f"{time.strftime('%b %d %Y', time.gmtime(timestamp))}"
    )
    return formatted_time


print(format_ft_time())
