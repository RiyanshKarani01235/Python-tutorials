#include<stdio.h>
#include<stdlib.h>

void convolution(int *image,int *kernel,int image_width, int image_height, int kernel_size, int kernel_normalizer) {
    
    int image_starting_x = 0;
    int image_starting_y = 0;
    int image_ending_x = image_width;
    int image_ending_y = image_height;
    
    int i,j,u,v;
    int sum;
    
    for(i=image_starting_y;i<image_height-kernel_size;i++) {
        for(j=image_starting_x;j<image_width-kernel_size;j++) {
            
            //current left top corner pixel is i,j
            sum = 0;
            for(u=0;u<kernel_size;u++) {
                for(v=0;v<kernel_size;v++) {
                    sum += (*(image + image_width*(i+u) + j+v))*(*(kernel + u*kernel_size + v));
                }
            }
            *(image + (image_width*i) + j) = (sum/kernel_normalizer);
            // return_image[i][j] = sum/kernel_normalizer;
        }
    }
}

void sobel_operator(int *image,int image_width,int image_height) {
    
    int kernel_x[3][3] = {{-1,0,1},{-2,0,2},{-1,0,1}};
    int kernel_y[3][3] = {{-1,-2,-1},{0,0,0},{-1,0,-1}};

    int x,y,u,v;

    int sobel_x[image_height][image_width];
    int sobel_y[image_height][image_width];

    convolution(image,&sobel_x[0][0],&kernel_x[0][0],image_width,image_height,3,1);
    convolution(image,&sobel_y[0][0],&kernel_x[0][0],image_width,image_height,3,1);
    image = &sobel_x[0][0];
    int *p = &sobel_y[0][0];
    return p;
}