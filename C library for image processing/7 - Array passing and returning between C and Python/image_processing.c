
void convolution(int *image,int *return_image,int *kernel,int image_width, int image_height, int kernel_size, int kernel_normalizer) {
    
    int border_width = (kernel_size-1)/2;
    int image_starting_x = 0;
    int image_starting_y = 0;
    int image_ending_x = image_width - kernel_size + 1;
    int image_ending_y = image_height - kernel_size + 1;
    
    int i,j,u,v;
    int sum;

    for(i=image_starting_y;i<image_ending_y;i++) {
        for(j=image_starting_x;j<image_ending_x;j++) {
            
            //current left top corner pixel is i,j
            sum = 0;
            for(u=0;u<kernel_size;u++) {
                for(v=0;v<kernel_size;v++) {
                    sum += (*(image + image_width*(i+u) + j+v))*(*(kernel + u*kernel_size + v));
                }
            }
            *(return_image + (image_width*(i+border_width)) + j+border_width) = (sum/kernel_normalizer);
        }
    }
}

// void sobel_operator(int *image,int *grad_x,int *grad_y,int image_width,int image_height) {

//     int kernel_x[3][3] = {{1,0,-1},{2,0,-2},{1,0,-1}};
//     int kernel_y[3][3] = {{1,2,1},{0,0,0},{-1,-1,-1}};

//     for 

// }