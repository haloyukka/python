# #command = "0x00000000 0x00000000 0x00000000 0x00000000 0x00000001 0x00000001 0x00000001 0x00000001"
# # CommandListの読み込み : .cl(string)
# f = open('sample.cl', 'rt')
# command = f.read()
# hex = command.split(' ')
# #hex = command.split('\n')
# print (hex)
#
# # CommandList書き出し : .txt(string)
# fout = open('sample.txt', 'w')
# for line in hex:
#     fout.write(str(line) + "\n")
# fout.close

#16進の値が書かれたテキストファイル -> バイナリファイルへ変換
import re
with open('sample.cl', 'r') as fin:
  s = fin.read()
  s = re.sub(r'[\r\n\t ]|0x', '', s)
  bins = [int(a+b,16) for a, b in zip(s[::2], s[1::2])]
  with open('test.bin', 'wb') as fout:
     fout.write(bytearray(bins))