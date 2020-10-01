import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
inar=lambda: list(map(int,input().split()))
inin=lambda: inar()[0]
inst=lambda: input().decode().rstrip('\n\r')


_T_=1 #inin()
for _t_ in range(_T_):
    n=inin()
    a=inar()
    d=[0 for i in range(n-1)]
    k=0
    for i in range(1,n):
        d[i-1]+=a[i]-a[i-1]
        k+=max(0,a[i]-a[i-1])
    x=(a[0]+k+1)//2
    print(x)
    q=inin()
    for _ in range(q):
        l,r,c=inar()
        l-=1; r-=1
        if l==0:
            a[0]+=c
        else:
            if d[l-1]>=0:
                k-=d[l-1]
            d[l-1]+=c
            if d[l-1]>=0:
                k+=d[l-1]
        if r==n-1:
            pass
        else:
            if d[r]>=0:
                k-=d[r]
            d[r]-=c
            if d[r]>=0:
                k+=d[r]
        x=(a[0]+k+1)//2
        print(x)
