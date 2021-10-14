def RGBb2YIQ (r,  g, b):
    y = 0.299*r + 0.587*g + 0.114*b
    i = 0.596*r - 0.274*g - 0.322*b
    q = 0.211*r - 0.523*g + 0.312*b
    return (round(y,2), round(i,2), round(q,2))

def YIQ2RGB (y,  i, q):
    r = 1.0*y + 0.956*i + 0.621*q
    g = 1.0*y - 0.272*i - 0.647*q
    b = 1.0*y - 1.106*i + 1.703*q
    return (round(r,2),  round(g,2), round(b,2))
