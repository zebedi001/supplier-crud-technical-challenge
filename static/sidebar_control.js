
const sidebar = document.querySelector(".side-menu");
const trigger = document.querySelector(".sidebar-trigger");

if (sidebar) {
    sidebar.addEventListener("mouseenter", function() {
        sidebar.classList.add("is-open");
    });

    sidebar.addEventListener("mouseleave", function() {
        sidebar.classList.remove("is-open");
    });
}

if (sidebar && trigger) {
    trigger.addEventListener("mouseenter", function() {
        sidebar.classList.add("is-open");
    });
}