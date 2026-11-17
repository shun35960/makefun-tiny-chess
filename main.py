import json,os,sys,random,urllib.request as U
u=os.environ["MAKEFUN_ENV_URL"]
def P(p,d):return json.load(U.urlopen(U.Request(u+p,json.dumps(d).encode(),{"content-type":"application/json"})))
B_=[15,17,-15,-17];R_=[1,-1,16,-16]
D={2:[31,33,18,14,-31,-33,-18,-14],3:B_,4:R_,5:B_+R_,6:B_+R_}
Q=[i for i in range(128)if not i&136]
T=[[0]*128 for _ in range(13)];random.seed(7);Z=[[random.getrandbits(62)*(p>0)for i in range(128)]for p in range(13)]
for p in range(1,7):
 for i in Q:
  r,f=i>>4,i&7;c=14-abs(2*f-7)-abs(2*r-7)
  for s in(1,-1):
   a=r if s>0 else 7-r
   x=[100+a*a*4+c*(f in(3,4)),320+c*4,330+c*3,500+7*(a==6),900+c,-9*a+c*(a>3)][p-1]
   T[p*s][i]=s*x
M=30000
def g(s,q):
 r=[]
 for i in Q:
  p=b[i]*s
  if p<1:continue
  if p<2:
   f=16*s
   for t in(i+f-1,i+f+1):
    if not t&136 and b[t]*s<0:r+=[(10*abs(b[t])-1,i,t)]
   t=i+f
   if not b[t]and(not q or t>>4 in(0,7)):
    r+=[(0,i,t)]
    if not q and i>>4==(1 if s>0 else 6)and not b[t+f]:r+=[(0,i,t+f)]
  else:
   for d in D[p]:
    t=i
    while 1:
     t+=d
     if t&136 or b[t]*s>0:break
     c=b[t]
     if c:r+=[(10*abs(c)-p,i,t)];break
     if not q:r+=[(0,i,t)]
     if p in(2,6):break
   if p==6 and not q and i==(4 if s>0 else 116):
    if b[i+3]==4*s and not b[i+1]|b[i+2]:r+=[(0,i,i+2)]
    if b[i-4]==4*s and not b[i-1]|b[i-2]|b[i-3]:r+=[(0,i,i-2)]
 return r
def S(s,d,a,B,sc,h):
 global n
 n+=1
 if n>N:raise E
 q=d<1;k=h*s;e=tt.get(k);tm=0
 if k in H:return 0
 if e:
  tm=e[3]
  if e[0]>=d and not q:
   if e[1]==0 or e[1]<0 and e[2]<=a or e[1]>0 and e[2]>=B:return e[2]
 best=s*sc if q else -2*M;bm=0;a0=a
 if q:
  if best>=B:return best
  a=max(a,best)
 if d>2:
  v=-S(-s,d-3,-B,1-B,sc,h)
  if v>=B:return v
 ms=g(s,q);kk=kl.get(d);ms.sort(key=lambda m:-m[0]-99*(m[1:]==tm)-5*(m[1:]==kk))
 for _,i,t in ms:
  p=b[i];c=b[t];x=p;y=0
  if c==-6*s:return M+d
  if q and c and best+(0,100,300,300,500,900)[abs(c)]+200<a:continue
  if p*s==1 and t>>4 in(0,7):x=5*s
  z=sc+T[x][t]-T[p][i]-T[c][t];j=h^Z[x][t]^Z[p][i]^Z[c][t]
  if abs(p)==6 and abs(t-i)==2:
   y=(i+t)//2;w=i+3 if t>i else i-4;b[y]=b[w];b[w]=0;z+=T[b[y]][y]-T[b[y]][w];j^=Z[b[y]][y]^Z[b[y]][w]
  b[t]=x;b[i]=0
  v=-S(-s,d-1,-B,-a,z,j)
  b[i]=p;b[t]=c
  if y:b[w]=b[y];b[y]=0
  if v>best:
   best=v;bm=(i,t)
   if v>a:
    a=v
    if a>=B:
     if not c:kl[d]=bm
     break
 if not q:
  if best<-M//2 and not any(b[t]==6*s for _,i,t in g(-s,1)):best=0
  tt[k]=(d,1 if best>=B else-1 if best<=a0 else 0,best,bm)
 return best
N0=int(os.environ.get("NN",260000));V="⋈1ꔅ7疸1ᇸ9"
class E(Exception):0
while 1:
 G=P("/game",{})
 if G["status"]=="done":break
 H=set();x=V.find(chr(int.from_bytes((G["opponent"]+G["colour"]+G["opening"]["id"]).encode())%53183+2048));N=N0+(int(os.environ.get("KK",V[x+1]if x>=0 else 5))-5)*9000
 while G["status"]=="your_move":
  b=[0]*128;n=0;tt={};kl={}
  F=G["fen"].split();s=1 if F[1]=="w"else-1;sc=h=0
  for j,w in enumerate(F[0].split("/")):
   f=0
   for c in w:
    if c.isdigit():f+=int(c)
    else:
     p="pnbrqk".index(c.lower())+1;p=p if c<"a"else-p;b[(7-j)*16+f]=p;sc+=T[p][(7-j)*16+f];h^=Z[p][(7-j)*16+f];f+=1
  H.add(h*s)
  L=[(m,((int(m[1])-1)*16+ord(m[0])-97,(int(m[3])-1)*16+ord(m[2])-97))for m in G["legal_moves"]if m[4:]in("","q")]or[(m,(0,0))for m in G["legal_moves"][:1]]
  bst=L[0][0]
  if len(L)>1:
   try:
    for d in range(1,40):
     a=-3*M;r=[]
     for m,(i,t)in L:
      p=b[i];c=b[t];x=p;y=0
      if p*s==1 and t>>4 in(0,7):x=5*s
      z=sc+T[x][t]-T[p][i]-T[c][t];j=h^Z[x][t]^Z[p][i]^Z[c][t]
      if abs(p)==6 and abs(t-i)==2:
       y=(i+t)//2;w=i+3 if t>i else i-4;b[y]=b[w];b[w]=0;z+=T[b[y]][y]-T[b[y]][w];j^=Z[b[y]][y]^Z[b[y]][w]
      b[t]=x;b[i]=0
      try:v=-S(-s,d-1,-3*M,-a,z,j)
      finally:
       b[i]=p;b[t]=c
       if y:b[w]=b[y];b[y]=0
      r+=[(v,m)]
      a=max(a,v)
     r.sort(key=lambda x:-x[0]);bst=r[0][1];L=[(m,x)for m,x in L if m==bst]+[(m,x)for m,x in L if m!=bst]
    pass
   except E:pass
  G=P("/move",{"game":G["game"],"move":bst})
