#include<stdio.h>

void convolution(int *image,int *kernel,int image_width, int image_height, int kernel_size, int kernel_normalizer) {
    
    int image_starting_x = 0;
    int image_starting_y = 0;
    int image_ending_x = image_width - kernel_size + 1;
    int image_ending_y = image_height - kernel_size + 1;
    
    int i,j,u,v,sum;
    j=0;
    
    for(i=image_starting_y;i<image_height;i++) {
        for(j=image_starting_x;j<image_width;j++) {
            
            //current left top corner pixel is i,j
            sum = 0;
            for(u=0;u<kernel_size;u++) {
                for(v=0;v<kernel_size;v++) {
                    sum += (*(image + image_width*(i+u) + j+v))*(*(kernel + u*kernel_size + v));
                }
            }
            *(image + (image_width*i) + j) = sum/kernel_normalizer;
            
            
        }
    }
}