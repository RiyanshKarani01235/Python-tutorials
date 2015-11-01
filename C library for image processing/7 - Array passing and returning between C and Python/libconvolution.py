import ctypes
import numpy
import setup

_image_processing_ = ctypes.cdll.LoadLibrary(setup.shared_object_library_name)

#Python class for defining 2dimensional array type as required by Ctypes library
class two_d_array() : 
    
    def from_param(self,param) : 
        typename = type(param).__name__
        if hasattr(self,'from_'+typename) : 
            return getattr(self,'from_'+typename)(param)
        elif isinstance(param,ctypes.Array) : 
            
            return param
        else : 
            raise TypeError('type {0} not supported'.format(typename))
    
    def from_ndarray(self,param) : 
        c_array = numpy.ascontiguousarray(param,dtype=numpy.int32)
        pointer = c_array.ctypes
        return pointer
    
    def from_list(self,param) : 
        return self.from_ndarray(param)
    
    def from_tuple(self,param) : 
        return self.from_ndarray(param)
    
two_d_array_ = two_d_array()

#defining argtypes and restypes for _image_processing_.convolution function
_image_processing_.convolution.argtypes = [two_d_array_,two_d_array_,\
two_d_array_,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int]
_image_processing_.convolution.restype = ctypes.c_void_p

def convolution(image,kernel,convert_to_uint8=True) :

    image_height = len(image)
    image_width = len(image[0])
    kernel_normalizer = kernel[0]
    kernel = kernel[1] 
    
    #generate a new ctypes array and convert it into a numpy array
    return_c_array = numpy.ctypeslib.as_array(((ctypes.c_int*image_width)*image_height)())
    #generate a contiguous aray in memory for the image and the kernel
    image_c_array = numpy.ascontiguousarray(image,dtype=numpy.int32)
    kernel_c_array = numpy.ascontiguousarray(kernel,dtype=numpy.int32)
    
    #calling the _image_processing_.convolution function and passing appropriate parameters
    _image_processing_.convolution(image_c_array,return_c_array,kernel_c_array,\
        len(image[0]),len(image),len(kernel),kernel_normalizer)

    if convert_to_uint8 : 
        return numpy.ascontiguousarray(return_c_array,dtype=numpy.uint8)
    else :
        return numpy.ascontiguousarray(return_c_array,dtype=numpy.int32)