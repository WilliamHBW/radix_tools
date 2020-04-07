import random

class Radix(object):
    def gen_randseq(self,b_len,radix):
        stra = ""
        for i in range(b_len):
            ch = chr(random.randrange(ord('0'),ord('1')+1))
            stra += ch
        if(radix=='b'):
            return stra
        elif(radix=='h'):
            return self.b2h(stra)

    def gen_randfile(self,fileaddr,b_len,row_num,radix):
        f = open(fileaddr,mode="w")
        for i in range(row_num):
            test_a = self.gen_randseq(b_len,radix)
            f.write("%s"%test_a)
            f.write("\n")
        f.close()
        print("random",radix,"file has been generated at",fileaddr)
    
    def signed_b2d(self,b_seq):
        d = 0
        if(b_seq[0]=='1'):
            for i in range(len(b_seq)-1):
                d += int(b_seq[i+1])*(2**(len(b_seq)-2-i))
            d += -1*(2**(len(b_seq)-1))
        else:
            for i in range(len(b_seq)):
                d += int(b_seq[i])*(2**(len(b_seq)-1-i))
        return d

    def b2h(self,b_seq):
        h = []
        for item in [b_seq[i:i+4] for i in range(0,len(b_seq),4)]:
            if(len(item)==4):
                h_ = int(item[-1])*1+int(item[-2])*2+int(item[-3])*4+int(item[-4])*8
            elif(len(item)==3):
                h_ = int(item[-1])*1+int(item[-2])*2+int(item[-3])*4
            elif(len(item)==2):
                h_ = int(item[-1])*1+int(item[-2])*2
            else:
                h_ = int(item[-1])*1
            if(h_>9):
                h_ = chr((h_-10)+97)
            else:
                h_ = str(h_)
            h.append(h_)
        h.reverse()
        return "".join(h)


