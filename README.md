> Simple Algorithms of AI
>
> Content:
>- About the problem
>- English Version (way to solve)
>- Vietnamese Version (way to solve)
# I. About the problem
### 1. Problem 1
![image](https://user-images.githubusercontent.com/58379925/219711391-6c33783f-d12a-4694-a4b9-56a5833b3f04.png)

Install following Algorithms: 
- Heuristic
- A* 
Example: from Arad to Bucharest 

### 2. Problem 2
Find the number of islands using algorithms as follows: 
- BFS (Breadth First Search)
![image](https://user-images.githubusercontent.com/58379925/219710344-148e3383-ef64-4254-b25a-ea3523b46e55.png)
Example:
- Input: Green color: sea , land: white color 
- Output: 5 islands


# II. English Version
## Problem 1:
### 1. Greedy Best First Search (Heuristic) Algorithm
#### 1.1 Algorithm diagram
1. Save the starting point to O
2. If O is empty -> search failed, end search
3. If O is not empty -> take the first point in O and call it rs. Put rs in C
4. If rs is the endpoint -> search is successful, end search
5. Find all subpoints of rs given O in ascending order of h(x) - estimated distance to the destination
6. Go back to step 2 and continue

#### 1.2 Route results from Arad to Bucharest:
![image](https://user-images.githubusercontent.com/58379925/219714181-4a5564ed-b57e-4c93-ae5d-1458fa37334a.png)

### 2. Algorithm A* (A Star)
#### 2.1 Algorithm Diagram
1. Save the starting point to O
2. If O is empty -> search failed, end search
3. If O is not empty -> take the first point in O and call it rs. Put rs in C
4. If rs == endpoint successful search, end search
5. Find all subpoints of rs given in O in ascending order for the formula g(x) + h(x)
6. Go back to step 2 and continue
>in which:
>- g(x) is the distance from the starting point to x
>- h(x) is the estimated distance from x to the destination

#### 2.2 Route from Arad to Bucharest:
![image](https://user-images.githubusercontent.com/58379925/219714333-67a1e267-069e-46f3-b5da-243a29472a49.png)

## Problem 2:
### 1.BFS Algorithm – Breadth First Search
#### 1.1 Algorithm diagram
1. Make 2 loops to run in rows and columns
2. Check position [row][column], if equal to 1 and that position is not checked (False) -> count += 1 and save that position to queue, assign True to that position that has been checked
3. Get the first position saved in the queue -> Check around that position, if == 1 and haven't checked (False), then assign True to that position
4. Repeat step 2


# III. VietNamese Version
## Vấn đề 1:
### 1. Giải thuật Greedy Best First Search (Heuristic)	
#### 1.1 Sơ đồ giải thuật
1. Lưu điểm xuất phát vào O
2. Nếu O rỗng -> tìm kiếm thất bại, kết thúc tìm kiếm
3. Nếu O không rỗng -> lấy điểm đầu trong O và gọi nó là rs. Cho rs vào C
4. Nếu rs là điểm cuối -> tìm kiếm thành công, kết thúc tìm kiếm
5. Tìm tất cả cá điểm con của rs cho vào O theo thứ tự tăng dần về h(x) - khoảng cách ước lượng đến đích 
6. Trở lại về bước 2 và thực hiện tiếp

#### 1.2 Kết quả đường đi từ Arad tới Bucharest:
![image](https://user-images.githubusercontent.com/58379925/219714181-4a5564ed-b57e-4c93-ae5d-1458fa37334a.png)

### 2. Giải thuật A* (A Star)
#### 2.1 Sơ đồ giải thuật
1. Lưu điểm xuất phát vào O
2. Nếu O rỗng -> tìm kiếm thất bại, kết thúc tìm kiếm
3. Nếu O không rỗng -> lấy điểm đầu trong O và gọi nó là rs. Cho rs vào C
4. Nếu rs == điểm cuối  tìm kiếm thành công, kết thúc tìm kiếm
5. Tìm tất cả cá điểm con của rs cho vào O theo thứ tự tăng dần đối với công thức g(x) + h(x)
6. Trở lại về bước 2 và thực hiện tiếp
>trong đó:
>- g(x) là khoảng cách từ điểm xuất phát đến x
>- h(x) là khoảng cách ước lượng từ x đến đích

#### 2.2 Đường đi từ Arad tới Bucharest:
![image](https://user-images.githubusercontent.com/58379925/219714333-67a1e267-069e-46f3-b5da-243a29472a49.png)

## Vấn đề 2:
### 1.Giải thuật BFS – Breadth First Search	
#### 1.1 Sơ đồ giải thuật 
1. Thực hiện 2 vòng lặp để chạy theo hàng và cột
2. Kiểm tra vị trí [hàng][cột], nếu bằng 1 và vị trí đó chưa check (False) -> count += 1 và lưu vị trí đó vào queue, gán True cho vị trí đó đã check qua
3. Lấy vị trí đầu đã lưu trong queue -> Kiểm tra xung quanh vị trí đó, nếu == 1 và chưa check qua (False) thì gán True vào vị trí đó
4. Thực hiện lại bước 2

#### 1.2 Kết quả
![image](https://user-images.githubusercontent.com/58379925/219713880-c155db59-936c-41e1-a0bd-4a833b8de1aa.png)

> This Assignment by Lecture: Bui Thanh Hung 
> 
> Director of Data Analytics & Artificial Intelligence Laboratory - DAAI Lab  Director of Artificial Intelligence & Information System Programme  
> 
> Institute of Engineering -Technology 
> 
> Thu Dau Mot University 
> 
> Email: tg_buithanhhung@tdtu.edu.vn 
> 
> Website: https://sites.google.com/site/hungthanhbui1980 
> 
> I'm finished At Ton Duc Thang university - Year: 2021
