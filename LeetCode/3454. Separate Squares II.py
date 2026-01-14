# https://leetcode.com/problems/separate-squares-ii/description/?envType=daily-question&envId=2026-01-14
# Editorial ...

from typing import List
import bisect


class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def update(self, qleft, qright, qval, left, right, pos):
        if self.xs[right + 1] <= qleft or self.xs[left] >= qright:
            return
        if qleft <= self.xs[left] and self.xs[right + 1] <= qright:
            self.count[pos] += qval
        else:
            mid = (left + right) // 2
            self.update(qleft, qright, qval, left, mid, pos * 2 + 1)
            self.update(qleft, qright, qval, mid + 1, right, pos * 2 + 2)

        if self.count[pos] > 0:
            self.covered[pos] = self.xs[right + 1] - self.xs[left]
        else:
            if left == right:
                self.covered[pos] = 0
            else:
                self.covered[pos] = (
                    self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]
                )

    def query(self):
        return self.covered[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs_set = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs_set.update([x, x + l])
        xs = sorted(xs_set)

        seg_tree = SegmentTree(xs)
        events.sort()

        psum = []
        widths = []
        total_area = 0.0
        prev_y = events[0][0]

        # scan: calculate total area and record intermediate states
        for y, delta, xl, xr in events:
            length = seg_tree.query()
            total_area += length * (y - prev_y)
            seg_tree.update(xl, xr, delta, 0, seg_tree.n - 1, 0)
            # record prefix sums and widths
            psum.append(total_area)
            widths.append(seg_tree.query())
            prev_y = y

        # calculate the target area (half rounded up)
        target = (total_area + 1) // 2
        # find the first position greater than or equal to target using binary search
        i = bisect.bisect_left(psum, target) - 1
        # get the corresponding area, width, and height
        area = psum[i]
        width = widths[i]
        height = events[i][0]

        return height + (total_area - area * 2) / (width * 2.0)

'''
TLE . .. . . . .. . 

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        n = len(squares)
        min_y, max_y = 10**9 + 1, -1

        for i in range(n):
            x, y, l = squares[i][0], squares[i][1], squares[i][2]

            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        x_coordinates = sorted(list(set(x for x, _, _ in squares) | set(x+l for x, _, l in squares)))
        
        def get_area(line):
            area = 0
            for i in range(len(x_coordinates) - 1):
                x1, x2 = x_coordinates[i], x_coordinates[i+1]
                width = x2 - x1

                y_intervals = []
                for (sx, sy, sl) in squares:
                    if not (sx <= x1 and x2 <= sx + sl):
                        continue
                    y_start = sy
                    y_end = min(sy + sl, line)
                    if y_start < y_end:
                        y_intervals.append((y_start, y_end))

                if not y_intervals:
                    continue

                y_intervals.sort()

                union_height = 0
                curr_start, curr_end = y_intervals[0]

                for next_start, next_end in y_intervals[1:]:
                    if next_start < curr_end:
                        curr_end = max(curr_end, next_end)
                    else:
                        union_height += (curr_end - curr_start)
                        curr_start, curr_end = next_start, next_end
                union_height += (curr_end - curr_start)
                area += width * union_height

            return area
        
        total += get_area(max_y)

        while abs(min_y - max_y) > 1e-5:
            mid = (min_y + max_y) / 2
            if get_area(mid) >= total / 2:
                max_y = mid
            else:
                min_y = mid
        
        return max_y
'''
