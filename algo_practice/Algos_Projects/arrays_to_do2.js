
var arr1 = [1,3,5,7,9];
var arr2 = [1,2,3,4,5,6,7,8,9];
var arr3 = [1,5,8,3,13,56,3,35];
function remove_index(arr, ind){
    for(var i = ind; i<arr.length; i++){
        arr[i] = arr[i+1]
    }
    arr.pop()
    return arr
}
// Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
// array – move values within the array that you are given. As always, do not use built-in array functions such as splice().
// Step one iterate through half of array(will need to round down if half of array is a float)
// Take first index and assign it to temp variable
// Assign first index the value of last index
// Assign last index the value of the temp variable. 
function swap_indexes(arr){
    var half = arr.length/2;
    console.log(half);

    for (var i = 0; i<=half; i++){
        var temp1 = arr[i]
        arr[i]= arr[(arr.length-1)-i]
        arr[(arr.length-1)-i] = temp1
    }
    console.log(arr)
    return arr
}
// swap_indexes(arr3)
// swap_indexes(arr2)
// swap_indexes(arr1)

// sImplement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), 
// change the array to [3,1,2]. Don't use built-in functions.
// Second: allow negative shiftBy (shift L, not R).
// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
// Fourth: minimize the touches of each element.
// iterate through the array using the number of shiftBy
// each iteration shift the numbers down one spot

function rotate(arr, offset){
    if (Math.abs(offset)>arr.length){    //reduces the number offsets to as small a number as possible
        console.log(offset)
        offset = offset%arr.length
        console.log(offset)
    }
    var negative_check = false    //assumes variable is a positive number
    if(offset<0){           //Will only trigger if offset is a negative number
        negative_check = true    //changes negative check to true 
        arr = arr.reverse()    //reverses our array
        offset = Math.abs(offset)
    }
    for( var a = 0; a<offset; a++)  {
        var temp1 = arr[0], temp2 = arr[1];
        for(var i = 0; i<arr.length && temp1 != undefined; i++){
            arr[i+1] = temp1
            temp1 = temp2 
            temp2 = arr[i+2]
        }
        arr[0] = arr[arr.length-1]
        arr.pop()
        
    }
    if(negative_check == true){
        arr= arr.reverse()
    }
    console.log(arr)
}
// console.log(arr1)
// console.log([ 9, 1, 3, 5, 7 ])
// rotate(arr1, 1)
// rotate(arr1, 2)
// rotate(arr1, 3)
// rotate(arr1, 5)
// rotate(arr1, 1)
// rotate(arr1, -6)     //Why are these chaining? I'm not returning arr, only printing it, the value of arr should reset to the univeral variable once the function is done 
// console.log(arr1)
// rotate(arr1, 1)
// rotate(arr1, 1)
// 1,3,5,7,9  "9,1,3,5,7"    // Shifted to the right
// 1,3,5,7,9  "3,5,7,9,1" "5,7,9,1,3" // Shifted to the left 
// 9,7,5,3,1  "1,9,7,5,3"  '3,5,7,9,1'// Revered and shift to the right then reversed again. 
// // Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.
function eliminate_outliers(arr, min, max){
    for(var i = 0; i<arr.length; i++){
        if(arr[i] < min || arr[i] > max){
            remove_index(arr, i);
            i = i-1
        }
    }
    return arr
}
// console.log(eliminate_outliers(arr1, 3,5))
// Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].
function concat_arr(arr1, arr2){
    let new_array = []
    for(var i = 0; i<arr1.length; i++){
        new_array.push(arr1[i])
    }
    for(var i = 0; i<arr2.length; i++){
        new_array.push(arr2[i])
    }
return new_array
}
console.log(concat_arr(arr1,arr2))