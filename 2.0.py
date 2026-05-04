#hello!と表示する
print('hello!')
#こんにちは。初めましてと表示する。
print('こんにちは。',end='')
print('初めまして。')
#風林火山と表示する。
print('風\n林\n火\n山')

print(' ')

#パターンA：途中に\nを挟む。
print('1行目\n2行目\n3行目')
#パターンB：endに\nを２つ入れてみる。
print('hello',end='\n\n')
print('world')

print()

#こんにちは。はじめまして！を改行を挟んで表示する。
print('こんにちは。')
print()
print('初めまして。')

print()

#
print('お名前は:',end='')
name=input()
print('こんにちは',name,'さん')

name=input('お名前は：')
print('こんにちは',name,'さん',sep='')

name=input('お名前は：')
print('こんにちは'+name+'さん')

print()
print()

#２つの整数値を読み込んで加減乗算を行う。（その１：文字列を読み込んで数値に変換）
a=int(input('整数a：'))
b=int(input('整数b：'))
print('a+bは',a+b,'です。')
print('a-bは',a-b,'です。')
print('a*bは',a*b,'です。')
print('a/bは',a/b,'です。')
print('a//bは',a//b,'です。')
print('a%bは',a%b,'です。')
print('a**bは',a**b,'です。')

print('a+bは'+str(a+b)+'です。')
print('a-bは'+str(a-b)+'です。')
print('a*bは'+str(a*b)+'です。')
print('a/bは'+str(a/b)+'です。')
print('a//bは'+str(a//b)+'です。')
print('a%bは'+str(a%b)+'です。')
print('a**bは'+str(a**b)+'です。')

#２つの文字列の和を表示する。
a11=int(input('整数a：'))
b11=int(input('整数b：'))
print(f'a+bは{a11+b11}です。')
print(f'a-bは{a11-b11}です。')
print(f'a*bは{a11*b11}です。')
print(f'a/bは{a11/b11}です。')
print(f'a//bは{a11//b11}です。')
print(f'a%bは{a11%b11}です。')
print(f'a**bは{a11**b11}です。')

#円周の長さと面積を求める。
r=float(input('半径：'))
print(f'円周の長さは{2*3.14*r}です。')
print(f'円の面積は{3.14*r**2}です。')

#円周の長さと面積を求める。
r=float(input('半径：'))
PI=3.1415926535897933
print(f'円周の長さは{2*PI*r}です。')
print(f'円の面積は{PI*r**2}です。')