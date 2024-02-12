class A:
    def method_a(self):
        print('Method of Class A')
class B(A):
    def method_b(self):
        print('Method of Class B')

class C(B):
    # inherits from both Class A and B
    def method_c(self):
        print('Method of Class C')

c1 = C()
c1.method_a()
c1.method_b()
c1.method_c()