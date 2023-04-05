from typing import Any

import numpy as np
from numpy.typing import NDArray
import yaml

class StackUnderflowException(BaseException):
	pass
class StackOverflowException(BaseException):
	pass

class LIFOStack:
	# Initialisation
	def __init__(self, max_n: int, dtype: Any, top_index: int=-1) -> None:
		self._array: NDArray = np.zeros((max_n), dtype=dtype)
		self.top_index: int = -1
	
	@classmethod
	def stack_from_list(cls, array: list[Any]):
		pass
	
	@classmethod
	def stack_from_array(cls, array: NDArray[Any]):
		pass	
	
	@classmethod
	def stack_from_str(cls, s: str):
		pass
	
	# Push an element into stack
	def push(self, x: Any) -> None:
		""" Complexity: O(1) """
		
		self.top_index += 1
		
		if (self.top_index == len(self._array)):
			raise StackOverflowException("Stack is already full")
		
		self._array[self.top_index] = x
	
	def pop(self) -> None:
		""" Complexity: O(1) """
		
		if (self.top_index == -1):
			raise StackUnderflowException("Stack is already empty")
		
		self.top_index -= 1
		return self._array[self.top_index + 1]
	
	def is_empty(self) -> bool:
		return self.top_index == -1

def get_opposite_symbol(s: str) -> str:
	if s == "}": return '{'

	if s == ")": return '('
	
	if s == "]": return '['
	

def are_parentheses_valid(s: str) -> bool:
	stack = LIFOStack(max_n=100, dtype=str)
	stack.push(s[0])
	
	open_symbols = ["(", "[", "{"]
	end_symbols = [")", "]", "}"]
	
	for x in s[1:]:
		if x in open_symbols:
			stack.push(x)
		else:
			try:
				tmp = stack.pop()
			except StackUnderflowException:
				continue
				
			if get_opposite_symbol(x) != tmp:
				return False
			
	return stack.is_empty()
				
			
	

if __name__ == "__main__":
    # Let's solve Valid Parentheses problem from leetcode.com:
    # https://leetcode.com/problems/valid-parentheses/
    cases = []
    with open("practicum_4/valid_parentheses_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = are_parentheses_valid(c["input"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")
