from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def convex_bucket(points: NDArray) -> NDArray:
	# sort the points by x-coords
	sorted_points = sorted(points, key=lambda x: (x[0]))
	# list to store the lower part
	lowers = []
	
	for point in sorted_points:
		while len(lowers) >= 2 and (np.cross(lowers[-1] - lowers[-2], point - lowers[-2]) <= 0):
			lowers.pop()
		
		lowers.append(point)
	
	print(sorted_points)
	#print(lowers)
	return np.array(lowers + lowers[-2::-1])


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"../points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
