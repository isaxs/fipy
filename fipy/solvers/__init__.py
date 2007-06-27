import sys
from solver import SolverConvergenceWarning, \
     PreconditionerWarning, \
     ScalarQuantityOutOfRangeWarning, \
     StagnatedSolverWarning, \
     MatrixIllConditionedWarning, \
     PreconditionerNotPositiveDefiniteWarning, \
     IllConditionedPreconditionerWarning, \
     MaximumIterationWarning

if '--trilinos' in sys.argv[1:]:
    from fipy.solvers.trilinos import *
elif '--pysparse' in sys.argv[1:]:
    from fipy.solvers.pysparse import *
elif '--scipy' in sys.argv[1:]:
    from fipy.solvers.scipy import *
else:
    foundSolvers  = False
    if not foundSolvers:
        try: 
            from fipy.solvers.trilinos import *
            foundSolvers = True
        except:
            pass

    if not foundSolvers:
        try:
            from fipy.solvers.pysparse import *
            foundSolvers = True
        except:
            pass
    
    
    if not foundSolvers:
        try: 
            from fipy.solvers.scipy import *
            foundSolvers = True
        except:
            pass

    #if not foundSolvers:
        #raise ImportError, "Could not import any solver package." 
    
from fipy.solvers.pysparse import *
