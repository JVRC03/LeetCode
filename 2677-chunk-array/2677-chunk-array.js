/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, k) {
    let jvrc = []; 
    let c = 0;
    let temp = []; 

    for(let i = 0; i < arr.length; i++)
    {
        temp.push(arr[i]);
        c += 1; 
        if(c == k)
        {
            jvrc.push(temp)
            c = 0; 
            temp = [];
        }
    }

    if(c > 0)
    {
        jvrc.push(temp);
    }

    return jvrc;
    
};
