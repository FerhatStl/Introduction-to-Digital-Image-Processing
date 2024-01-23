close all;
clear all;
clc;
pkg load image;

RGB =imread('example.jpg');

figure;

[X1,map] = rgb2ind(RGB);
subplot(2,2,1);
imshow(X1,map)
title('RGB')


X2 = ind2gray(X1,map);
subplot(2,2,2);
imshow(X2)
title('Grayscale')

% Unexpectedly it doesn't show X1 as rotated.
X3=imrotate(X2,45,'nearest','loose');
subplot(2,2,3);
imshow(X3)
title('Rotated')

subplot(2,2,4);
imhist(X2)
title('Histogram')
