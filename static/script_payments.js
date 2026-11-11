
const mainButton = document.getElementById("index_main");
mainButton.addEventListener("click", function() {
    window.location.href = "/";
});

const paymentsButton = document.getElementById("index_payments");
paymentsButton.addEventListener("click", function() {
    window.location.href = "/index_payments";
});

const addpayButton = document.getElementById("add_pay");
addpayButton.addEventListener("click", function() {
    window.location.href = "/add_pay";
});

const viewpayButton = document.getElementById("view_pay");
viewpayButton.addEventListener("click", function() {
    window.location.href = "/view_pay";
});

const deletepayButton = document.getElementById("delete_pay");
deletepayButton.addEventListener("click", function() {
    window.location.href = "/delete_pay";
});
