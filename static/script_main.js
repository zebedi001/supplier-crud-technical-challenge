
const mainButton = document.getElementById("index_main");
mainButton.addEventListener("click", function() {
    window.location.href = "/";
});

const supplierButton = document.getElementById("index_supplier");
supplierButton.addEventListener("click", function() {
    window.location.href = "index_supplier";
});

const purchasesButton = document.getElementById("index_purchases");
purchasesButton.addEventListener("click", function() {
    window.location.href = "index_purchases";
});

const paymentsButton = document.getElementById("index_payments");
paymentsButton.addEventListener("click", function() {
    window.location.href = "index_payments";
});

const ledgerButton = document.getElementById("index_ledger");
ledgerButton.addEventListener("click", function() {
    window.location.href = "index_ledger";
});

const reportsButton = document.getElementById("index_reports");
reportsButton.addEventListener("click", function() {
    window.location.href = "index_reports";
});

const settingsButton = document.getElementById("index_settings");
settingsButton.addEventListener("click", function() {
    window.location.href = "index_settings";
});
