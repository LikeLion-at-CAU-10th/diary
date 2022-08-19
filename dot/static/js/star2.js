//클릭하는 순간 검은색으로 변경
//선 -> 점 검은색으로 변하자마자 나오게
//일기 확인버튼을 누르면 효과나오기(일기장 페이지에서 연결)->그럴려면 한 페이지에서 해야할 것 같기도...
//점이 회색이면 일기 쓰는 페이지로 연결, 검은색이면 작성한 페이지로 연결
// const dot1 = document.querySelector("#dot1");
let dot1 = document.querySelector("#dot1");
let dot2 = document.querySelector("#dot2");
let dot3 = document.querySelector("#dot3");
let dot4 = document.querySelector("#dot4");
let dot5 = document.querySelector("#dot5");
let dot6 = document.querySelector("#dot6");
let dot7 = document.querySelector("#dot7");

function click1() {
  dot1 = document.querySelector("#dot1");

  const currentColor = dot1.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot1.style.backgroundColor = newColor;
}

function click2() {
  //   if (dot1.style.backgroundColor == "black") {
  const currentColor = dot2.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#onetwo");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 0);
    context.lineTo(80, 30);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot2.style.backgroundColor = newColor;
  //   }
}
function click3() {
  //   if (
  //     dot1.style.backgroundColor == "black" &&
  //     dot2.style.backgroundColor == "black"
  //   ) {
  const currentColor = dot3.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#twothree");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 55);
    context.lineTo(56, 0);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot3.style.backgroundColor = newColor;
  //   }
}
function click4() {
  //   if (
  //     dot1.style.backgroundColor == "black" &&
  //     dot2.style.backgroundColor == "black" &&
  //     dot3.style.backgroundColor == "black"
  //   ) {
  const currentColor = dot4.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#threefour");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 30);
    context.lineTo(80, 0);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot4.style.backgroundColor = newColor;
  //   }
}
function click5() {
  //   if (
  //     dot1.style.backgroundColor == "black" &&
  //     dot2.style.backgroundColor == "black" &&
  //     dot3.style.backgroundColor == "black" &&
  //     dot4.style.backgroundColor == "black"
  //   ) {
  const currentColor = dot5.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#fourfive");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 0);
    context.lineTo(80, 30);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot5.style.backgroundColor = newColor;
  //   }
}

function click6() {
  //   if (dot1.style.backgroundColor == "black") {
  const currentColor = dot6.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#fivesix");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 30);
    context.lineTo(80, 0);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot6.style.backgroundColor = newColor;
  //   }
}

function click7() {
  //   if (dot1.style.backgroundColor == "black") {
  const currentColor = dot7.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#sixseven");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 0);
    context.lineTo(80, 30);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot7.style.backgroundColor = newColor;
  //   }
}

function click8() {
  //   if (dot1.style.backgroundColor == "black") {
  const currentColor = dot8.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#seveneight");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 0);
    context.lineTo(56, 50);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot8.style.backgroundColor = newColor;
  //   }
}

function click9() {
  //   if (dot1.style.backgroundColor == "black") {
  const currentColor = dot9.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#eightnine");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 30);
    context.lineTo(80, 0);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot9.style.backgroundColor = newColor;
  //   }
}

window.onload = function(){
  click1();
  click2();
}