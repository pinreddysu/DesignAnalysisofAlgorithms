# DesignAnalysisofAlgorithms



### This project is designed to solve a real-life problem of finding the best search engine. In this project, we need to find the best option among the five search engines based on the ranking given by each of them to 10000 web pages.

### We have found a practical way to solve this issue by using different sorting algorithms: Merge Sort, Quick Sort and Insertion Sort to compare the 5 search engines and find the optimum one. The reason why we chose these sorting algorithms is because of the time complexity being O(nlogn) for Merge Sort, and Quick Sort. We chose Insertion sort to check whether the Merge Sort and Quick Sort are giving same sort of inversions compared to insertion sort due to the complexity of algorithms of Merge and Quick sort. We would be calculating the combined rank for each of the web page by all 5 sources (adding all 10000 ranks elements wise). Next step, would be sorting the combined data (in ascending order).

### With the help of combined data, we would be rearranging the data in each of the 5 source files according to same index positions. After that, we would be applying different sorting algorithms on all of the 5 rearranged file arrays to calculate the inversions in each of the files. The file having least inversions would be considered as the best search engine.
