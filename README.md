# Ex1 - Offline Elevator Algorithm

 <code><img height="300" width="600" src="https://38i4h31480aw2fd03t4av02o-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/Smart-Elevators.jpg"/></code>

#### @ Or Yitshak & Haim Goldfisher

---------

## 1. Introduction and resources:
We want to design an efficient algorithm for a smart elevator. It should be noted that in some articles there is a lot of reference to the engineering or economic aspect of elevators. We focused solely on the algorithms that the elevators implement. Sources we used:

a) https://www.youtube.com/watch?v=xOayymoIl8U - A nice video that focuses on the logic behind elevators. It presents an opinion that systematic walking along the floor closest to the elevator is a problematic principle. When there is a person on a remote floor, the elevator may not reach him at all. Another thing reviewed there, is the ability of the elevators to "communicate" with each other using an efficient algorithm. That is, when we maintain the activity of the elevators, it is more convenient for us to instruct the other elevators how to operate. Also, the video indicates that it is necessary to reach a minimum waiting time even inside the elevator and not just at the waiting for it. Another interesting point that emerges from the video is that the nature of the structure needs to be understood in depth. For example, there is a difference between a number of adjacent elevators and a situation where each elevator is at a great distance from each other (e.g. in a wide building where each elevator is at a different edge of the building).

b) https://peters-research.com/index.php/papers/etd-algorithm-with-destination-dispatch-and-booster-options/ - ETD Algorithm - Estimated Time to Destination for elevators. Here is an efficient algorithm that can be applied for an elevator system. We learned a lot from him in order to design our online algorithm, and it is actually a cornerstone of the algorithm we designed.

c) https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.diva-portal.org/smash/get/diva2:668671/fulltext01.pdf&ved=2ahUKEwj3mYyis9PzAhXPhf0HHRXFCLcQFnoECBYQAQ&usg=AOvVaw3mb79K_dvlH9TNNYY9g93- - An article on strategies in designing elevator algorithms, both technically and algorithmically. There is a lot of reference in the technical aspect of elevators, which is less relevant to us.

d) https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/ - A thought-provoking and very interesting but less practical article on lifts and choosing a suitable algorithm for them. The article for example takes into account the question of whether it is better to wait outside the elevator or inside the elevator. A point is less critical for us since we have no meaning for waiting outside or inside an elevator.

---------

## 2. The differences between 'Offline' and 'Online' algorithms:
The main difference between the above two modes is the ability of the elevator to prepare for the sequence of actions. That is, when it comes to Online mode, a number of variables must be taken into account. There is a higher probability of a call, so the elevator will be available most of the time to this floor.
In Offline mode, on the other hand, we want to design the shortest elevator route that "covers" as many people as possible, so that the waiting time for an elevator is minimal. We can use all the elevators we have for this purpose, without considering additional considerations. Another thing that is fascinating about the offline algorithm is the ability to be a fortune teller. That is, we can assign an elevator to call even before it has received one! In addition, the elevator will be able to ignore calls in order to wait for a more strategic call. All this is possible for us due to the fact that we get the list of calls in advance, as well as the time of the calls.

--------- 

## 3. The Algorithm:



---------

## 4. UML Diagram:


<code><img height="450" width="300" src="https://github.com/haimgoldfisher/OOP_ex1/blob/master/UML_img.png?raw=true"/></code>

---------

## 5. Results:

|       | Building | Call | Total Waiting Time | Average Waiting Time Per Call | UnCompleted Calls | Certificate |
| ----- | ---------| -----| ------------------ | ----------------------------- | ----------------- | ----------- |
| 1     | B1       | a_1  | 11292              | 112.92                        | 0                 | -273971877  |
| 2     | B2       | a_2  | 4649               | 46.49                         | 0                 | -237904543  |
| 3     | B3       | a_3  | 2994               | 29.94                         | 0                 | -44160852   |
| 4     | B3       | b_3  | 547470.620351999   | 547.470620351999              | 174               | -2001207391 |
| 5     | B3       | c_3  | 554600.120260004   | 554.600120260004              | 132               | -1969794310 |
| 6     | B3       | d_3  | 549593.916998004   | 549.593916998004              | 153               | -1979939333 |
| 7     | B4       | a_4  | 2063               | 20.63                         | 0                 | -54793609   |
| 8     | B4       | b_4  | 210331.646815999   | 210.331646815999              | 17                | -744519961  |
| 9     | B4       | c_4  | 213750.38061       | 213.750380609999              | 2                 | -747533748  |
| 10    | B4       | d_4  | 205285.061562      | 205.285061561999              | 7                 | -762051044  |
| 11    | B5       | a_5  | 1714               | 17.14                         | 0                 | -69599288   |
| 12    | B5       | b_5  | 50362              | 50.362                        | 0                 | -219374659  |
| 13    | B5       | c_5  | 47999              | 47.999                        | 0                 | -250958602  |
| 14    | B5       | d_5  | 49564.437366       | 49.564437366                  | 1                 | -223098839  |

---------

## 6. Languages and Tools:

  <div align="center">
  
  <code><img height="40" src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png"/></code>
  <code><img height="40" src="https://pbs.twimg.com/profile_images/1206603239791218688/0AwZ0m6W_400x400.jpg"/></code>
  <code><img height="40" src="https://www.clipartmax.com/png/middle/136-1368231_farmers-markets-json-icon-transparent.png"/></code>
  <code><img height="40" width="80" src="https://user-images.githubusercontent.com/74299934/124384183-c15bd600-dcd8-11eb-8350-d1980f87b8c8.png"/></code>
  
