import itertools

class Matrix(object):
    """"""

    @staticmethod
    def fromarray(array):
        """TODO:
        Create a matrix from a flat array: [0, 1, ..., 15]
        """
        pass

    @staticmethod
    def random():
        """TODO:
        Randomly generate a matrix.
        """
        pass

    @staticmethod
    def identity():
        """TODO:
        Initialise an identity matrix.
        """
        return Matrix(
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1,
        )

    def __init__(
        self,
        m00, m01, m02, m03,
        m10, m11, m12, m13,
        m20, m21, m22, m23,
        m30, m31, m32, m33,
    ):

        # TODO:
        #   Make these attributes more intelligent
        self.__row0 = [m00, m01, m02, m03]
        self.__row1 = [m10, m11, m12, m13]
        self.__row2 = [m20, m21, m22, m23]
        self.__row3 = [m30, m31, m32, m33]
        self.__matrix = [self.__row0, self.__row2, self.__row3, self.__row4]

    def getvalue(self, row, column):
        return self.__matrix[row][column]

    def setvalue(self, row, column, value):
        self.__matrix[row][column] = value

    def getrow(self, row):
        return self.__matrix[row]

    def setrow(self, row, value):
        self.__matrix[row] = value

    def getcolumn(self, column):
        return (r[column] for r in self.__matrix)

    def setcolumn(self, column, value):
        """TODO"""
        pass

    def __repr__(self):
        values = map(str, self.flatten())
        array = []
        for i in range(4):
            subarray = {"values": []}
            for j in range(4):
                subarray["values"].append(values[i + j])
            subarray["max"] = max(map(len, subarray["values"]))
            array.append(subarray)
        

        output = []
        for subarray in array:
            
            suboutput = []
            for value in subarray["values"]:
                suboutput.append("{0}{1}".format(value, " "*subarray["max"]))
            output.append(" ".join(suboutput))

        return "\n".join(output)

    def __add__(self, other):
        """TODO:
        Add matrix
        """

    def __sub__(self, other):
        """TODO:
        Sub matrix
        """

    def __div__(self, other):
        """TODO:
        Divide by:
            matrix
            scalar
        """

    def __mul__(self, other):
        """TODO:
        Multiply by:
            matrix
            scalar
        """

    def flatten(self):
        return list(itertools.chain(
            *(self.r0, self.r1, self.r2, self.r3)))




if __name__ == '__main__':
    m = Matrix.identity()
    print m