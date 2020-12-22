# -*- coding: utf-8 -*-
import random
import copy

def selectMt(scrtmp,target,sel):
  if scrtmp.count(1)==sel:
    return True
  selectnum=int((random.random() * 100000) % target)
  scrtmp[selectnum]|=1
  selectMt(scrtmp,target,sel)

def matching():
  score = list(range(0))
  msel = list(range(0))
  fsel = list(range(0))
  total = 0
  
  for i in range(x):
    female = list(range(0))
    for j in range(y):
      female.append(0)
    msel.append(female)
    
  for i in range(y):
    male = list(range(0))
    for j in range(x):
      male.append(0)
    fsel.append(male)
    
  score = copy.deepcopy(msel)

  sumvote=0
  for i in range(x):
    selectMt(msel[i],y,z)
  for i in range(y):
    selectMt(fsel[i],x,z)
  for i in range(x):
    for j in range(y):
      score[i][j]=msel[i][j]+fsel[j][i]
  for i in range(x):
      total+=score[i].count(2)
      sumvote+=sum(score[i])
      # print(score[i])
  # print(sumvote)
  return(total)

x=10
y=10
z=5
party=100
totalmatch=0

for i in range(party):
    totalmatch+=matching()
print(totalmatch/party)