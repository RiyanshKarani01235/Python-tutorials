
import numpy
import locate_file
import setup
import sys
import ctypes
import copy

working_directory = locate_file.locate_file()

_image_processing_ = ctypes.cdll.LoadLibrary(setup.shared_object_library_name)

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

class just_pass_() : 
    def from_param(self,param) : 
        return param

just_pass = just_pass_()

_image_processing_.convolution.argtypes = [two_d_array_,two_d_array_,\
two_d_array_,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int]
_image_processing_.convolution.restype = ctypes.c_void_p

def convolution(image,kernel,flag=True) :

    image_height = len(image)
    image_width = len(image[0])
    kernel_normalizer = kernel[0]
    kernel = kernel[1] 

    return_c_array = numpy.ctypeslib.as_array(((ctypes.c_int*image_width)*image_height)())

    '''
    ADD BORDER TO IMAGE
    '''
    image_c_array = numpy.ascontiguousarray(image,dtype=numpy.int32)
    kernel_c_array = numpy.ascontiguousarray(kernel,dtype=numpy.int32)
    _image_processing_.convolution(image_c_array,return_c_array,kernel_c_array,\
        len(image[0]),len(image),len(kernel),kernel_normalizer)

    #remove border from the image
    image_c_array =[element[:-len(kernel)+1] for element in image_c_array]\
    [:-len(kernel)+1]
    if flag : 
        return numpy.ascontiguousarray(return_c_array,dtype=numpy.uint8)
    else :
        return numpy.ascontiguousarray(return_c_array,dtype=numpy.int32)
