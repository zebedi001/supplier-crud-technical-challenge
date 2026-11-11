
const mainButton = document.getElementById("index_main");
mainButton.addEventListener("click", function() {
    window.location.href = "/";
});

const ledgerButton = document.getElementById("index_ledger");
ledgerButton.addEventListener("click", function() {
    window.location.href = "/index_ledger";
});

const viewaccallButton = document.getElementById("view_acc_all");
viewaccallButton.addEventListener("click", function() {
    window.location.href = "/view_acc_all";
});

const viewtransacButton = document.getElementById("view_transac"); 
viewtransacButton.addEventListener("click", function() {
    window.location.href = "/view_transac";
});

const allocmatchButton = document.getElementById("alloc_match");
allocmatchButton.addEventListener("click", function() {
    window.location.href = "/alloc_match";
});

const viewoutitemsButton = document.getElementById("view_out_items"); 
viewoutitemsButton.addEventListener("click", function() {
    window.location.href = "/view_out_items";
});

const manualadjButton = document.getElementById("manual_adj");
manualadjButton.addEventListener("click", function() {
    window.location.href = "/manual_adj";
});