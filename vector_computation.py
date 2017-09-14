# -*- coding: UTF-8 -*-
import vector

# 计算两个向量的和
v = vector.Vector([8.218,-9.341])
w = vector.Vector([-1.129,2.111])
print (v.plus(w))

# 计算两个向量的差
v = vector.Vector([7.119,8.215])
w = vector.Vector([-8.223,0.878])
print (v.minus(w))

# 计算向量的标量乘法
v = vector.Vector([1.671,-1.012,-0.318])
c = 7.41
print (v.times_scalar(c))


# 计算向量大小
v = vector.Vector([-0.221,7.437])
print(v.magnitude())

v = vector.Vector([8.813,-1.331,-6.247])
print(v.magnitude())

# 向量标准化
v = vector.Vector([5.581,-2.136])
print(v.normalized())

v = vector.Vector([1.996,3.108,-4.554])
print(v.normalized())

# 计算向量内积
v = vector.Vector([7.887,4.138])
w = vector.Vector([-8.802,6.776])
print(v.dot(w))

# 计算向量夹角
v = vector.Vector([3.183,-7.627])
w = vector.Vector([-2.668,5.319])
print(v.angle_with(w))


# 判断两个向量是平行还是正交
v = vector.Vector([-7.579,-7.88])
w = vector.Vector([22.737,23.64])
print(v.is_parallel_to(w))
print(v.is_orthogonal_to(w))


v = vector.Vector([-2.029,9.97,4.172])
w = vector.Vector([-9.231,-6.639,-7.245])
print(v.is_parallel_to(w))
print(v.is_orthogonal_to(w))


v = vector.Vector([-2.328,-7.284,-1.214])
w = vector.Vector([-1.821,1.072,-2.94])
print(v.is_parallel_to(w))
print(v.is_orthogonal_to(w))


v = vector.Vector([2.118,4.827])
w = vector.Vector([0,0])
print(v.is_parallel_to(w))
print(v.is_orthogonal_to(w))


# 计算一个向量在另一个向量上的投影
v = vector.Vector([3.039,1.879])
w = vector.Vector([0.825,2.036])
print (v.component_parallel_to(w))

# 计算给定向量的情况下，与基向量的正交向量
v = vector.Vector([-9.88,-3.264,-8.159])
w = vector.Vector([-2.155,-9.353,-9.473])
print(v.component_orthogonal_to(w))

# 计算给定向量的情况下，与基向量的正交向量，以及在基向量上的投影
v = vector.Vector([3.009,-6.172,3.692,-2.51])
w = vector.Vector([6.404,-9.144,2.759,8.718])
vpar = v.component_parallel_to(w)
vort = v.component_orthogonal_to(w)
print(vpar)
print(vort)


# 计算两个向量的向量积
v = vector.Vector([8.462,7.893,-8.187])
w = vector.Vector([6.984,-5.975,4.778])
print(v.cross(w))

# 计算两个向量形成的平行四边形的面积
v = vector.Vector([-8.984,-9.838,5.031])
w = vector.Vector([-4.268,-1.861,-8.866])
print(v.area_of_parallelogram_with(w))

# 计算两个向量形成的三角形的面积
v = vector.Vector([1.5,9.547,3.691])
w = vector.Vector([-6.007,0.124,5.772])
print(v.area_of_triangle_with(w))


