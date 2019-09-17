import numpy

A = numpy.array([[0,1],
                 [1,1],
                 [2,1],
                 [3,1]])

A_Transpose = numpy.array([[0,1,2,3],
                           [1,1,1,1]])

y = numpy.array([1.5,2.9,5.3,6.6])
numpy.matmul(A_Transpose, y)
inverse_matrix = numpy.linalg.inv(numpy.matmul(A_Transpose, A))

print(numpy.matmul(inverse_matrix,numpy.matmul(A_Transpose, y)))

