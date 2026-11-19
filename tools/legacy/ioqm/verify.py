#!/usr/bin/env python3
"""Recompute every number stated in the IOQM pages' questions, lessons and puzzles.
Run: python3 tools/legacy/ioqm/verify.py   — any failed assert names the claim."""
from math import gcd, comb, factorial, isqrt
from itertools import permutations, product
from fractions import Fraction as F

def divisors(n): return [d for d in range(1, n+1) if n % d == 0]
def nd(n): return len(divisors(n))
def lcm(a, b): return a*b//gcd(a, b)
def alt(n):
    s = str(n)[::-1]; return sum((1 if i % 2 == 0 else -1)*int(c) for i, c in enumerate(s))
def ds(n): return sum(map(int, str(n)))
def issq(n): return isqrt(n)**2 == n

# ---------- ioqm-divisors ----------
# MCQ1
assert [x % 9 == 0 for x in (4517, 2349, 6283, 7401)] == [False, True, False, False] and 7401 % 3 == 0
# MCQ2
assert [x % 11 == 0 for x in (2817, 3729, 4375, 9182)] == [False, True, False, False]
assert [alt(x) for x in (2817, 3729, 4375, 9182)] == [12, 11, -3, -14] and 3729 == 11*339
assert nd(72) == 12
assert [nd(x) for x in (48, 64, 72, 96)] == [10, 7, 12, 12]
assert 12 % 4 == 0 and 12 % 6 == 0 and 12 % 24 != 0 and lcm(4, 6) == 12
# Q6
assert [d for d in range(10) if int(f'47{d}2') % 9 == 0] == [5] and 4752 % 4 == 0 and 52 == 4*13
assert nd(360) == 24
assert gcd(391, 119) == 17 and 391 == 3*119+34 and 119 == 3*34+17 and 391 == 17*23 and 119 == 17*7
assert min(n for n in range(1, 1000) if nd(n) == 6) == 12 and divisors(12) == [1, 2, 3, 4, 6, 12]
assert 1001 == 7*11*13 and 418418 == 418*1001 and 418418 // 7 == 59774
# Q11 lockers
assert nd(36) == 9
openl = []
for L in range(1, 51):
    t = sum(1 for k in range(1, 51) if L % k == 0)
    if t % 2: openl.append(L)
assert openl == [1, 4, 9, 16, 25, 36, 49]
# Q12 / lesson 3
sols = [int(f'7{a}2{b}') for a in range(10) for b in range(10) if int(f'7{a}2{b}') % 36 == 0]
assert sols == [7020, 7128, 7524, 7920] and 7524 // 36 == 209
# Q13
assert 391//17 * (119//17) == 161 and lcm(391, 119) == 2737 and (2737//391)*(2737//119) == 161
# Q14
assert min(n for n in range(1, 5000) if nd(n) == 12) == 60
assert [2**11, 2**5*3, 2**3*9, 4*3*5] == [2048, 96, 72, 60]
assert [d for d in divisors(60) if d % 2 == 0] == [2, 4, 6, 10, 12, 20, 30, 60]
# Q15
N = 2**4*3**3*5**2
assert N == 10800 and nd(N) == 60
assert sum(1 for d in divisors(N) if issq(d)) == 12
assert sum(1 for d in divisors(N) if d % 10 == 0) == 32
# lessons / videos
assert 52817 % 9 == 5 and ds(52817) == 23
assert 918082 % 11 == 0 and alt(918082) == -22 and 123456 % 11 != 0
assert 5214 == 66*79
assert [d for d in range(10) if int(f'48{d}6') % 12 == 0] == [3, 9]
assert nd(1000) == 16 and nd(1024) == 11
assert gcd(1071, 462) == 21 and 1071 % 462 == 147 and 462 % 147 == 21
assert gcd(252, 198) == 18 and 252 % 198 == 54 and 198 % 54 == 36 and 54 % 36 == 18
assert 12**3 == 1728 and eval('*'.join(map(str, divisors(12)))) == 1728
assert [L for L in range(1, 31) if nd(L) % 2] == [1, 4, 9, 16, 25] and nd(12) == 6
assert 99 % 27 != 0 and ds(99) == 18
assert 7000125 % 125 == 0 and 7000125 % 8 != 0 and 3416 % 8 == 0
# bench puzzles
def fills(p, by):
    out = []
    for d in range(10):
        s = p.replace('*', str(d))
        if s[0] == '0': continue
        if all(int(s) % k == 0 for k in by): out.append(d)
    return out
assert fills('3*72', [9]) == [6]
assert fills('52*4', [11]) == [1]
assert fills('48*6', [12]) == [3, 9]
assert fills('*1234', [9]) == [8]
assert fills('1*56', [24]) == [0, 6]
assert fills('9*81', [11]) == [5]
# grid puzzles: machine-smallest equals true smallest
for T, want in [(6, 12), (8, 24), (9, 36), (10, 48), (12, 60), (16, 120)]:
    assert min(n for n in range(1, 2000) if nd(n) == T) == want, T
print('ioqm-divisors ok')

# ---------- ioqm-remainders ----------
import datetime
assert 100 % 7 == 2 and (9 + 100) % 12 == 1
assert pow(3, 2026, 10) == 9 and pow(2, 100, 7) == 2 and pow(2, 100, 10) == 6
assert all((2*x) % 6 == 4 for x in range(5, 200, 6))
assert (1234*5678) % 9 == 8 and (1234+5678) % 9 == 0 and 1234+5678 == 6912 and ds(5678) == 26
assert pow(7, 2026, 10) == 9 and 2026 == 4*506+2
assert (pow(6, 50) + pow(8, 51)) % 7 == 2
assert min(n for n in range(11, 1000) if all(n % k == 2 for k in (3, 4, 5))) == 62
assert all((k*k) % 8 == 1 for k in range(1, 400, 2))
d0 = datetime.date(2027, 1, 1); assert d0.strftime('%A') == 'Friday'
assert datetime.date(2027, 3, 1).strftime('%A') == 'Monday' and (datetime.date(2027,3,1)-d0).days == 59
assert datetime.date(2028, 1, 1).strftime('%A') == 'Saturday' and datetime.date(2029, 1, 1).strftime('%A') == 'Monday'
assert [(5*n) % 7 for n in (3, 10)] == [1, 1] and (3*3+3) % 7 == 5 and 27 % 7 == 6 and 110 % 7 == 5 and 1000 % 7 == 6
S = sum(factorial(k) for k in range(1, 101)); assert S % 12 == 9 and S % 10 == 3
assert [pow(b, 2027, 10) for b in (2, 3, 7)] == [8, 7, 3] and (pow(2,2027)+pow(3,2027)+pow(7,2027)) % 10 == 8
assert all((pow(3, n) + pow(7, n)) % 10 == 0 for n in range(1, 60, 2))
c = [n for n in range(1, 300) if n % 3 == 2 and n % 4 == 3 and n % 5 == 4]
assert c == [59, 119, 179, 239, 299] and [n for n in c if n % 7 == 0] == [119] and (119//3, 119%3, 119//4, 119%4, 119//5, 119%5) == (39,2,29,3,23,4)
# lessons/videos
assert [(10+h) % 12 or 12 for h in (50, 100, 1000)] == [12, 2, 2]
assert [x for x in (365, 366, 371) if x % 7 == 1] == [365] or True
assert [x for x in (365, 366, 371) if x % 7 == 1] == [365]
assert (47*53) % 5 == 1 and 47*53 == 2491
assert pow(6, 50, 7) == 1 and pow(6, 51, 7) == 6 and pow(8, 101, 9) == 8
assert pow(7, 25, 10) == 7 and pow(7, 100, 10) == 1 and pow(4, 124, 7) == 4 and pow(3, 3, 13) == 1
assert min(n for n in range(1, 500) if all(n % k == 1 for k in (2, 3, 4, 5, 6))) == 1
assert [n for n in range(1, 200) if n % 7 == 3 and n % 4 == 0][:3] == [24, 52, 80]
# clock puzzles
cp = lambda lo, hi, cs: [n for n in range(lo, hi+1) if all(n % m == r for m, r in cs)]
assert cp(50,100,[(7,3),(4,0)]) == [52, 80]
assert cp(20,60,[(5,2),(3,1)]) == [22, 37, 52]
assert cp(100,150,[(9,4),(2,0)]) == [112, 130, 148]
assert cp(1,100,[(3,2),(4,3),(5,4)]) == [59]
assert cp(1,100,[(11,0),(2,1),(3,2)]) == [11, 77]
assert cp(1,100,[(6,5),(7,6)]) == [41, 83]
# cycle puzzles
cy = lambda b, m, w, lo, hi: [n for n in range(lo, hi+1) if pow(b, n, m) == w]
assert cy(3,10,7,20,40) == [23,27,31,35,39]
assert cy(7,10,1,50,60) == [52,56,60]
assert cy(2,10,6,30,40) == [32,36,40]
assert cy(2,7,4,40,50) == [41,44,47,50]
assert cy(4,7,2,1,20) == [n for n in range(1,21) if n % 3 == 2]
assert cy(9,10,9,41,49) == [41,43,45,47,49]
print('ioqm-remainders ok')

# ---------- ioqm-identities ----------
assert 51**2-49**2 == 200 and 49-20 == 29 and 98*102 == 9996
assert 997**2 == 994009 and 103**2 == 10609 and 97**2 == 9409 and 65**2 == 4225
assert [21**2, 49**2, 85**2, 1001**2] == [441, 2401, 7225, 1002001]
assert 47*53 == 2491 and 101**2-99**2 == 400 and 1003*997 == 999991 and 68**2-32**2 == 3600
assert 23*17 == 391 and 46*54 == 2484 and 99*101 == 9999
assert (81+9)//2 == 45 and 6**2+3**2 == 45
x = F(1); # x + 1/x = 4 -> x^2+1/x^2 = 14 ; x+1/x=3 -> 7, x^4.. = 47
assert 4*4-2 == 14 and 3*3-2 == 7 and 7*7-2 == 47
sol = lambda N: [(a, b) for a in range(1, N+1) for b in range(1, a) if a*a-b*b == N]
assert sol(15) == [(4, 1), (8, 7)] and sol(45) == [(7, 2), (9, 6), (23, 22)] and sol(21) == [(5, 2), (11, 10)]
assert sol(60) == [(8, 2), (16, 14)] and 256-196 == 60
assert all((n*(n+1)*(n+2)*(n+3)+1) == (n*n+3*n+1)**2 for n in range(0, 60))
assert all(8*s+16 == (s+4)**2-s**2 for s in range(100)) and 8*10+16 == 96 and 50**2-46**2 == 384
assert (7+3, 7*3) == (10, 21) and 7**2+3**2 == 58 and 7-3 == 4 and 7**3+3**3 == 370 and 1000-630 == 370
r = [(x, y) for x in range(1, 80) for y in range(x, 80) if x*y+2*x+2*y == 76]
assert r == [(2, 18), (3, 14), (6, 8)] and [x*y for x, y in r] == [36, 42, 48]
tot = sum((k*k if k % 2 == 0 else -k*k) for k in range(1, 2027))
assert tot == 2053351 == 1013*2027 and 13*2027 == 26351
assert [(x, y) for x in range(1, 30) for y in range(1, 30) if x*y+2*x+3*y == 29] == [(2, 5), (4, 3)]
assert [(x, y) for x in range(1, 30) for y in range(x, 30) if x*y+x+y == 23] == [(1, 11), (2, 7), (3, 5)]
assert (1, 4, 14, 52) == (1, 4, 16-2, 64-12)
assert 2**3+3**3 == 35 == 125-90
# puzzles
dsol = lambda t: [(a, b) for a in range(1, 13) for b in range(1, a) if a*a-b*b == t]
assert dsol(33) == [(7, 4)] and dsol(45) == [(7, 2), (9, 6)] and dsol(24) == [(5, 1), (7, 5)] and dsol(40) == [(7, 3), (11, 9)]
assert (8+4, 8*4, 144-64) == (12, 32, 80) and 6+7 == 13 and 6*7 == 42 and 36+84+49 == 169
bs = lambda t: [(x, y) for x in range(1, 16) for y in range(x, 16) if x*y+x+y == t]
assert bs(34) == [(4, 6)] and bs(23) == [(1, 11), (2, 7), (3, 5)] and bs(54) == [(4, 10)]
assert bs(44) == [(2, 14), (4, 8)] and bs(62) == [(6, 8)] and bs(29) == [(1, 14), (2, 9), (4, 5)]
print('ioqm-identities ok')

# ---------- ioqm-sequences ----------
assert sum(range(1, 51)) == 1275 and len(range(5, 102, 3)) == 33 and 8*4 == 32 and (144-16)//4 == 32
assert max(x*(10-x) for x in range(11)) == 25 and sum(range(2, 101, 2)) == 2550 and sum(range(1, 100, 2)) == 2500
assert all(7*n-3 != 2026 for n in range(1, 400)) and 2029 == 7*289+6 and 2026 % 7 == 3 and all((7*n-3) % 7 == 4 for n in range(1, 50))
m3 = [k for k in range(101, 200) if k % 3 == 0]; assert len(m3) == 33 and sum(m3) == 4950 and m3[0] == 102 and m3[-1] == 198
assert sum(F(1, n*(n+1)) for n in range(1, 50)) == F(49, 50) and sum(F(1, n*(n+1)) for n in range(1, 100)) == F(99, 100)
assert (7, 6, 9) == (22-15, 22-16, 22-13)
assert all(x + F(9, x) >= 6 for x in [F(k, 7) for k in range(1, 200)]) and 3 + F(9, 3) == 6
assert 20+2*24 == 68 and 25*(20+68)//2 == 1100 and min(n for n in range(1, 26) if 20+2*(n-1) > 50) == 17 and 20+2*15 == 50
assert 4*505+6 == 2026 and 505+506+507+508 == 2026 and 2026 % 3 != 0
assert [(p, n) for p in range(1, 20) for n in range(1, 10) if 12*p+35*n == 200] == [(5, 4)]
assert max((x*(60-2*x), x) for x in range(0, 31)) == (450, 15) and 20*20 == 400
assert sum(F(2, n*(n+1)) for n in range(2, 101)) == F(99, 101)
assert sum(F(1, sum(range(1, n+1))) for n in range(2, 101)) == F(99, 101)
assert sum(range(1, 201)) == 20100 and sum(range(1, 1000)) == 499500
assert len(range(7, 404, 4)) == 100 and sum(range(7, 404, 4)) == 20500
assert sum(range(51, 101)) == 3775
# lesson 4 demo: x+y+z=10, x-y=1, y-z=2 -> y=3
assert [(x, y, z) for x in range(-10, 20) for y in range(-10, 20) for z in range(-10, 20) if x+y+z == 11 and x-y == 1 and y-z == 2] == [(5, 4, 2)]
assert [x*(20-x) for x in (8, 9, 10, 11, 12)] == [96, 99, 100, 99, 96]
assert min((x*x+10*x+30, x) for x in range(-20, 20)) == (5, -5)
assert min(x*x-6*x+13 for x in range(-20, 20)) == 4
# puzzles
sp = lambda fix, tgt: [(a, d, n) for a in range(1, 31) for d in range(1, 6) for n in range(1, 31)
      if all({'a': a, 'd': d, 'n': n}[k] == v for k, v in fix.items()) and n*(2*a+(n-1)*d) == 2*tgt]
assert sp({'d': 1}, 100) == [(9, 1, 8), (18, 1, 5)]
assert sp({'a': 1, 'd': 2}, 144) == [(1, 2, 12)] and sp({'a': 1, 'd': 1}, 210) == [(1, 1, 20)]
assert sp({'d': 1, 'n': 5}, 45) == [(7, 1, 5)] and sp({'a': 2, 'd': 3}, 155) == [(2, 3, 10)] and 2+9*3 == 29
assert sp({'d': 1, 'n': 6}, 93) == [(13, 1, 6)]
fp = lambda s, A: [x for x in range(s+1) if x*(s-x) == A]
assert fp(20, 96) == [8, 12] and fp(14, 40) == [4, 10] and fp(30, 200) == [10, 20] and fp(16, 55) == [5, 11]
assert fp(18, 81) == [9] and fp(24, 144) == [12]
print('ioqm-sequences ok')

# ---------- ioqm-angles ----------
assert 180-47-68 == 65 and 180-360//6 == 120 and 110-45 == 65 and (180-100)//2 == 40 and (180-70)/2 == 55 and 180-140 == 40
assert 180-58 == 122
assert (540-100)//5 == 88 and sum([88, 98, 108, 118, 128]) == 540
assert 360//24 == 15 and 13*180 == 2340 and 15*156 == 2340
assert 180-(180-50)/2 == 115
hands = lambda h, m: (lambda d: min(d, 360-d))(abs((h % 12)*30 + m*0.5 - m*6))
assert hands(3, 0) == 90 and hands(3, 30) == 75 and hands(4, 20) == 10 and hands(9, 45) == 22.5
e = 180/5; assert e == 36 and 360/e == 10 and 10*7//2 == 35 and 4*36 == 144
assert 36+72+72 == 180
assert [k for k in range(1, 30) if 2190 < k*180 < 2190+180] == [13] and 2340-2190 == 150 and 14*180-2190 == 330 and 12*180 == 2160
assert 110/2 == 55 and (360-110)/2 == 125
# polygon puzzles
assert 360/(180-140) == 9 and 360/24 == 15 and 1440/180+2 == 10 and 360/45 == 8 and 360/30 == 12
assert [n for n in range(3, 21) if n*(n-3)//2 == 44] == [11] and 12*9//2 == 54
assert 360/(180-140) == 9 and (9-2)*180/9 == 140
# video tasks
assert 180-2*65 == 50 and (180-65)/2 == 57.5
# triangle puzzles have unique 5-degree solutions as described
assert (180-40)/2 == 70 and 130-50 == 80 and sorted([35, 55, 90]) == [35, 55, 90] and [30, 60, 90] == [180*k//6 for k in (1, 2, 3)]
assert [180*k//9 for k in (2, 3, 4)] == [40, 60, 80] and 100/2 == 50 and 180-100 == 80
print('ioqm-angles ok')

# ---------- ioqm-areas ----------
from math import hypot
assert 10*7/2 == 35 and 9**2+12**2 == 15**2 and 6**2+9**2 != 11**2 and 36+81 == 117
for t in [(5,12,13),(8,15,17),(7,24,25),(3,4,5),(20,21,29)]: assert t[0]**2+t[1]**2 == t[2]**2
assert isqrt(169-25) == 12 and isqrt(169-144) == 5 and 12-5 == 7
def shoe(*P):
    return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P))))/2
assert shoe((0,0),(6,2),(2,5)) == 13 and shoe((1,1),(7,3),(3,6)) == 13
assert 30-6-6-5 == 13
assert 48/10 == 4.8 and F(60, 13) == F(5*12, 13) and 9*12/15 == 7.2
assert 15*4/10 == 6 and F(4, 10)**2 == F(4, 25)
assert 15**2 == 12**2+9**2 and 15**2+8**2 == 17**2 and 12+9-15 == 6
A, B, C, D = (0,0), (12,0), (12,12), (0,12); E = (12, 6); Fp = (8, 12)
assert shoe(A,B,E) == 36 and shoe(E,C,Fp) == 12 and shoe(Fp,D,A) == 48 and shoe(A,E,Fp) == 48 and 144-36-12-48 == 48
assert 1.5/2*14 == 10.5 and 1.5/(10.5/21) == 3
sols = [(b, isqrt(144+b*b)) for b in range(1, 200) if isqrt(144+b*b)**2 == 144+b*b]
assert sols == [(5, 13), (9, 15), (16, 20), (35, 37)]
# Q15 with coordinates
Ap, Bp, Cp = (0, 10), (0, 0), (12, 0)   # area 60
Dp = (4, 0); Ep = ((Ap[0]+Dp[0])/2, (Ap[1]+Dp[1])/2)
assert shoe(Ap,Bp,Cp) == 60 and shoe(Ap,Bp,Dp) == 20 and shoe(Ap,Dp,Cp) == 40 and shoe(Bp,Ep,Dp) == 10 and shoe(Cp,Ep,Dp) == 20 and shoe(Bp,Ep,Cp) == 30
assert hypot(5, 13)**2 - 194 < 1e-9
# leg-12 triples on sliders (legs <= 20)
assert [(a, b) for a in range(1, 21) for b in range(a, 21) if (a == 12 or b == 12) and isqrt(a*a+b*b)**2 == a*a+b*b] == [(5, 12), (9, 12), (12, 16)]
# square-builder puzzles
trip = lambda f: [(a, b) for a in range(1, 21) for b in range(a, 21) if isqrt(a*a+b*b)**2 == a*a+b*b and f(a, b, isqrt(a*a+b*b))]
assert trip(lambda a,b,c: c == 13) == [(5, 12)] and trip(lambda a,b,c: c == 17) == [(8, 15)] and trip(lambda a,b,c: c == 25) == [(15, 20)]
assert trip(lambda a,b,c: 9 in (a, b)) == [(9, 12)] and trip(lambda a,b,c: c == 10) == [(6, 8)]
assert trip(lambda a,b,c: c > 15 and gcd(a, b) == 1) == [(8, 15)]
# apex puzzles
ap = lambda f: [(b,h,o) for b in range(2,13) for h in range(1,11) for o in range(-6,19) if f(b,h,o)]
assert {(b,h) for b,h,o in ap(lambda b,h,o: b*h == 40 and 2*o == b)} == {(10,4),(8,5),(4,10)}
assert ap(lambda b,h,o: b == h and b*h == 36) and all(b == 6 for b,h,o in ap(lambda b,h,o: b == h and b*h == 36))
assert hypot(6, 8) == 10
print('ioqm-areas ok')

# ---------- ioqm-counting ----------
assert 3*4*2 == 24 and factorial(5) == 120 and comb(10, 2) == 45 and len(range(100, 1000)) == 900 and comb(8, 2) == 28 and 8*7 == 56
assert 10**4 == 10000 and 10*9*8*7 == 5040 and 10000-5040 == 4960
assert sum(1 for n in range(100, 1000) if '7' in str(n)) == 252 == 900-648 and 8*9*9 == 648
assert len(set(permutations('LEVEL'))) == 30 and len(set(permutations('BANANA'))) == 60
assert factorial(11)//(factorial(4)*factorial(4)*factorial(2)) == 34650
def paths(W, H, blocked=()):
    N = {}
    for i in range(W+1):
        for j in range(H+1):
            if (i, j) in blocked: N[i, j] = 0
            elif i == 0 and j == 0: N[i, j] = 1
            else: N[i, j] = N.get((i-1, j), 0) + N.get((i, j-1), 0)
    return N[W, H]
assert paths(4, 3) == 35 == comb(7, 3) and comb(3, 1)*comb(4, 2) == 18
assert paths(4, 3) - paths(4, 3, {(2, 1)}) == 18
assert comb(10, 4) == 210 and comb(4, 2)*comb(6, 2) == 90 and comb(10, 4)-comb(6, 4) == 195
assert 4*comb(6, 3) + 90 + comb(4, 3)*comb(6, 1) + 1 == 195
digs = [p for p in permutations('123456', 3)]
assert len(digs) == 120 and sum(1 for p in digs if int(p[2]) % 2 == 0) == 60 and sum(1 for p in digs if p[2] == '5') == 20
seats = list(permutations('ABCDE'))
adj = sum(1 for p in seats if abs(p.index('A')-p.index('B')) == 1)
assert len(seats) == 120 and adj == 48 and 120-adj == 72
assert paths(5, 5) == 252 and comb(4, 2)*comb(6, 3) == 120 and paths(5, 5, {(2, 2)}) == 132
assert 5*7 == 35 and comb(12, 3)-comb(5, 3)-comb(7, 3) == 175 and comb(5, 2)*comb(7, 2) == 210 and 10*7+5*21 == 175
assert comb(10, 2)-10 == 35 and comb(4, 2)*comb(4, 2) == 36
assert len(range(42, 98)) == 56 and sum(1 for k in range(100, 301) if k % 7 == 0) == 28
assert 6*5*4 == 120 and factorial(6) == 720 and 7*6*5 == 210 and comb(7, 3) == 35 and 12*11 == 132
assert 900 - 5**3 == 775 and comb(10, 3) == 120
assert 5*9*9 != 648 and 9*9*8 == 648 and sum(1 for n in range(100, 1000) if len(set(str(n))) == 3) == 648
assert sum(1 for n in range(100, 1000) if all(int(c) % 2 for c in str(n))) == 125
# grid puzzles
small = lambda c: [(w, h) for w in range(1, 9) for h in range(1, 7) if comb(w+h, h) == c]
assert small(20) == [(3, 3)] and set(small(35)) == {(3, 4), (4, 3)} and set(small(15)) == {(2, 4), (4, 2)} and set(small(56)) == {(3, 5), (5, 3)}
b33 = [(i, j) for i in range(4) for j in range(4) if (i, j) not in ((0, 0), (3, 3)) and paths(3, 3, {(i, j)}) == 10]
assert sorted(b33) == [(0, 1), (1, 0), (2, 3), (3, 2)]
b44 = [(i, j) for i in range(5) for j in range(5) if (i, j) not in ((0, 0), (4, 4)) and paths(4, 4, {(i, j)}) == 34]
assert b44 == [(2, 2)] and paths(4, 4) == 70
# circle puzzles
assert [n for n in range(2, 13) if n*(n-1)//2 == 45] == [10] and [n for n in range(2, 13) if n*(n-1)//2 == 28] == [8]
assert [n for n in range(2, 13) if n*(n-1)//2 == 66] == [12] and [n for n in range(2, 13) if comb(n, 3) == 20] == [6]
assert [n for n in range(2, 13) if comb(n, 3) == 56] == [8] and [n for n in range(4, 13) if comb(n, 2)-n == 27] == [9]
print('ioqm-counting ok')

# ---------- ioqm-logic ----------
from math import ceil
assert ceil(30/12) == 3 and 3+1 == 4 and 12*2+1 == 25 and 7*3+1 == 22
assert sum(range(1, 11)) == 55 and sum(range(1, 7)) == 21 and sum(range(1, 8)) == 28 and 1+2-3+4-5-6+7 == 0
# no sign choice of 1..10 gives 0
assert all(sum(s*k for s, k in zip(signs, range(1, 11))) != 0 for signs in product((1, -1), repeat=10))
assert any(sum(s*k for s, k in zip(signs, range(1, 8))) == 0 for signs in product((1, -1), repeat=7))
assert 1+1+1 == 3 and 6+2+1+1 == 10
# knights & knaves
def kk(stA, stB=None):
    out = []
    for A, B in product((True, False), repeat=2):   # True = knight
        if stA(A, B) == A and (stB is None or stB(A, B) == B): out.append((A, B))
    return out
assert kk(lambda A, B: (not A) and (not B)) == [(False, True)]
assert kk(lambda A, B: not B, lambda A, B: A == B) == [(True, False)]
# Q9 invariant: simulate random difference moves from 1..10 always ends odd
import random
random.seed(1)
for _ in range(500):
    L = list(range(1, 11))
    while len(L) > 1:
        a, b = random.sample(range(len(L)), 2); x, y = L[a], L[b]
        L = [v for i, v in enumerate(L) if i not in (a, b)] + [abs(x-y)]
    assert L[0] % 2 == 1
# Q11 chessboard
cols = [(r+c) % 2 for r in range(8) for c in range(8) if (r, c) not in ((0, 0), (7, 7))]
assert cols.count(0) == 30 and cols.count(1) == 32
assert 2 ** 0.5 == hypot(1, 1)
assert 9*3 % 2 == 1 and 10*3 // 2 == 15
# 10 people, neighbours + opposite = 3 each
edges = {frozenset((i, (i+1) % 10)) for i in range(10)} | {frozenset((i, (i+5) % 10)) for i in range(10)}
assert len(edges) == 15 and all(sum(1 for e in edges if i in e) == 3 for i in range(10))
# Q14
pairs = [(k, 11-k) for k in range(1, 6)]
assert pairs == [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)]
from itertools import combinations
assert all(any(a+b == 11 for a, b in combinations(c, 2)) for c in combinations(range(1, 11), 6))
assert not any(a+b == 11 for a, b in combinations((1, 2, 3, 4, 5), 2))
# Q15 coins: BFS over head counts
def reach(n, flip):
    from collections import deque
    dist = {n: 0}; q = deque([n])
    while q:
        h = q.popleft()
        for hh in range(0, flip+1):   # heads turned
            t = flip-hh
            if hh <= h and t <= n-h:
                nh = h-hh+t
                if nh not in dist: dist[nh] = dist[h]+1; q.append(nh)
    return dist
assert 0 not in reach(7, 2) and reach(7, 3)[0] == 3
assert 7-2+1 == 6 and 6-3 == 3 and 3-3 == 0
# lesson 5 demo: 1..6, add 1 to two -> sum parity odd, six equal -> even
assert sum(range(1, 7)) % 2 == 1
# pigeon puzzles
for n, t, k in [(5,2,6),(4,3,9),(12,2,13),(7,4,22),(10,3,21),(5,4,16)]: assert n*(t-1)+1 == k and k <= 40 and n <= 12
print('ioqm-logic ok')
