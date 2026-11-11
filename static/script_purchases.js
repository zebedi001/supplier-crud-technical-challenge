
const mainButton = document.getElementById("index_main");
mainButton.addEventListener("click", function() {
    window.location.href = "/";
});

const purchasesButton = document.getElementById("index_purchases");
purchasesButton.addEventListener("click", function() {
    window.location.href = "/index_purchases";
});

const addpoButton = document.getElementById("add_po");
addpoButton.addEventListener("click", function() {
    window.location.href = "/add_po";
});

const viewpoButton = document.getElementById("view_po");
viewpoButton.addEventListener("click", function() {
    window.location.href = "/view_po";
});

const deletepoButton = document.getElementById("delete_po");
deletepoButton.addEventListener("click", function() {
    window.location.href = "/delete_po";
});

const addinvButton = document.getElementById("add_inv");
addinvButton.addEventListener("click", function() {
    window.location.href = "/add_inv";
});

const viewinvButton = document.getElementById("view_inv");
viewinvButton.addEventListener("click", function() {
    window.location.href = "/view_inv";
});

const deleteinvButton = document.getElementById("delete_inv");
deleteinvButton.addEventListener("click", function() {
    window.location.href = "/delete_inv";
});

const addcnButton = document.getElementById("add_cn");
addcnButton.addEventListener("click", function() {
    window.location.href = "/add_cn";
});

const viewcnButton = document.getElementById("view_cn");
viewcnButton.addEventListener("click", function() {
    window.location.href = "/view_cn";
});

const deletecnButton = document.getElementById("delete_cn");
deletecnButton.addEventListener("click", function() {
    window.location.href = "/delete_cn";
});