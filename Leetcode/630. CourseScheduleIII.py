# The iteration over the sorted courses remains the same. 
# Whenver the current course (i.e. time + duration_i ≤ endday_i), it is added to the queue and 
# the value of the current time is updated to time + duration_i

# If the current course can't be taken directly, as in the previous appraoches, 
# we need to find a course whose duration duration_j ​is maximum from amongst the courses taken till now. 
# Now, since we are maintaing a Max-Heap, queue, we can obtain this duration directly from this queue. 
# If the duration duration_j > duration_i, we can replace the j_th course with the current one.

# Thus, we remove the duration_j from the queue and add the current course's duration duration_i to the queue
# We also need to make proper adjustments to the time to account for this replacement done.

# At the end, the number of elements in the queue represent the number of courses that have been taken till now.

import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        print(courses)
        time = 0
        heap = []
        for duration, last_day in courses:
            time += duration
            heapq.heappush(heap, -duration)
            print(heap)
            if time > last_day:
                time += heapq.heappop(heap)
        return len(heap)