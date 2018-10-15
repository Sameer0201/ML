from numpy import *
from util import *
import util

def pca(X, K):
    '''
    X is an N*D matrix of data (N points in D dimensions)
    K is the desired maximum target dimensionality (K <= min{N,D})

    should return a tuple (P, Z, evals)
    
    where P is the projected data (N*K) where
    the first dimension is the higest variance,
    the second dimension is the second higest variance, etc.

    Z is the projection matrix (D*K) that projects the data into
    the low dimensional space (i.e., P = X * Z).

    and evals, a K dimensional array of eigenvalues (sorted)
    '''
    
    N,D = X.shape
    P, Z, evals = None, None, None ### TODO: delete this line after implementation

    # make sure we don't look for too many eigs!
    if K > N:
        K = N
    if K > D:
        K = D

    # first, we need to center the data
    ### TODO: YOUR CODE HERE
    M = mean(X.T, axis=1)
    
    centered = X - M
    #util.raiseNotDefined()

    # next, compute eigenvalues of the data variance
    #    hint 1: look at 'help(np.linalg.eig)'
    #    hint 2: you'll want to get rid of the imaginary portion of the eigenvalues; use: real(evals), real(evecs)
    #    hint 3: be sure to sort the eigen(vectors,values) by the eigenvalues: see 'argsort', and be sure to sort in the right direction!
    #             
    ### TODO: YOUR CODE HERE
    #util.raiseNotDefined()
    
    print(1)
    print(X)
    
    covarMatrix = cov(centered.T)
    
    evals, evecs = linalg.eig(covarMatrix)
    
    evals = real(evals)
    evecs = real(evecs)
    
    print(1)
    print(evals)
    print(evecs)
    
    sortedList = evals.argsort()[::-1]
    evals = evals[sortedList]
    evecs = evecs[:,sortedList]
    
    print(2)
    print(evals)
    print(evecs)
    
    P = evecs.T.dot(centered.T).T
    print(3)
    print(P)
    print(len(P))
    
    U = evecs.T[::-1]
    P = centered.dot(U[:2].T)
    print(D)
    print(N)
    Z = U
    
    return (P, Z, evals)


