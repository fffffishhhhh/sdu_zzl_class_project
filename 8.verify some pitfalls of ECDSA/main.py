import ECDSA
from ECDSA import CurveOverFp, Point, generate_keypair, mult_inv
import random

C = CurveOverFp(0, 1, 7, 729787)
G = Point(1, 3)
n = C.order(G)
(d1, P) = generate_keypair(C, G, n)
(d2, P2) = generate_keypair(C, G, n)
# G 生成元 ； P 公钥 ；d 私钥
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


def weak_verify(e, r, s, P):
    w = mult_inv(s, n) % n
    ver = C.add(C.mult(G, e * w), C.mult(P, r * w))
    _r = ver.x
    _s = ver.y
    if _r == r:
        print("Verified")
        return 1
    else:
        print("Verification failed")


# 01 leak k
def test_leaking_k(m, r, s):
    e = ECDSA.hash(m)
    d = mult_inv(r, n) * (k * s - e) % n
    print("泄露k后 , d 为 :", d)
    return


# 02 reuse k
def test_reusing_k(m1, m2):
    r1, s1 = sign(m1)
    r1, s2 = sign(m2)
    e1 = ECDSA.hash(m1)
    e2 = ECDSA.hash(m2)
    _d = (s1 * e2 - s2 * e1) * mult_inv((s2 * r1 - s1 * r1) % n, n) % n
    print("重用k后 , d为 :", _d)
    return


# 03 reuse different k by different users
def test_reusing_k_users(m1, m2):
    r, s1 = sign(m1, d1)
    r, s2 = sign(m2, d2)
    e1 = ECDSA.hash(m1)
    e2 = ECDSA.hash(m2)
    _d2 = (s2 * e1 - s1 * e2 + s2 * r * d1) * mult_inv(s1 * r, n) % n
    _d1 = (s1 * e2 - s2 * e1 + s1 * r * d2) * mult_inv(s2 * r, n) % n
    print("d1 d2 are:", d1, d2)
    print("不同用户重复使用k攻击的结果为,_d1 _d2 are:", _d1, _d2)
    return 0


# 05 Verify & Forge a signature of Satoshi
def test_verify_and_forge(m1):
    r, s1 = sign(m1, d1)

    u = random.randint(1, n)
    v = random.randint(1, n)
    _R = C.add(C.mult(G, u), C.mult(P, v))
    _r = _R.x
    _e = _r * u * mult_inv(v, n) % n
    _s = _r * mult_inv(v, n) % n

    print("Test forged signature:")
    weak_verify(_e, _r, _s, P)
    return 0


# 06 schnorr and ECDSA
def schnorr(m, priv_key):
    R = C.mult(G, k)
    conj = str(R.x) + m
    e2 = ECDSA.hash(conj)
    s2 = (k + e2 * priv_key) % n
    return R, e2, s2


def test_schnorr_EDCSA(m, priv_key):
    R, e2, s2 = schnorr(m, priv_key)
    r1, s1 = sign(m, d1)
    e1 = ECDSA.hash(m)
    s1 = (e1 + r1 * priv_key) * mult_inv((s2 - e2 * priv_key) % n, n) % n
    _d = (s1 * s2 - e1) * mult_inv(s1 * e2 + r1, n) % n
    print("d is :", priv_key)
    print("by test_schnorr_ECDSA,d is :", _d)

    return


def main():
    m1 = "8381238149235897325829537233sdfsfsd"
    m2 = "askjdhajskfajkf12312432463643242342"
    r, s = sign(m1, d1)
    r, s2 = sign(m2, d1)
    verify(m,r,s,P)

    # 01 leak k
    print("d is :",d1)
    test_leaking_k(m1,r,s)

    # 02 reuse k
    print("d is :",d1)
    test_reusing_k(m1,m2)

    # 03 reuse different k by different users
    test_reusing_k_users(m1,m2)

    # 04 Malleability of ECDSA
    print("Verify (r,s):")
    verify(m1, r, s, P)
    print("Verify (r,-s):")
    _s_ = -s % n
    verify(m1, r, _s_, P)

    # 05 Verify & Forge a signature of Satoshi
    test_verify_and_forge(m1)

    # 06 schnorr and ECDSA
    test_schnorr_EDCSA(m1, d1)


if __name__ == '__main__':
    main()
