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
k = random.randint(1, n)


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
        print("Verification failed")


def forge(G, P, u, v):
    R = C.add(C.mult(G, u), C.mult(P, v))
    _r = R.x
    _s = _r * mult_inv(v, n) % n


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


def forge(G, P, u, v):
    R = C.add(C.mult(G, u), C.mult(P, v))
    _r = R.x
    _s = _r * mult_inv(v, n) % n
    _e = u * _s % n
    return _r, _s, _e


def main():
    r, s, e = forge(G, P, 1, 1)
    weak_verify(e, r, s, P)


if __name__ == '__main__':
    main()
