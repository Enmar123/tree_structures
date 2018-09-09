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
        self.data = None
        self.root = None
        
        self.branch = [None, None]
        
    #recursive check function that finds an empty slot for data
    def check(self, pend):
        self.pend = pend
        
        if self.data == None:
            self.data = pend
            print("object allocated = ", self.pend)
        elif self.data != None:
            if pend < self.data:
                self.build(0)
                self.branch[0].check(pend)
            if pend > self.data:
                self.build(1)
                self.branch[1].check(pend)

            
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
    
    pending = [5, 6, 10, 1, 7, 3]
    tree = Tree(pending)
    tree.build()
    tree.order()