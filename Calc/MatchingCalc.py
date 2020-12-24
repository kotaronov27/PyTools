# -*- coding: utf-8 -*-
import random
import copy

# 相手を選択する。
# scrtmp:immutable、選択リスト
# target:ターゲット数
# sel:希望順位
# weight:重み
def selectMt(scrtmp,target):
  # sel数まで選んだら終わり
  if scrtmp.count(1)==sel:
    return True
  #0~target-1 までをランダム
  selectnum=int(random.random() * target * weight)
  scrtmp[selectnum]|=1
  # 再帰処理
  selectMt(scrtmp,target)

# マッチングメイン
def matching():
  # 初期化
  score = list(range(0))
  msel = list(range(0))
  fsel = list(range(0))
  total = 0
  
  # 男性の選択表作成
  for i in range(x):
    female = list(range(0))
    for j in range(y):
      female.append(0)
    msel.append(female)
    
  # 女性の選択表作成
  for i in range(y):
    male = list(range(0))
    for j in range(x):
      male.append(0)
    fsel.append(male)
    
  # マッチングテーブル作成
  score = copy.deepcopy(msel)

  sumvote=0
  # 男性側選択
  for i in range(x):
    selectMt(msel[i],y)
  # 女性側選択
  for i in range(y):
    selectMt(fsel[i],x)
  # マッチング結果計算
  for i in range(x):
    for j in range(y):
      score[i][j]=msel[i][j]+fsel[j][i]
  for i in range(x):
      total+=score[i].count(2)
      sumvote+=sum(score[i])
      print(score[i]) # マッチング表確認
  # print(sumvote) # 投票数確認
  return(total)

# ~~以下メイン処理~~
# 男性人数
# 女性人数
# 希望順位
# ウェイト(上位)
# パーティ回数
x=20
y=20
sel=5
weight=0.3
party=1
totalmatch=0.0

if x * weight < sel:
  weight = 1
elif y * weight < sel:
  weight = 1
elif weight > 1:
  weight = 1

for i in range(party):
    totalmatch+=matching()
print(totalmatch/party)