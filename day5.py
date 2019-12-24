# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:15:44 2019

@author: adam.trexler
"""

def main():
    with open("./data/day5.txt", "r") as f:
        data = f.read()         
        data = data.split(",")
    
    ix = 0 
    def helper(data,howmany,ix,modes):
        pos = {}
        for x in range(howmany):
            x += 1
            pos[x] = int(data[int(data[ix+x])]) if modes[x] == '0' else int(data[ix+x])
        return pos
        
    while ix < len(data):
        opcode = str(data[ix]).zfill(5) 
        instruction = opcode[-2:] #get opcode last two digits
        modes = {1:opcode[-3],
                 2:opcode[-4],
                 3:opcode[-5]}
        
        if instruction == "01":
            pos = helper(data,2,ix,modes)
            output = int(pos[1]) + int(pos[2])
            data[int(data[ix+3])] = output
            step = 4
        elif instruction == "02":
            pos = helper(data,2,ix,modes)
            output = int(pos[1]) * int(pos[2])
            data[int(data[ix+3])] = output
            step = 4
        elif instruction == "03":
            # input instruction
            pos = helper(data,1,ix,modes)
            data[int(data[ix+1])] = 1
            step = 2
        elif instruction == "04":
            # output instruction
            pos = helper(data,1,ix,modes)
            print(ix,":",pos[1])
            step = 2
        elif instruction == "99":
            print("end found")
            break
        else:
            print("invalid opcode {x}".format(x=instruction))
        ix += step
            
       
if __name__ == '__main__':
    main()