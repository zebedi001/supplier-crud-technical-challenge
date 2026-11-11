
const mainButton = document.getElementById("index_main");
mainButton.addEventListener("click", function() {
    window.location.href = "/";
});

const supplierButton = document.getElementById("index_supplier");
supplierButton.addEventListener("click", function() {
    window.location.href = "/index_supplier";
});

const addsupButton = document.getElementById("add_supplier");
addsupButton.addEventListener("click", function() {
    window.location.href = "/add_supplier";
});

const amendsupButton = document.getElementById("amend_supplier");
amendsupButton.addEventListener("click", function() {
    window.location.href = "/amend_supplier";
});

const deletesupButton = document.getElementById("delete_supplier");
deletesupButton.addEventListener("click", function() {
    window.location.href = "/delete_supplier";
});

const accountsupButton = document.getElementById("account_details");
accountsupButton.addEventListener("click", function() {
    window.location.href = "/account_details";
});

const addresssupButton = document.getElementById("address_details");
addresssupButton.addEventListener("click", function() {
    window.location.href = "/address_details";
});


