def z_score(s, mean, std):
    return (s - mean) / std

def z_to_x(z, mean, std):
    return (z * std) + mean


mean = 140000
std_dev = 3000
x = 150000

z = z_score(x, mean, std_dev)
back_to_x = z_to_x(z, mean, std_dev)

print('z 점수: {}'.format(z)) # 3.3333333333333335
print('x로 되돌리기: {}'.format(back_to_x)) # 150000.0
