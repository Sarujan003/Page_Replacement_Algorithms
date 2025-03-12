def fifo_page_replacement(pages, frames):
    memory = []
    page_faults = 0
    steps = []  # Stores memory states at each step
    index = 0   # Pointer to track the next frame to replace

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[index] = page
                index = (index + 1) % frames
            page_faults += 1
        
        steps.append(memory.copy())  # Store current frame state

    return page_faults, steps


def lru_page_replacement(pages, frames):
    memory = []
    page_faults = 0
    steps = []
    recently_used = []

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                least_recently_used = recently_used.pop(0)  # Remove the LRU page from the list
                index_of_lru_frame = memory.index(least_recently_used)
                memory[index_of_lru_frame] = page  # Replace the LRU page with the new page
            page_faults += 1
        else:
            # Update the recently_used list by removing and appending the page.
            recently_used.remove(page)

        # Add the current page to the recently_used list.
        recently_used.append(page)

        steps.append(memory.copy())  # Record the memory state after each step

    return page_faults, steps

def lfu_page_replacement(pages, frames):
    memory = []
    page_faults = 0
    steps = []  # To store memory states at each step
    page_frequency = {}  # frequency tracking
    page_hist = []  # Maintains order of page arrivals

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
                page_hist.append(page)
            else:
                # Find the page with the least frequency
                minimum_freq = min(page_frequency[x] for x in memory)
                min_freq_pages = [x for x in memory if page_frequency[x] == minimum_freq]

                if len(min_freq_pages) == 1:
                    page_to_replace = min_freq_pages[0]
                else:
                    # Find the first in page
                    indexes = []
                    for i in min_freq_pages:
                        index = page_hist.index(i)
                        indexes.append(index)
                    page_to_replace = page_hist[min(indexes)]

                # Replace the page
                memory[memory.index(page_to_replace)] = page
                page_hist.remove(page_to_replace)
                page_hist.append(page)
                page_frequency[page_to_replace] = 0  # Reset frequency for removed page

            page_faults += 1

        page_frequency[page] = page_frequency.get(page, 0) + 1

        # Store the current memory state after each step
        steps.append(memory.copy())

    return page_faults, steps



def mfu_page_replacement(pages, frames):
    memory = []
    page_faults = 0
    steps = []  # To store memory states at each step
    page_frequency = {}  # for frequency tracking
    page_hist = []  # Maintains order of page arrivals

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
                page_hist.append(page)
            else:
                maximum_freq = max(page_frequency[x] for x in memory)
                max_freq_page = [x for x in memory if page_frequency[x] == maximum_freq]

                if len(max_freq_page) == 1:
                    page_to_replace = max_freq_page[0]
                else:
                    # Find the first in page
                    indexes = []
                    for i in max_freq_page:
                        index = page_hist.index(i)
                        indexes.append(index)
                    page_to_replace = page_hist[min(indexes)]

                # Replace the page
                memory[memory.index(page_to_replace)] = page
                page_hist.remove(page_to_replace)
                page_hist.append(page)
                page_frequency[page_to_replace] = 0    # Reset frequency for removed page

            page_faults += 1

        page_frequency[page] = page_frequency.get(page, 0) + 1

        # Store the current memory state after each page is processed
        steps.append(memory.copy())

    return page_faults, steps


