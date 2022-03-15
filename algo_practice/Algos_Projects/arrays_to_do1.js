
var arr1 = [1,3,5,7,9];
var arr2 = [1,2,3,4,5,6,7,8,9];
var arr3 = [1,5,8,3,13,56,3,35];



// Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.
// function push_front(arr, val){
//     var temp1 = arr[0], temp2 = arr[1];
//     for(var i = 0; i<arr.length && temp1 != undefined; i++){
//         arr[i+1] = temp1
//         temp1 = temp2 
//         temp2 = arr[i+2]
//     }
//     arr[0] = val;
//     return arr
// }

// console.log(push_front(arr1,3))
// console.log(push_front(arr2,3))
// console.log(push_front(arr3,3))

// Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop()
// function pop_front(arr){
//     var return_val = arr[0];
        
//     for(var i = 1; i<arr.length; i++){
//         arr[i-1]= arr[i]
//     }
//     arr.pop()
//     console.group(arr)
//     return return_val;
// }
// console.log(pop_front(arr1));
// console.log(pop_front(arr2));
// console.log(pop_front(arr3));

// Given an array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods.
// Split the array into two arrays by appending the values after the given index into a new array. 
// Append the value to orginial array
// Append the second array to our inifial array. 
// function insert_val_at_indext(arr, dex, val){
//     arr1 = [];
//     for(var i = dex-1; i<arr.length; i++){
//         arr1.push(arr[i])
//     }
//     // console.log(arr1)
//     for(var i = 0; i<dex; i++){
//         arr.pop()
//     }
//     // console.log(arr)
//     arr.push(val)
//     for(var i = 0; i<arr1.length; i++){
//         arr.push(arr1[i])
//     }
//     return arr
// }
// insert_val_at_indext(arr1, 3,99)
// insert_val_at_indext(arr2, 4,10001)
// insert_val_at_indext(arr3, 2,-55)

// Given an array and an index into array, remove and return the array value at that index. Do this without using built-in array methods except pop(). Think of popFront(arr) as equivalent to removeAt(arr,0).
// Return value of array index
// Starting at the index position, iterate through the array and shift values down one place
// Pop the last index of our array

// Swap positions of successive pairs of values of given array. If length is odd, do not change the final element. For [1,2,3,4], return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42]. As with all array challenges, do this without using any built-in array methods
// Iterate through list by 2
// assign i index to variable
// i index = i+1 index
// i+1 dex = variable
function swap_pairs(arr){
    for(var i = 0; i<arr.length-1; i=i+2){
        var temp1 = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp1;
        
    }
    console.log(arr)
}
swap_pairs(arr1)
swap_pairs(arr2)
swap_pairs(arr3)
// Sara is looking to hire an awesome web developer and has received applications from various sources. Her assistant alphabetized them but noticed some duplicates. Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. As with all these array challenges, do this without using any built-in array methods.
// Iterate through list
//