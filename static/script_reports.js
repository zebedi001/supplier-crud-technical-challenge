
const mainButton = document.getElementById("index_main");
mainButton.addEventListener("click", function() {
    window.location.href = "/";
});

const reportsButton = document.getElementById("index_reports");
reportsButton.addEventListener("click", function() {
    window.location.href = "/index_reports";
});

const agedcreditorsButton = document.getElementById("aged_creditors");
agedcreditorsButton.addEventListener("click", function() {
    window.location.href = "/aged_creditors";
});

const suppbalancesButton = document.getElementById("supp_balances"); 
suppbalancesButton.addEventListener("click", function() {
    window.location.href = "/supp_balances";
});

const outinvoicesButton = document.getElementById("out_invoices");
outinvoicesButton.addEventListener("click", function() {
    window.location.href = "/out_invoices";
});

const purchanalysisButton = document.getElementById("purch_analysis"); 
purchanalysisButton.addEventListener("click", function() {
    window.location.href = "/purch_analysis";
});

const payhistoryButton = document.getElementById("pay_history");
payhistoryButton.addEventListener("click", function() {
    window.location.href = "/pay_history";
});