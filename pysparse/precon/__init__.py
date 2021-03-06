"""
Preconditioners.
"""

__all__ = [s for s in dir() if not s.startswith('_')]

from pysparse.misc import Deprecated

@Deprecated('Use pysparse.precon.precon.ssor instead.')
def ssor(*args, **kwargs):
    import pysparse.precon.precon
    return  pysparse.precon.precon.ssor(*args, **kwargs)

@Deprecated('Use pysparse.precon.precon.jacobi instead.')
def jacobi(*args, **kwargs):
    import pysparse.precon.precon
    return  pysparse.precon.precon.jacobi(*args, **kwargs)


