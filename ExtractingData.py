import MergeSort as MS
import InsertionSort as IS
import RearrangingDataFiles as RD
import QuickSort as QS


class ExtractingData:
    def __init__(self,val,index) -> None:
        self.index = index
        self.val = val

        
inversionslist = []
list1 = [] 

file1 = open("source1.txt","r",newline=None)#opening all files 
file2 = open("source2.txt","r",newline=None)
file3 = open("source3.txt","r",newline=None)
file4 = open("source4.txt","r",newline=None)
file5 = open("source5.txt","r",newline=None)
count=0
file1array=[]
file2array=[]
file3array=[]
file4array=[]
file5array=[]
while True:
    data1 = file1.readline() #reading the data through each line until data is present
    data2 = file2.readline()
    data3 = file3.readline()
    data4 = file4.readline()
    data5 = file5.readline()
    if not data1:
        break
    vals1 = data1.strip() #removing the leading and trailing characters in all data sets
    vals2 = data2.strip()
    vals3 = data3.strip()
    vals4 = data4.strip()
    vals5 = data5.strip()
    filedata1 = ExtractingData(int(vals1),count) #extracting data by 
    filedata2 = ExtractingData(int(vals2),count)
    filedata3 = ExtractingData(int(vals3),count)
    filedata4 = ExtractingData(int(vals4),count)
    filedata5 = ExtractingData(int(vals5),count)
    total = int(vals1) + int(vals2) + int(vals3) + int(vals4) + int(vals5) #adding all values element wise for all files
    comination = ExtractingData(total,count) #total is the value for data and count is the index
    count+=1
    
    list1.append(comination) 
    #getting the data of their particular files
    file1array.append(filedata1) 
    file2array.append(filedata2)
    file3array.append(filedata3)
    file4array.append(filedata4)
    file5array.append(filedata5)

#sort combinations
sortData = MS.mergesort(list1,inversionslist,0) 



#rearranging the data in all 5 files according to sorted combined data

Rearrangefile1 = RD.RearrangingDataFiles(file1array, sortData)
Rearrangefile2 = RD.RearrangingDataFiles(file2array, sortData)
Rearrangefile3 = RD.RearrangingDataFiles(file3array, sortData)
Rearrangefile4 = RD.RearrangingDataFiles(file4array, sortData)
Rearrangefile5 = RD.RearrangingDataFiles(file5array, sortData)
inversionslist1 = []
inversionslist2 = []
inversionslist3 = []
inversionslist4 = []
inversionslist5 = []

#applying mergesort on all the 5 rearranged files and getting inversions list(adding all values to get inversions) 
MS.mergesort(Rearrangefile1,inversionslist1,0)
MS.mergesort(Rearrangefile2,inversionslist2,0)
MS.mergesort(Rearrangefile3,inversionslist3,0)
MS.mergesort(Rearrangefile4,inversionslist4,0)
MS.mergesort(Rearrangefile5,inversionslist5,0)
inversionsfile1 = sum(inversionslist1)
inversionsfile2 = sum(inversionslist2)
inversionsfile3 = sum(inversionslist3)
inversionsfile4 = sum(inversionslist4)
inversionsfile5 = sum(inversionslist5)
print("Merge Sort Results: ")
print("File 1 Inversions: ", inversionsfile1, "File 2 Inversions: ", inversionsfile2, "File 3 Inversions: ",inversionsfile3, "File 4 Inversions: ", inversionsfile4, "File 5 Inversions: ", inversionsfile5)

#applying quicksort on all 5 rearranged files and getting the inversions in each of the 5 files
QS.QuickSort(Rearrangefile1)
inversionsfile1 = QS.inversions
QS.inversions = 0
QS.QuickSort(Rearrangefile2)
inversionsfile2 = QS.inversions
QS.inversions = 0
QS.QuickSort(Rearrangefile3)
inversionsfile3 = QS.inversions
QS.inversions = 0
QS.QuickSort(Rearrangefile4)
inversionsfile4 = QS.inversions
QS.inversions= 0
QS.QuickSort(Rearrangefile5)
inversionsfile5 = QS.inversions
QS.inversions = 0

print("Quick Sort Results:")
print("File 1 Inversions: ", inversionsfile1, "File 2 Inversions: ", inversionsfile2, "File 3 Inversions: ",inversionsfile3, "File 4 Inversions: ", inversionsfile4, "File 5 Inversions: ", inversionsfile5)

#applying insertion sort on all 5 rearranged files and getting inversion is each of them
inversionsfile1 = IS.insertionSort(Rearrangefile1)
inversionsfile2 = IS.insertionSort(Rearrangefile2)
inversionsfile3 = IS.insertionSort(Rearrangefile3)
inversionsfile4 = IS.insertionSort(Rearrangefile4)
inversionsfile5 = IS.insertionSort(Rearrangefile5)
print("Insertion Sort Results: ")
print("File 1 Inversions: ", inversionsfile1, "File 2 Inversions: ", inversionsfile2, "File 3 Inversions: ",inversionsfile3, "File 4 Inversions: ", inversionsfile4, "File 5 Inversions: ", inversionsfile5)
print()
#Conclusion
print("In conclusion: Web Search Engine 1 is most efficent compared to the others")



