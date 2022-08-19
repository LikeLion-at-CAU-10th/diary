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
    context.lineTo(40, 0);
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
    context.moveTo(55, 0);
    context.lineTo(0, 90);
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
    context.moveTo(0, 0);
    context.lineTo(55, 0);
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
    context.moveTo(65, 0);
    context.lineTo(0, 100);
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
    context.moveTo(110, 0);
    context.lineTo(0, 40);
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
    context.lineTo(115, 40);
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
    context.lineTo(65, 100);
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
    context.moveTo(0, 0);
    context.lineTo(55, 0);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot9.style.backgroundColor = newColor;
  //   }
}

function click10() {
  //   if (dot1.style.backgroundColor == "black") {
  const currentColor = dot10.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#nineten");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 0);
    context.lineTo(55, 90);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot10.style.backgroundColor = newColor;
  //   }
}
function click11() {
  //   if (dot1.style.backgroundColor == "black") {
  const currentColor = dot11.style.backgroundColor;
  let newColor;
  if (currentColor != "black") {
    newColor = "black";
    //선
    const canvas = document.querySelector("#teneleven");
    var context = canvas.getContext("2d");
    context.strokeStyle = "black";
    context.lineWidth = 3;

    context.beginPath();
    context.moveTo(0, 0);
    context.lineTo(40, 0);
    context.stroke();
  } else {
    //다음페이지 나오게 -> html에 연결해두고 display:none해놨다가 display:block으로 변경하자
  }
  dot11.style.backgroundColor = newColor;
  //   }
}
window.onload = function(){
    click1();
    click2();
    click3();
    click4();
    click5();
    click6();
    click7();
    click8();

  }
