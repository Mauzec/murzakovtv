from typing import Any

import yaml
import numpy as np
from numpy.typing import NDArray

class StackUnderflowException(BaseException):
	pass
class StackOverflowException(BaseException):
	pass

class FIFOStack:
	def __init__(self, max_n: int, dtype: Any) -> None:
		self._array: NDArray = np.zeros((max_n), dtype=dtype)
		self.head_index = 0 # the oldest element
		self.next_index = 0  # the future element
	
	def _increment(self, index: int) -> int:
		return 0 if index == len(self._array) else index + 1
		
	def push(self, x: Any) -> None:
		self.next_index = self._increment(self.next_index)
		if self.next_index  == self.head_index:
			raise StackOverflowException("Stack is already full")
		
		self._array[self.next_index - 1] = x
		
	def pop(self) -> Any:
		if self.is_empty(): 
			raise StackUnderflowException("Stack is already empty")
		
		x = self._array[self.head_index]
		self.head_index = self._increment(self.head_index)
		
		return x
	
	def is_empty(self) -> bool:
		return self.next_index == self.head_index
		
		
		


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    # Here we show a toy solution which does not make use of k and simply returns
    # the number of seconds the whole queue spent to disappear.
    # It should be modified to solve the original problem (and it can be solved without a queue)
    #with open("practicum_4/time_needed_to_buy_tickets_cases.yaml", "r") as f:
    #    cases = yaml.safe_load(f)
    #for c in cases:
    #    res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
    #    print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")

	stack = FIFOStack(max_n=5, dtype=int)
	stack.push(5)
	stack.push(4)
	stack.push(3)
	stack.push(2)
	stack.push(1)
	print(stack.pop())