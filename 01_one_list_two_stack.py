'''
用一个数组实现一个高性能的双头栈，支持从左侧、右侧的push和pop操作（l_pop/l_push/r_pop/r_push）
'''

# 自定义异常
class StackError(Exception):
    pass

class List_Stack:
    def __init__(self):
        self.list1 = [1,3,5]

    # 查看数组是否为空
    def is_empty(self):
        if len(self.list1) == 0:
            return 1
        else:
            return 0

    # 数组反转
    def list_reverse(self):
        return self.list1.reverse()

    # 右侧入栈
    def right_push(self,val):
        self.list1.append(val)

    # 右侧出栈
    def right_pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        self.list1.pop()

    # 查看右侧栈顶元素
    def right_top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self.list1[-1]

    # 左侧入栈
    def left_push(self, val):
        self.list_reverse()
        self.list1.append(val)
        self.list_reverse()

    # 左侧出栈
    def left_pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        self.list_reverse()
        self.list1.pop()
        self.list_reverse()

    # 查看左侧栈顶元素
    def left_top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self.list1[0]


if __name__ == '__main__':
    # 右侧测试
    # ls = List_Stack()
    # print(ls.right_pop())
    # print(ls.right_pop())
    # ls.right_push(7)
    # print(ls.right_top())
    # print(ls.list1)

    # 左侧测试
    ls = List_Stack()
    ls.left_push(10)
    ls.left_pop()
    print(ls.list1)
    ls.left_pop()
    print(ls.left_top())
    print(ls.list1)
