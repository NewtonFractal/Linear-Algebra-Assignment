import numpy
import matplotlib.pyplot as plt
norm_list_y = []
norm_list_x = []
A = numpy.array([[1,1,2],
                 [1,2,1],
                 [2,1,1],
                 [2,2,1]])

A_Transpose = numpy.array([[1,1,2,2],
                           [1,2,1,2],
                           [2,1,1,1]])

for a in range(-2001,2001,20):
    a = a/100
    norm_list_x.append(a)
    y = numpy.array([1, a, 1, a])
    numpy.matmul(A_Transpose, y)
    inverse_matrix = numpy.linalg.inv(numpy.matmul(A_Transpose, A))
    norm_list_y.append(numpy.linalg.norm(numpy.matmul(inverse_matrix, numpy.matmul(A_Transpose, y))))

plt.plot(norm_list_x,norm_list_y)
plt.ylabel('norm')
plt.xlabel('parameter value')
plt.show()
