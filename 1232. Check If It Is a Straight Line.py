class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True  # If there are 0 or 1 points, they always form a straight line.

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]

            # Check if the points are collinear by comparing slopes.
            if (y2 - y1) * (xi - x1) != (yi - y1) * (x2 - x1):
                return False  # If the slopes are not equal, points are not collinear.

        return True  # All points are collinear.