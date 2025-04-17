from tqdm import tqdm
import sys

def ft_tqdm(lst: range) -> None:
    """Custom implementation of a progress bar generator, similar to tqdm.

    This function wraps over a given iterable (typically a range object) and 
    yields its items one by one while displaying a dynamic progress bar in the terminal.

    Parameters:
    -----------
    lst : range
        A range object representing the iterable to be processed.

    Yields:
    -------
    item : int
        Each item from the input iterable, one at a time.

    Example:
    --------
    >>> for i in ft_tqdm(range(100)):
    ...     time.sleep(0.01)
    """
    def progression_bar(iteration) -> int:
        total_items = len(lst)
        progression = iteration / total_items
        percentage = f"{progression * 100:3.0f}" + "%"

        bar_width = 100
        filled_space = int(bar_width * progression)
        empty_space = " " * (bar_width - filled_space)
        bar = "█" * filled_space + empty_space

        info = f"{iteration}/{total_items}"
        return f"\r{percentage}|{bar}|{info}"

    for i, item in enumerate(lst):
        yield sys.stdout.write(progression_bar(i + 1))
        sys.stdout.flush()