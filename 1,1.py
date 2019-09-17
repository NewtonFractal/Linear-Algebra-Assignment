import numpy

A = numpy.array([[1,1,2],
                 [1,2,1],
                 [2,1,1],
                 [2,2,1]])

A_Transpose = numpy.array([[1,1,2,2],
                           [1,2,1,2],
                           [2,1,1,1]])

y = numpy.array([1,-1,1,-1])
numpy.matmul(A_Transpose, y)
inverse_matrix = numpy.linalg.inv(numpy.matmul(A_Transpose, A))

print(numpy.matmul(inverse_matrix,numpy.matmul(A_Transpose, y)))

