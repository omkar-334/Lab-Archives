import operator as op

class Evaluate:
	def __init__(self, size):
		self.top = -1
		self.capacity = size
		self.stack = []
		self.dict={'+' : op.add,'-' : op.sub,'*' : op.mul,'/' : op.truediv}

	def isEmpty(self):
		return True if self.top == -1 else False

	def peek(self):
		return self.stack[-1]

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.stack.pop()
		else:
			return "$"

	def push(self, op):
		self.top += 1
		self.stack.append(op)

	def evalpostfix(self, exp):
		for i in exp:
			if i.isdigit():
				self.push(i)
			else:
				val1 = int(self.pop())
				val2 = int(self.pop())
				self.push(self.dict[i](val1,val2))
		return int(self.pop())

if __name__ == '__main__':
	exp = "231*+9-"
	obj = Evaluate(len(exp))
	print(f"postfix evaluation: {obj.evalpostfix(exp)}")

