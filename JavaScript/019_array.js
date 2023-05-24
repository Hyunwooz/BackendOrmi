const arr1 = [];
const arr2 = [1, 2, 3];
const arr3 = new Array(4, 5, 6);

const arr = [[10, 20], 1, 2, 3, 4, 5];
arr[0];
arr[0][0];
arr.length;
arr.pop();
arr.pop(2); // 들어가는 값과 상관없이 마지막 값을 꺼냅니다. (index나 value와 무관)
arr.push(100);

const arr4 = [1, 2, 3, 4, 5];
arr4.shift();
arr4.unshift(100);
arr4.unshift(1000, 2000, 3000);

const arr5 = [1, 2, 3, 4, 5];
// splice() 메소드는 배열의 요소를 추가, 제거 또는 교체
// array.splice(start, deleteCount, changeitem)
arr5.splice(1, 0, 100);

arr5.splice(1, 1, 1000);

arr5.splice(1, 1, 10000, 20000);

let arr6 = [10, 20, 30, 40, 50, 60];
arr6.slice(2, 5); // array[2:5]

// 사전식 정렬입니다.
//
//
const arr7 = [1, 11, 2, 22, 3, 7, 8, 5];
arr7.sort();

// 오름차순
arr7.sort((a, b) => a - b);

// 내림차순
arr7.sort((a, b) => b - a);

// forEach 자주 사용합니다.
// forEach는 반복만 합니다!
// 새로운 arr를 만들고 싶다면 map을 사용해주세요.
const arr8 = [1, 11, 2, 3, 7, 8, 22, 5];
arr8.forEach((item, index, arr) => {
    console.log(item);
    console.log(index);
    console.log(arr);
});

const arr9 = [1, 11, 2, 3, 7, 8, 22, 5];
arr9.forEach((v, i) => {
    console.log(v); // value
    console.log(i); // i
});

/* 
<body>
    <div id="0">1</div>
    <div id="1">11</div>
    <div id="2">2</div>
    <div id="3">3</div>
    <div id="4">7</div>
    <div id="5">8</div>
    <div id="6">22</div>
    <div id="7">5</div>
</body> 
*/
const arr10 = [1, 11, 2, 3, 7, 8, 22, 5];
arr10.forEach((v, i) => {
    const tag = document.getElementById(i);
    tag.innerHTML = v;
});

const arr11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const newArr = arr11.filter((el) => el % 2 === 0);

console.log(newArr);

// https://school.programmers.co.kr/learn/courses/30/lessons/120583?language=javascript

function solution(array, n) {
    var answer = 0;
    return answer;
}

[1, 2, 3, 4, 5, 1, 1].filter(v => v == 1)
[1, 2, 3, 4, 5, 1, 1].filter(v => v == 1).length;

[1, 2, 3, 4, 5, 1, 1].filter(v => v == 1)

[10,20,30,40].reduce((a,c) => {
    console.log(a,c)
    return a + c
})

[10,20,30,40].reduce((a,c) => a+c,0)
[].reduce((a,c) => a+c,0)
[].reduce((a,c) => a+c) // 견고하지 못한 코드입니다.

// 우리가 생각하는 것처럼 in이 작동하지 않습니다.
// 여기서 in 앞에 나오는 값은 key(index) 입니다.
10 in [10,20,30,40]
'one' in {'one':1,'two':2}

[10,20,30,40].includes(10)

const arr12 = ['hello','world','hojun']