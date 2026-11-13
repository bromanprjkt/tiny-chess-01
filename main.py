import json,os,sys,urllib.request as u
V=[0,100,320,330,500,900,0]
PS="SSSS~~~~]]gqXX]lSSSgXNISX]]?SSSS!+55+?SS5S]b5Xbg5Sbg5X]b+?SX!+55?IIIISSSISX]IXX]IS]]I]]]IXSS?IIISSSSX]]]NSSSNSSSNSSSNSSSNSSSSSSX?IINISSSISXXNSXXSSXXIXXXISXS?IIN5++!5++!5++!5++!?55+I???ggSSgq]S!+5?5?IS5Igq5Iq{5Iq{5Igq55SS!555"
PI=[ord(c)-83 for c in PS]
BK=json.load(open(__file__[:-7]+'book.txt'))
W=10**6;M=10**5;N=60000
b=[0]*128;s=0;c=0;e=-1;k=[4,116];z=[];TT={};KL=[[0,0]for _ in range(128)];n=0;H={};G=-1;zh=0;fm=5
CD={c:i+1+2*(i>5) for i,c in enumerate('PNBRQKpnbrqk')}
KD=(-17,-16,-15,-1,1,15,16,17);ND=(-33,-31,-18,-14,14,18,31,33);BD=(-17,-15,15,17);RD=(-16,-1,1,16)
_R=987654321
def _z():
 global _R;_R=(_R*6364136223846793005+1)&(1<<64)-1;return _R
ZP=[[_z() for _ in range(128)] for _ in range(15)]
ZS=_z();ZC=[_z() for _ in range(16)];ZE=[_z() for _ in range(8)]
HS=[0]*1920
class A(Exception):pass
def F(f):
 global b,s,c,e,k,z,zh,fm
 b=[0]*128;p=f.split();zh=0;fm=int(p[5])
 for r,w in enumerate(p[0].split('/')):
  x=0
  for ch in w:
   if ch.isdigit():x+=int(ch)
   else:
    q=(7-r)*16+x;b[q]=CD[ch];zh^=ZP[CD[ch]][q]
    if ch=='K':k[0]=q
    elif ch=='k':k[1]=q
    x+=1
 s=0 if p[1]=='w' else 8;c=0
 for ch in p[2]:
  if ch=='K':c|=1
  elif ch=='Q':c|=2
  elif ch=='k':c|=4
  elif ch=='q':c|=8
 e=-1
 if p[3]!='-':e=ord(p[3][0])-97+(int(p[3][1])-1)*16
 z=[];zh^=ZS if s else 0;zh^=ZC[c]
 if e>=0:zh^=ZE[e&7]
def X(q,by):
 for x in(q-15,q-17)if by==0 else(q+15,q+17):
  if not(x&0x88)and b[x]==(1 if by==0 else 9)and abs((x&7)-(q&7))==1:return 1
 for d in ND:
  x=q+d
  if not(x&0x88)and b[x]==(2 if by==0 else 10):return 1
 for d in KD:
  x=q+d
  if not(x&0x88)and b[x]==(6 if by==0 else 14):return 1
 for d in BD:
  x=q+d
  while not(x&0x88):
   v=b[x]
   if v:
    if v==(3 if by==0 else 11)or v==(5 if by==0 else 13):return 1
    break
   x+=d
 for d in RD:
  x=q+d
  while not(x&0x88):
   v=b[x]
   if v:
    if v==(4 if by==0 else 12)or v==(5 if by==0 else 13):return 1
    break
   x+=d
 return 0
def g(Q):
 m=[]
 for f in range(128):
  p=b[f]
  if not p or(p&8)!=s:continue
  t=p&7
  if t==1:
   d=16 if s==0 else-16;w=f+d;r=7 if s==0 else 0
   if not(w&0x88)and b[w]==0:
    if w>>4==r:
     for v in(5,4,3,2):m.append(f|w<<7|v<<14)
    elif not Q:
     m.append(f|w<<7)
     if f>>4==(1 if s==0 else 6)and b[f+2*d]==0:m.append(f|(f+2*d)<<7)
   for dd in(d-1,d+1):
    w=f+dd
    if w&0x88:continue
    v=b[w]
    if v and(v&8)!=s:
     if w>>4==r:
      for j in(5,4,3,2):m.append(f|w<<7|j<<14)
     else:m.append(f|w<<7)
    elif w==e and not v:m.append(f|w<<7)
  elif t==2 or t==6:
   for d in(ND if t==2 else KD):
    w=f+d
    if w&0x88:continue
    v=b[w]
    if not Q and not v:m.append(f|w<<7)
    elif v and(v&8)!=s:m.append(f|w<<7)
  else:
   for d in(BD if t==3 else RD if t==4 else BD+RD):
    w=f+d
    while not(w&0x88):
     v=b[w]
     if not v:
      if not Q:m.append(f|w<<7)
     else:
      if(v&8)!=s:m.append(f|w<<7)
      break
     w+=d
 if not Q:
  if s==0:
   if c&1 and b[5]==0 and b[6]==0 and b[4]==6 and b[7]==4 and not X(4,8)and not X(5,8)and not X(6,8):m.append(4|6<<7)
   if c&2 and b[3]==0 and b[2]==0 and b[1]==0 and b[0]==4 and b[4]==6 and not X(4,8)and not X(3,8)and not X(2,8):m.append(4|2<<7)
  else:
   if c&4 and b[117]==0 and b[118]==0 and b[116]==14 and b[119]==12 and not X(116,0)and not X(117,0)and not X(118,0):m.append(116|118<<7)
   if c&8 and b[115]==0 and b[114]==0 and b[113]==0 and b[112]==12 and b[116]==14 and not X(116,0)and not X(115,0)and not X(114,0):m.append(116|114<<7)
 o=[]
 for v in m:
  y(v)
  if not X(k[s>>3^1],s):o.append(v)
  U()
 return o
KP={0:13,7:14,4:12,112:7,119:11,116:3}
def y(m):
 global s,c,e,zh
 f=m&127;w=m>>7&127;r=m>>14&7;p=b[f];v=b[w];j=w;zo=zh
 if e>=0:zh^=ZE[e&7]
 zh^=ZC[c]
 if(p&7)==1 and w==e and v==0:
  j=w-16 if s==0 else w+16;v=b[j];b[j]=0
 np=r+s if r else p;zh^=ZP[p][f]^ZP[np][w]
 if v:zh^=ZP[v][j]
 b[w]=np;b[f]=0
 if(p&7)==6:
  k[s>>3]=w;rp=4 if s==0 else 12
  if w-f==2:zh^=ZP[rp][f+3]^ZP[rp][f+1];b[f+1]=b[f+3];b[f+3]=0
  elif f-w==2:zh^=ZP[rp][f-4]^ZP[rp][f-1];b[f-1]=b[f-4];b[f-4]=0
 z.append((m,v,j,c,e,zo));c&=KP.get(f,15)&KP.get(w,15);e=(f+w)//2 if(p&7)==1 and abs(w-f)==32 else-1;s^=8
 zh^=ZC[c]
 if e>=0:zh^=ZE[e&7]
 zh^=ZS
def U():
 global s,c,e,zh
 m,v,j,oc,oe,oz=z.pop();s^=8;f=m&127;w=m>>7&127;r=m>>14&7;p=b[w]
 b[f]=(1 if s==0 else 9)if r else p;b[w]=0
 if v:b[j]=v
 if(p&7)==6:
  k[s>>3]=f
  if w-f==2:b[f+3]=b[f+1];b[f+1]=0
  elif f-w==2:b[f-4]=b[f-1];b[f-1]=0
 c,e,zh=oc,oe,oz
def E():
 bb=b;Vv=V;PIi=PI;t=0;w=0;q=0;qe=0;kg=[]
 for i,p in enumerate(bb):
  if p:
   v=p&7;f=i&7;r=i>>4;m=f if f<4 else 7-f
   if v==6:kg.append((i,p));continue
   k=(v-1)*32
   if p&8:
    t-=Vv[v]+PIi[k+r*4+m]
    if v==3:q+=1
   else:
    t+=Vv[v]+PIi[k+(7-r)*4+m]
    if v==3:w+=1
   if v==5:qe=1
 for i,p in kg:
  f=i&7;r=i>>4;m=f if f<4 else 7-f;k=192-32*qe
  if p&8:t-=PIi[k+r*4+m]
  else:t+=PIi[k+(7-r)*4+m]
 if w>=2:t+=30
 if q>=2:t-=30
 return t if s==0 else-t
def O(m,t,kl=(0,0)):
 def j(v):
  if v==t:return 1<<28
  w=v>>7&127;x=b[w]
  if x:return 1000000+10*V[x&7]-V[b[v&127]&7]
  if v>>14&7:return 900000
  if v==kl[0]:return 800000
  if v==kl[1]:return 700000
  return HS[(b[v&127]<<7)|w]
 m.sort(key=j,reverse=True)
def Q(a,be,p):
 global n
 n+=1
 if n>N:raise A
 if p>100:return E()
 h=X(k[s>>3],s^8)
 if not h:
  v=E()
  if v>=be:return be
  if v>a:a=v
 m=g(not h)
 if not m:return -M+p if h else a
 O(m,0)
 for v in m:
  y(v);v=-Q(-be,-a,p+1);U()
  if v>=be:return be
  if v>a:a=v
 return a
def S(d,a,be,p):
 global n,s,c,e
 n+=1
 if n>N:raise A
 h=X(k[s>>3],s^8)
 if d<=0:return Q(a,be,p)
 K=zh
 if K in H:return 0
 v=TT.get(K);tm=0
 if v:
  ed,ef,vv,em=v;tm=em
  if ed>=d:
   if ef==0:return vv
   if ef==1 and vv>=be:return vv
   if ef==2 and vv<=a:return vv
 m=g(False)
 if not m:return -M+p if h else 0
 a0=a;kl=KL[p] if p<128 else(0,0);O(m,tm,kl);bs=-W;bm=m[0];bb=b
 for i,w in enumerate(m):
  cp=bb[w>>7&127]!=0;y(w)
  if i==0:v=-S(d-1,-be,-a,p+1)
  else:
   if d>2 and i>2 and not cp and not h:
    v=-S(d-2,-a-1,-a,p+1)
    if v>a:v=-S(d-1,-a-1,-a,p+1)
   else:v=-S(d-1,-a-1,-a,p+1)
   if a<v<be:v=-S(d-1,-be,-a,p+1)
  U()
  if v>bs:bs=v;bm=w
  if v>a:
   a=v
   if v>=be:
    if not cp:
     HS[(bb[w&127]<<7)|(w>>7&127)]+=d*d
     if w!=kl[0]:kl[1]=kl[0];kl[0]=w
    if abs(v)<M-1000:TT[K]=(d,1,v,w)
    return v
 if abs(bs)<M-1000:TT[K]=(d,0 if bs>a0 else 2,bs,bm)
 return bs
def R(d,m):
 a=-W;be=W;sc=[];O(m,0)
 for i,w in enumerate(m):
  y(w)
  if i==0:v=-S(d-1,-be,-a,1)
  else:
   v=-S(d-1,-a-1,-a,1)
   if a<v<be:v=-S(d-1,-be,-a,1)
  U();sc.append((v,w));a=max(a,v)
 sc.sort(key=lambda x:-x[0]);return sc
def C(m):
 f=m&127;w=m>>7&127;r=m>>14&7
 s='abcdefgh'[f&7]+str((f>>4)+1)+'abcdefgh'[w&7]+str((w>>4)+1)
 if r:s+='nbrq'[r-2]
 return s
def r(f,L,gm=0):
 global n,G
 if gm!=G:G=gm;H.clear()
 F(f);H[zh]=H.get(zh,0)+1
 m=g(False);ls=set(L);m=[v for v in m if C(v) in ls]
 if not m:return L[0]
 if len(m)==1:return C(m[0])
 if fm==5 and (j:=BK.get(str((zh>>41)&2047)))is not None and j<len(m):
  bm=m[j];y(bm);K=zh;U();H[K]=H.get(K,0)+1;return C(bm)
 if len(TT)>400000:TT.clear()
 bs=-W;bm=m[0];sc=[];n=0
 try:
  for d in range(1,64):
   sc=R(d,m);bs,bm=sc[0]
   if bs>M-1000 or bs<-M+1000:break
 except A:pass
 if sc:
  y(bm);K=zh;U()
 y(bm);K=zh;U();H[K]=H.get(K,0)+1
 return C(bm)
E0=os.environ.get("MAKEFUN_ENV_URL")
def P(p,y):
 q=u.Request(E0+p,data=json.dumps(y).encode(),headers={"content-type":"application/json"})
 with u.urlopen(q) as w:return json.load(w)
def main():
 while 1:
  q=P("/game",{})
  if q["status"]=="done":break
  while q["status"]=="your_move":
   try:mv=r(q["fen"],q["legal_moves"],q["game"])
   except Exception:mv=q["legal_moves"][0]
   if mv not in q["legal_moves"]:mv=q["legal_moves"][0]
   q=P("/move",{"game":q["game"],"move":mv})
if __name__=="__main__":main()
