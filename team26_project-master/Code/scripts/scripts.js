function openManageMem(){
    var curPage = document.getElementById("Home");
    var nxtPage = document.getElementById("member-mng");
    curPage.style.display = "none";
    nxtPage.style.display = "block";
}

function openAddMem(){
    var curPage = document.getElementById("member-mng");
    var nxtPage = document.getElementById("member-add");
    curPage.style.display = "none";
    nxtPage.style.display = "block";
}

function openRemMem(){
    var curPage = document.getElementById("member-mng");
    var nxtPage = document.getElementById("member-rmv");
    curPage.style.display = "none";
    nxtPage.style.display = "block";
}
