N,K,L = map(int,input('Enter integers:').split())
d = min (K,2*L)
area  = 4*L*L + (N-1)*(4*L*d-d*d)
print('Total area:',area)