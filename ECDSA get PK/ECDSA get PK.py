import ECDSA
from ECDSA import CurveOverFp, Point, generate_keypair, mult_inv
import random

C = CurveOverFp(0, 1, 7, 729787)
G = Point(1, 3)
n = C.order(G)
(d1, P) = generate_keypair(C, G, n)
# G 生成元 ； P 公钥 ；d 私钥
a = 1
b = 7
p = 729787
k = 369788


def sign(m, pri_key=d1):  # d is pri_key
    R = C.mult(G, k)
    r = R.x % n
    e = ECDSA.hash(m)
    s = mult_inv(k, n) * (e + pri_key * r) % n
    signature = [r, s]
    print("m is ", m)
    print("its signature is ", signature)
    return r, s


def verify(m, r, s, P):
    e = ECDSA.hash(m)
    w = mult_inv(s, n) % n
    ver = C.add(C.mult(G, e * w), C.mult(P, r * w))
    _r = ver.x
    _s = ver.y
    if _r == r:
        print("Verified")
        return 1
    else:
        #print("Verification failed")
        return 0


def weak_verify(e, r, s, P):
    w = mult_inv(s, n) % n
    # ver = e*w*G+r*w*P
    ver = C.add(C.mult(G, e * w), C.mult(P, r * w))
    _r = ver.x
    _s = ver.y
    if _r == r:
        print("Verified")
        return 1
    else:
        print("Verification failed")


def func(sign, msg, pk, msg_c, sign_c):
    r = sign[0]
    for j in range(1000000):  # 遍历j
        r = (r + n) % p
        if r==0
            continue
        s = sign[1]
        r_inverse = mult_inv(r, n)  # 求r^-1
        z = ECDSA.hash_and_truncate(msg, n)  # 消息hash

        y_squared = (r * r * r + a * r + b) % p
        if ECDSA.is_have_sqrt_model(y_squared, p) == False:
            continue
        y1, y2 = ECDSA.get_sqrt_model(y_squared, p)  # 求模平方根，y1,y2
        R1, R2 = Point(r, y1), Point(r, y2)
        Qs = [C.mult(C.minus(C.mult(R1, s), C.mult(G, z)), r_inverse),
              C.mult(C.minus(C.mult(R2, s), C.mult(G, z)), r_inverse)]
        # 根据公式求两个可能公钥
        # if pk == Qs[0] or pk == Qs[1]:  # 根据疑似公钥验证签名，若验证成功说明是正确公钥   //这里直接和生成的公钥对比了
        #if verify(msg_c, sign_c[0], sign_c[1], Qs[0]):
        if pk == Qs[0]:
            print('key_recovery:')
            print(Qs[0].x, Qs[0].y)
            return Qs[0]
        # elif verify(msg_c, sign_c[0], sign_c[1], Qs[1]):
        elif pk == Qs[1]:
            print('key_recovery:')
            print(Qs[1].x, Qs[1].y)
            return Qs[1]



def main():
    m = "12345"
    sig = sign(m)
    m_c = "123456"
    sig_c = sign(m_c)
    extend_pk=func(sig, m, P, m_c, sig_c)


if __name__ == '__main__':
    main()
