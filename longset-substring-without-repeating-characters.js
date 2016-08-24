/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var charQueue = [],
        charHashMap = {},
        maxLong = 0,
        nowLong = 0; 
    
    for (var i = 0; i < s.length; i++) {
        if (!charHashMap.hasOwnProperty(s.charAt(i)) || charHashMap[s.charAt(i)] !== 1 ) {
            charQueue.push(s.charAt(i));
            charHashMap[s.charAt(i)] = 1;
            maxLong = ++nowLong > maxLong ? nowLong : maxLong;
        } else {
            while (true) {
                if (charQueue[0] === s.charAt(i)) {
                    charHashMap[charQueue[0]] = 0;
                    charQueue.shift();
                    break;
                } else {
                    charHashMap[charQueue[0]] = 0;
                    charQueue.shift();
                }
            }
            charQueue.push(s.charAt(i));
            charHashMap[s.charAt(i)] = 1;
            nowLong = charQueue.length;
        }
    }
    return maxLong;
};