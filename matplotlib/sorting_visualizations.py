import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_sort(arr, frames, title="Sorting Animation"):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color="skyblue")
    ax.set_title(title)
    ax.set_ylim(0, max(arr) * 1.2)

    def update(frame):
        snap, hl, event = frame
        for i, b in enumerate(bars):
            b.set_height(snap[i])
            b.set_color("skyblue")  # reset to default color

        if hl:
            # hl can be tuple of (list_of_indices, color_name)
            if isinstance(hl, tuple) and len(hl) == 2 and isinstance(hl[0], (list, tuple)):
                indices, color = hl
                for idx in indices:
                    bars[idx].set_color(color)
            # hl can be list of indices (defaults to orange)
            elif isinstance(hl, (list, tuple)):
                for idx in hl:
                    bars[idx].set_color("orange")
            # hl can be single int index
            elif isinstance(hl, int):
                bars[hl].set_color("orange")

        ax.set_title(f"{title} — {event}")
        return bars

    return FuncAnimation(fig, update, frames=frames, interval=400, blit=False)

# ---- Merge Sort Steps ----
def merge_sort_steps(arr):
    a = arr[:]
    def merge_sort(start, end):
        if end - start > 1:
            mid = (start + end) // 2
            yield from merge_sort(start, mid)
            yield from merge_sort(mid, end)
            left = a[start:mid]
            right = a[mid:end]
            i = j = 0
            for k in range(start, end):
                # Purple for merge area
                yield (a[:], ([x for x in range(start, end)], "purple"), "merging")
                if j >= len(right) or (i < len(left) and left[i] <= right[j]):
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                # Highlight just-updated index in green
                yield (a[:], (k,), "merge step")
    yield from merge_sort(0, len(a))
    # Mark all as sorted (green)
    yield (a[:], ([x for x in range(len(a))], "green"), "done")

# ---- Quick Sort Steps ----
def quick_sort_steps(arr):
    a = arr[:]
    def quick_sort(low, high):
        if low < high:
            pivot_index = yield from partition(low, high)
            yield from quick_sort(low, pivot_index - 1)
            yield from quick_sort(pivot_index + 1, high)

    def partition(low, high):
        pivot = a[high]
        # Red for pivot
        yield (a[:], (high, "red"), f"pivot={pivot}")
        i = low
        for j in range(low, high):
            yield (a[:], ([j, high], "orange"), "compare with pivot")
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                yield (a[:], ([i, j], "yellow"), "swap")
                i += 1
        a[i], a[high] = a[high], a[i]
        yield (a[:], ([i, high], "yellow"), "swap pivot")
        return i

    yield from quick_sort(0, len(a) - 1)
    yield (a[:], ([x for x in range(len(a))], "green"), "done")

# ---- Example Usage ----
data = [5, 1, 4, 2, 8, 3]
ani = animate_sort(data, merge_sort_steps(data), title="Merge Sort")
plt.show()

# ani = animate_sort([5, 1, 4, 2, 8, 3], quick_sort_steps([5, 1, 4, 2, 8, 3]), title="Quick Sort")
# plt.show()
