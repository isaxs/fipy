#!/usr/bin/env python

## 
 # -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "solver.py"
 #                                    created: 11/14/03 {3:47:20 PM} 
 #                                last update: 7/6/05 {3:56:55 PM} 
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-14 JEG 1.0 original
 # ###################################################################
 ##

__docformat__ = 'restructuredtext'

class Solver:
    """
    The base `LinearXSolver` class.
    
    .. attention:: This class is abstract. Always create one of its subclasses.
    """

    def __init__(self, tolerance = 1e-10, steps = 1000):
        """
        Create a `Solver` object.

        :Parameters:
          - `tolerance`: The required error tolerance.
          - `steps`: The maximum number of iterative steps to perform.

        """
	self.tolerance = tolerance
	self.steps = steps
	
    def _solve(self, L, x, b):
	pass
        
    def __repr__(self):
        return '%s(tolerance = %g, steps = %g)' \
            % (self.__class__.__name__, self.tolerance, self.steps)

