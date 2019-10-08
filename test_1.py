# coding=gbk
# Notice: This is the test file , just for reference.
# 設有用戶A、B,A設置壹個門電路,使用後得到真值表,並用密鑰替換真值表得到新的密文真值表,將密文真值表和B輸入的密鑰對應表發送給B
# A發送加密後的訊息x給B,B使用A發送的對應表找到自己訊息的對應密鑰y,使用密文真值表得到唯壹結果z,將z返回給A
# 以下實現僅壹個門電路的傳輸過程

def gate_example(x,y):
	if(x=='a0' and y=='b0'):
		z='c0'
	if(x=='a1' and y=='b0'):
		z='c0'
	if(x=='a0' and y=='b1'):
		z='c0'
	if(x=='a1' and y=='b1'):
		z='c1'
	return z

tran_A = {"1":"a1","0":"a0"}
tran_B = {"1":"b1","0":"b0"}
tran_C = {"1":"c1","0":"c0"}

list_a = ['a0','a1']
list_b = ['b0','b1']
list_c = ['c0','c1']

plain_A = input("A want to send the plain code is (1/0)：")
cipher_A = tran_A[plain_A]

print("A send the message is "+cipher_A)

plain_B = input("B's plain code is (1/0):")
cipher_B = tran_B[plain_B]

print("B get the cipher is "+cipher_B)

cipher_C = gate_example(cipher_A,cipher_B)

print("B return the cipher is "+cipher_C)
print("A get cipher:"+cipher_C+" and start to tranlate it:")

for x in tran_C:
  if tran_C[x] == cipher_C:
    z = x

print("A get the result from B is:"+z)





