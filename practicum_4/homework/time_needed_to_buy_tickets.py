from typing import Any

import yaml
import numpy as np

from queue import Queue


def time_taken(tickets: list[int], k: int) -> int:
    # ~ O(MN): n: persons count, m: max tickets per person
 
    seconds_elapsed = 0
    
    queue = Queue()
    for index, value in enumerate(tickets):
    	queue.put((index,value))
    
    while queue:
    	idx, val = queue.get()
    	val -= 1
    	seconds_elapsed += 1
    	if (val != 0):
    		queue.put((idx, val))
    	elif (idx == k):
    		return seconds_elapsed


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    with open("practicum_4/time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")
