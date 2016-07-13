
import math
import operator
from .axis import Axis

class Vector(object):
    """TODO
    """

    DIMENSIONS = 3
    AXIS_X = 'x'
    AXIS_Y = 'y'
    AXIS_Z = 'z'

    @staticmethod
    def fromarray(array):
        """TODO:
        Init vector from array"""
        return Vector(*array)

    @staticmethod
    def identity(self):
        """"""
        return Vector(0, 0, 0)

    def __init__(self, x, y, z):
        self.__vec = [x, y, z]

    def __add__(self, other):
        """TODO:
        Add matrix
        """

        # Add vector
        if isinstance(self, self.__class__):
            return [operator.add(a, b) for a, b in zip(self, other)]

        # Add collection
        pass

        # Add number
        pass

    def __sub__(self, other):
        """TODO:
        Sub matrix
        """

        # Add vector
        if isinstance(self, self.__class__):
            return [operator.sub(a, b) for a, b in zip(self, other)]

        # Add collection
        pass

        # Add number
        pass

    def __div__(self, other):
        """TODO:
        Divide by:
            matrix
            scalar
        """

        # Add vector
        if isinstance(self, self.__class__):
            return [operator.div(a, b) for a, b in zip(self, other)]

        # Add collection
        pass

        # Add number
        pass

    def __mul__(self, other):
        """TODO:
        Multiply by:
            matrix
            scalar
        """

        if isinstance(self, self.__class__):
            return [operator.mul(a, b) for a, b in zip(self, other)]

        # Add collection
        pass

        # Add number
        pass

    def __iter__(self):
        for value in self.__vec:
            yield value

    def __getitem__(self, index):
        self.getindex(index)

    def __setitem__(self, index, value):
        self.setindex(index, value)

    def __delitem__(self, index):
        self.setindex(index, 0)

    def __repr__(self):
        return "<{0} {1}".format(self.__class__.__name__, self.__vec)

    def getaxis(self, axis):
        """"""
        return self[(
            self.AXIS_X, self.AXIS_Y, self.AXIS_Z).index(axis)]

    def magnitude(self):
        """"""
        return math.sqrt(sum(map(lambda n: n**2, self.__vec)))

    def average(self):
        """TODO:
        Average of vector
        """
        return sum(self.__vec) / Vector.DIMENSIONS

    def setindex(self, index, value):
        """"""
        self.__vec[index] = value

    def getorder(self):
        """TODO: Implement ordering
        """
        return "xyz"

    def getindex(self, index):
        """"""
        return self.__vec[index]

    def normalize(self):
        """"""
        magnitude = self.magnitude()
        return Vector.fromarray([axis / magnitude for axis in self])

    x = property(
        fget=lambda self: self.getindex(0),
        fset=lambda self, value: self.setindex(0, value),
        fdel=lambda self, value: self.setindex(0, 0)
    )
    y = property(
        fget=lambda self: self.getindex(1),
        fset=lambda self, value: self.setindex(1, value),
        fdel=lambda self, value: self.setindex(1, 0)
    )
    z = property(
        fget=lambda self: self.getindex(2),
        fset=lambda self, value: self.setindex(2, value),
        fdel=lambda self, value: self.setindex(2, 0)
    )