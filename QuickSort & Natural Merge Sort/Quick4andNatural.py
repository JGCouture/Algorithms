# Name: Quicksort and Natural Merge Sort. 
# Author: Yang(Albert) Zhang
# Purpose: compare Quick sort of 5 versions with Natural Merge Sort
# Notes:
    # 1: All sorting algorithms are achieved in an iterative way
    # 2: A linked structure is created for Natural Merge Sort so that the space complexity is O(1)

import os
import csv
import random
from collections import Counter

from datetime import datetime
from linkedList import linkedList
from linkedList import Node
from linkedList import Segment

class Quick4andNatural:

    # General quick sort
    def quickSort(self, arr):

        #Comparison and Exchanges Initilization
        com = 0
        exc = 0

        if len(arr) < 2:
            return [arr, com, exc]

        # stack to pop the indices of a subset every time
        stack = []
        stack.append(len(arr)-1)
        stack.append(0)

        while stack:
            
            l= stack.pop()
            r = stack.pop()

            # Partition
            [index, com, exc] = self.partition(arr, l, r, com, exc)

            if l < index-1:

                # Left subset
                stack.append(index -1)
                stack.append(l)

            if r > index+1:

                # Right subset
                stack.append(r)
                stack.append(index+1)

        #[the sorted list, # of comparisons, # of exchanges]        
        return [arr, com, exc]

    def partition(self, arr, start, end, com, exc):

        # Select the first item of the partition as the pivot
        pivot = arr[start]
        
        while start < end:
            
            while start < end and arr[end] >= pivot:
                
                end -=1
                com += 1
                
            arr[start] = arr[end]
            exc += 1
            
            while start < end and arr[start] <= pivot:
                
                start += 1
                com += 1
                
            arr[end] = arr[start]
            exc += 1

        arr[end] = pivot
        exc += 1

        return [start, com, exc]

    # Insertion sort for partition of size 100 or less 
    def quickSortPartition100(self, arr):
        
        #Comparison and Exchanges Initilization
        com = 0
        exc = 0
            
        if len(arr) < 2:
            return [arr, com, exc]

        stack = []

        stack.append(len(arr)-1)
        stack.append(0)

        l= stack.pop()
        r = stack.pop()
        [index, com, exc] = self.partition(arr, l, r, com, exc)
        
        if l < index-1:
            stack.append(index -1)
            stack.append(l)

        if r > index+1:
            stack.append(r)
            stack.append(index+1)

        while stack:

            l= stack.pop()
            r = stack.pop()
            
            # Check if partition of size 100 or less
            pSize = r - l
            

            if pSize <= 100:

                [com, exc] = self.insertionSort(arr, l, r, com, exc)

            else:
                [index, com, exc] = self.partition(arr, l, r, com, exc)
                if l < index-1:
                    stack.append(index -1)
                    stack.append(l)
                if r > index+1:
                    stack.append(r)
                    stack.append(index+1)

                    
        return [arr, com, exc]
    
    # Insertion sort for partition of size 50 or less 
    def quickSortPartition50(self, arr):

        #Comparison and Exchanges Initilization
        com = 0
        exc = 0
            
        if len(arr) < 2:
            return [arr, com, exc]

        stack = []

        stack.append(len(arr)-1)
        stack.append(0)

        l= stack.pop()
        r = stack.pop()
        [index, com, exc] = self.partition(arr, l, r, com, exc)
        
        if l < index-1:
            stack.append(index -1)
            stack.append(l)

        if r > index+1:
            stack.append(r)
            stack.append(index+1)

        while stack:

            l= stack.pop()
            r = stack.pop()
            
            # Check if partition of size 50 or less
            pSize = r - l
            

            if pSize <= 50:

                [com, exc] = self.insertionSort(arr, l, r, com, exc)

            else:
                [index, com, exc] = self.partition(arr, l, r, com, exc)
                if l < index-1:
                    stack.append(index -1)
                    stack.append(l)
                if r > index+1:
                    stack.append(r)
                    stack.append(index+1)

                    
        return [arr, com, exc]


    # Insertion sort
    def insertionSort(self, arr, l, r, com, exc):

        if (n := len(arr)) <= 1:return
        
        for i in range(l, r+1):
             
            key = arr[i]

            j = i-1

            # Swap 
            while j >=0 and key < arr[j] :
                
                    arr[j+1] = arr[j]
                    j -= 1
                    com += 1
                    exc += 1
                    
            arr[j+1] = key
            com += 1
            
        return [com, exc]

    # Quick sort with median-of-three as the pivot
    def medianOf3Sort(self, arr, left=0, right=0):

        #Comparison and Exchanges Initilization
        com = 0
        exc = 0
    
        if len(arr) < 2:return [arr, com, exc]

        stack = []
        stack.append(len(arr)-1)
        stack.append(0)

        while stack:
            
            l= stack.pop()
            r = stack.pop()

            # Median-of-three as the pivot
            [index, com, exc] = self.medianOf3partition(arr, l, r, com, exc)

            if l < index-1:
                
                stack.append(index -1)
                stack.append(l)

            if r > index+1:
                
                stack.append(r)
                stack.append(index+1)
                
        return [arr, com, exc]


    def medianOf3partition(self, nums, left, right, com, exc):

        # Find the median of three
        [med, com, exc] = self.median_three(nums, left, (left + right) // 2, right, com, exc)
       
        nums[left], nums[med] = nums[med], nums[left]
        
        i, j = left, right
        
        while i < j:
            
            while i < j and nums[j] >= nums[left]:
                
                j -= 1
                com += 1
                
            while i < j and nums[i] <= nums[left]:
                
                i += 1
                com += 1
          
            nums[i], nums[j] = nums[j], nums[i]
            exc += 1
       
        nums[i], nums[left] = nums[left], nums[i]
        exc += 1
        
        return [i, com, exc]

    def median_three(self, nums, left, mid, right, com, exc):
      
        # 0 ^ 0 = 1 ^ 1 = 0, 0 ^ 1 = 1 ^ 0 = 1
        if (nums[left] < nums[mid]) ^ (nums[left] < nums[right]):

            com += 2
            
            return [left, com, exc]
        
        elif (nums[mid] < nums[left]) ^ (nums[mid] < nums[right]):

            com += 2
            
            return [mid, com, exc]
        
        return [right, com, exc]

    # Natural merge sort
    def naturalMergeSort(self, head):

        #Comparison and Exchanges Initilization
        com = 0
        exc = 0
        
        if head is None:

            return [None, com, exc]
        
        numMerge = 2
        
        while numMerge > 1:
            
            nextHead = head
            lastTail = None
            head = None
            numMerge = 0
            
            while nextHead is not None:

                # Get two adjacent segments
                [seg1, com, exc] = self.getSortedSegment(nextHead, com, exc)
                [seg2, com, exc] = self.getSortedSegment(seg1.tail.next, com, exc)
                
                # record head for next merging
                nextHead = None if seg2 is None else seg2.tail.next
                [merged, com, exc] = self.merge(seg1, seg2, com, exc)
                
                # connect last merged part to current merged part
                if lastTail is not None:
                    
                    lastTail.next = merged.head
                    
                lastTail = merged.tail
                
                if head is None:
                    
                    head = merged.head
                    
                numMerge += 1
                
        return [head, com, exc]

    def getSortedSegment(self, head, com, exc):

        if head is None:return [None, com, exc]

        tail = head
        size = 1

        # Get the sorted degment and its length, head, and tail node.
        while tail.next is not None and tail.next.data >= tail.data:

            tail = tail.next
            size += 1
            com += 1
            
        return [Segment(size, head, tail), com, exc]

    def merge(self, seg1, seg2, com, exc):
   
        if seg2 is None:
            return [seg1, com, exc]
        
        if seg1 is None:
            return [seg2, com, exc]

        dummy = Node()
        node1, node2, node = seg1.head, seg2.head, dummy
        size1, size2 = seg1.size, seg2.size
        
        while size1 > 0 and size2 > 0:
            
            if node1.data <= node2.data:
                
                node.next = node1
                node1 = node1.next
                size1 -= 1

                exc += 1
                
            else:
                
                node.next = node2
                node2 = node2.next
                size2 -= 1

                exc += 1
                
            node = node.next

            com += 1
            
        tail = node
        
        if size1 > 0:
            
            node.next = node1
            tail = seg1.tail
            
        elif size2 > 0:
            
            node.next = node2
            tail = seg2.tail
            
        tail.next = None
        
        return [Segment(seg1.size + seg2.size, dummy.next, tail), com, exc]

    def readFile(self, fileName, path):

        s = []
        lines = open((path +'/'+fileName), 'r').readlines()
        for line in lines:
            if line.strip():
                temp = line.replace("\n", "")
                temp = temp.split(" ")
                
                for i in temp:
                    if i.isdigit():
                        s.append(int(i))
        return s
    
    def outCSV(self, result):
        name = input("Please input a valid file name (.csv): ")
        with open(name, 'w', newline='') as file:
            write = csv.writer(file, delimiter=",")
            for i in result:
                line = [i[0], i[1][0], i[1][1], i[1][2], i[1][3]]
                write.writerow(line)

    def outputFile(self, list50, fileName, sortName):
        print("\ninput fils is {} and sort is {}\n".format(fileName, sortName))
        outName = input("Please type a valid txt file name (.txt) for output: ")
        out = open(outName, "w")
        for i in list50:
            out.write(str(i)+'\n')

    def generateNumbers(self):

        print("Input txt file name must include ran, res, or rev such as ran50.txt")
        outName = input("Please type a valid txt file name (.txt): ")

        if 'ran' not in outName or 'res' not in outName or 'rev' not in outName:
            print("You input name is not valid")
            
        else:

            ran = input("Please type the range of numbers (start, end): ")
            num = input("Please type how may numbers to create: ")

            out = open(outName, "w")

            t = ran.split(",")
            
            array = random.sample(range(int(t[0]), int(t[-1])), int(num))

            dulOrNot = input("if duplicate requested, type 1 for yes, 2 for no: ")

            if dulOrNot == '1':
                 
                temp = random.sample(range(15, 20), 1)

                dupl = len(array)*temp[0]//100

                m = array[:dupl]
                n = array[:len(array)-dupl]

                p = m + n
                random.shuffle(p)


            if dulOrNot == '2':

                p = array
            
            if 'ran' in outName:

                for i in p:  
                    out.write(str(i) + "\n")

            if 'rev' in outName:

                p1 = sorted(p, reverse=True)

                for j in p1:  
                    out.write(str(j) + "\n")

            if 'asc' in outName:

                p2 = sorted(p)

                for k in p2:  
                    out.write(str(k) + "\n")
    
            
if __name__ == '__main__':

    test = Quick4andNatural()

    # Option to create files first or directly read existed files

    option = input("please type 1 to create or 2 to read files: ")

    if option == '2':
        
        #Read a folder contains all input files
        path = input("please input a folder path: ")
        
        # /Users/albert/Documents/Lab 4 Input Files
        files = os.listdir(path)
        fileList=[]
        
        for file in files:
            if not os.path.isdir(file):
                
                f = open(path+"/"+file, encoding="ISO-8859-1")
                iter_f = iter(f)
                string = ""
                for line in iter_f:
                    string = string +line
                if file[-1: -5:-1] == "txt.":
                    fileList.append(file)

        # Read each file and output
        fileSize = []
        li = []
        
        for fileName in fileList:
            
            s = test.readFile(fileName, path)

            fileSize.append([fileName,len(s)])
            li.append([fileName,s])
        print("\n--------------------Successfully Read All Files--------------------\n")
        # Check if the duplicates to <1%
        for j in li:

            counter_object = Counter(j[1])
            keys = counter_object.keys()
            per = (len(j[1]) - len(keys))/len(j[1])
            print('File {} has duplicate values (%): {}'.format(j[0], per))

    
        # Sort the file names based on the size first then name
        fileSize = sorted(fileSize, key = lambda x: (x[1], x[0]))
        print(fileSize)

        # Format result = [['fileName',['Sort Algorithm', # of comparison, # of exchanges, time span in sec]], ...]
        result = []
        
        date_format_str = '%Y-%m-%d %H:%M:%S.%f'

        # count # of runs
        count = 0
        
        # Run diff sort algorithms
        for i in li:

            # ----------General quick sort
            temp1 = i[1][:]
            now1 =datetime.now().strftime(date_format_str)
            re1 = test.quickSort(temp1)
            now2 = datetime.now().strftime(date_format_str)

            start1 = datetime.strptime(now1, date_format_str)
            end1 =   datetime.strptime(now2, date_format_str)
            diff1 = end1 - start1

            sec1 = diff1.total_seconds()

            # Check if correctlly sorted
            if re1[0] == sorted(i[1]):
                count += 1
                print("\n----------Correctly sorted with General Quick Sort ({})----------\n".format(count))

            # outpuit the size of 50
            if len(re1[0]) == 50:
                test.outputFile(re1[0],i[0],'GQS')

                
            result.append([i[0], ["QS", re1[1], re1[2], sec1]])


            # ----------Quick sort and insertion sort for partition size 50 or less
            temp2 = i[1][:]
            now3 =datetime.now().strftime(date_format_str)
            re2 = test.quickSortPartition50(temp2)
            now4 = datetime.now().strftime(date_format_str)

            start2 = datetime.strptime(now3, date_format_str)
            end2 =   datetime.strptime(now4, date_format_str)
            diff2 = end2 - start2

            sec2 = diff2.total_seconds()

            # Check if correctlly sorted
            if re2[0] == sorted(i[1]):
                count += 1
                print("\n----------Correctly sorted in Quick Sort and Insertition Sort with Size 50 or less ({})----------\n".format(count))

            # outpuit the size of 50
            if len(re2[0]) == 50:
                test.outputFile(re2[0],i[0],'GQSI50')
                
            result.append([i[0], ['QSI50', re2[1], re2[2], sec2]])


            # ----------Quick sort and insertion sort for partition size 100 or less
            temp3 = i[1][:]
            now5 =datetime.now().strftime(date_format_str)
            re3 = test.quickSortPartition100(temp3)
            now6 =datetime.now().strftime(date_format_str)

            start3 = datetime.strptime(now5, date_format_str)
            end3 =   datetime.strptime(now6, date_format_str)
            diff3 = end3 - start3

            sec3 = diff3.total_seconds()

            # Check if correctlly sorted
            if re3[0] == sorted(i[1]):
                count += 1
                print("\n----------Correctly sorted in Quick Sort and Insertition Sort with Size 100 or less ({})----------\n".format(count))

            # outpuit the size of 50
            if len(re3[0]) == 50:
                test.outputFile(re3[0],i[0],'GQSI100')
                
            result.append([i[0], ['QSI100', re3[1], re3[2], sec3]])


            # ----------Quick sort with median-of-three as the pivot
            temp4 = i[1][:]
            now7 =datetime.now().strftime(date_format_str)
            re4 = test.medianOf3Sort(temp4)
            now8 =datetime.now().strftime(date_format_str)

            start4 = datetime.strptime(now7, date_format_str)
            end4 =   datetime.strptime(now8, date_format_str)
            diff4 = end4 - start4

            sec4 = diff4.total_seconds()

            # Check if correctlly sorted
            if re4[0] == sorted(i[1]):
                count += 1
                print("\n----------Correctly sorted in Quick Sort Median-Of-Three as the Pivot ({})----------\n".format(count))

            # outpuit the size of 50
            if len(re4[0]) == 50:
                test.outputFile(re4[0],i[0],'GQSIM3')
                
            result.append([i[0], ['QSIM3', re4[1], re4[2], sec4]])

            # ----------Natural merge sort
            temp5 = i[1][:]
            he = linkedList()
            he.head = Node(temp5[0])
            temp = he.head

            for j in temp5[1:]:

                temp.next = Node(j)
                temp = temp.next

            now9 =datetime.now().strftime(date_format_str)
            re5 = test.naturalMergeSort(he.head)
            now10 =datetime.now().strftime(date_format_str)

            start5 = datetime.strptime(now9, date_format_str)
            end5 =   datetime.strptime(now10, date_format_str)
            diff5 = end5 - start5

            sec5 = diff5.total_seconds()

            t = linkedList(re5[0])
            k = t.toArray()

            # Check if correctlly sorted
            if k == sorted(i[1]):
                count += 1
                print("\n----------Correctly sorted in Natural Merge Sort ({})----------\n".format(count))

            # outpuit the size of 50
            if len(re1[0]) == 50:
                test.outputFile(k,i[0],'NMS')
                
            result.append([i[0], ['NMS', re5[1], re5[2], sec5]])
            
        print(result)
        # Transfer the result to CSV format
        test.outCSV(result)


    if option == "1":
        test.generateNumbers()
        

   
    
            

                
            


                
                

                
                

            
            

        
            



        

