# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:02:06 2018

@author: js_en
"""

""" in this code we will attempt to create a binary tree capable
    of storing objects
"""
#import numpy as np
# Global Var



class Node:
    
        
    def __init__(self):
        self.data = [None]
        self.root = None
        
        self.branch = [None, None]
        
    # recursive check that finds an empty slot for data
    def check(self, pend):
        
        if self.data[0] == None:
            self.data[0] = pend
            print("object allocated = ", pend)
            
        elif self.data[0] != None:
            if pend < self.data[0]:
                if self.branch[0] != None:
                    self.branch[0].check(pend)
                elif self.branch[0] == None:
                    self.build(0)
                    self.branch[0].check(pend)
                    
            if pend > self.data[0]:
                if self.branch[1] != None:
                    self.branch[1].check(pend)
                elif self.branch[1] == None:
                    self.build(1)
                    self.branch[1].check(pend)
                    
            if pend == self.data[0]:
                self.data.append(pend)
                print("object allocated = ", pend)

    # Builds an empty node at location        
    def build(self,num):
        self.branch[num] = Node()
        self.branch[num].root = self

    
            

class Tree:
    
    def __init__(self, pending):
        self.pending = pending
        self.size = len(self.pending)
        self.root = Node()
        
    def build(self):
        for i in range(self.size):
            data = pending[i]
            self.root.check(data)
    
    def order(self):
        
        order = "Not Implemented Yet" 
        
        return order
        
    
    
if __name__=="__main__":
    
    pending = [5, 5, 6, 10, 1, 7, 3, -1, 0]
    tree = Tree(pending)
    tree.build()
    tree.order()