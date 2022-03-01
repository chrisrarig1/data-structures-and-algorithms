# Insertion Sort

## Overview

- Given the pseudocode below we will be looking through how this code works from iteration to iteration with the given list

- Pseudocode:

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

- Input List: `[8,4,23,42,16,15]`

## Iterations

- *First*:
  ![It1](code_challenges/insertion_sort/it1.png)
  - 8 is the first number we have seen so we will assume it is in the correct place
- *Second*:
  ![It2](code_challenges/insertion_sort/it2.png)
  - In this iteration we will compare the first index (8) and the second (4). Since (4) is less than (8) we will shift the (4) into the first index position
- *Third*:
  ![It3](code_challenges/insertion_sort/it3.png)
  - In this iteration we will compare index value (8) and (23). Since (8) is not greater than (23) the number (23) will stay in place
- *Fourth*:
  ![It4](code_challenges/insertion_sort/it4.png)
  - In this iteration we will compare index value (23) and (42). Since (23) is not greater than (42) the number (42) will stay in place
- *Fifth*:
  ![It5](code_challenges/insertion_sort/it5.png)
  - In this iteration we will compare index value (42) and (16). Since (42) is greater than (16) the number (16) will be placed in (42)'s index spot and (42) will shift forward. Next (16) will be compared to (23). Since (23) is greater than (16) the number (16) will be placed in (23)'s index spot and (23) will be shifted forward. Then (16) is compared to (8) and since (8) is not greater than (16) both values will remain in place.
- *Sixth*:
  ![It6](code_challenges/insertion_sort/it6.png)
  - In this iteration we will compare index value (42) and (15). Since (42) is greater than (15) the number (15) will be placed in (42)'s index spot and (42) will shift forward. Next (15) will be compared to (23). Since (23) is greater than (15) the number (15) will be placed in (23)'s index spot and (23) will be shifted forward.Next (15) will be compared to (16). Since (16) is greater than (15) the number (15) will be placed in (16)'s index spot and (16) will be shifted forward. Then (15) is compared to (8) and since (8) is not greater than (15) both values will remain in place.

## Output

- `[4,8,15,16,23,42]`

## Big 'O'

- *Time*: O(N)
- *Space*: O(1)

## Summary

- The Insertion Sort method allows an array to be reordered into numerical order by value by comparing each previous index than the current index. If the current index is greater than the previous then the iteration is complete