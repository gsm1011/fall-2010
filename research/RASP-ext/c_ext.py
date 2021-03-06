# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_c_ext', [dirname(__file__)])
        except ImportError:
            import _c_ext
            return _c_ext
        if fp is not None:
            try:
                _mod = imp.load_module('_c_ext', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _c_ext = swig_import_helper()
    del swig_import_helper
else:
    import _c_ext
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class floatArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, floatArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, floatArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _c_ext.new_floatArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _c_ext.delete_floatArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _c_ext.floatArray___getitem__(self, *args)
    def __setitem__(self, *args): return _c_ext.floatArray___setitem__(self, *args)
    def cast(self): return _c_ext.floatArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _c_ext.floatArray_frompointer
    if _newclass:frompointer = staticmethod(_c_ext.floatArray_frompointer)
floatArray_swigregister = _c_ext.floatArray_swigregister
floatArray_swigregister(floatArray)

def floatArray_frompointer(*args):
  return _c_ext.floatArray_frompointer(*args)
floatArray_frompointer = _c_ext.floatArray_frompointer


def validate0(*args):
  return _c_ext.validate0(*args)
validate0 = _c_ext.validate0

def validate(*args):
  return _c_ext.validate(*args)
validate = _c_ext.validate


