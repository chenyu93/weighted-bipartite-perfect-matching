cimport cython
import numpy as np
cimport numpy as np

from libcpp.vector cimport vector

cdef extern from "hungarian.h":
    ctypedef struct WeightedBipartiteEdge:
        int left
        int right
        int cost

    const vector[int] hungarianMinimumWeightPerfectMatching(int n, const vector[WeightedBipartiteEdge] allEdges)


def c_match(int n):
    return hungarianMinimumWeightPerfectMatching(n, [])
