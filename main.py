from converter import *
import colorsys

#Sistema YIQ, Y é intensidade e IQ são cruminâncias
y,i,q = RGBb2YIQ (200,100,50)
print("\nYIQ = ", y,i,q)

r,g,b = YIQ2RGB(y,i,q)
print("RGB = ", r,g,b, "\n")

#HSV = ","
a = colorsys.rgb_to_hsv(45./255., 0./255., 111./255.)
print(a)

#Sistema HSB, Quando a imagem é cinza o S é 0, logo a matiz 
# é indefinida


#Sistema LAB, L é intensidade, luma... e AB são cruminâncias
#Quando a imagem é cinza não tem-se cruminância, 
# ou seja AeB =0 e a intensidade é similar ao do HSB
