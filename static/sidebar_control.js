const sidebar = document.querySelector(".side-menu");
const trigger = document.querySelector(".sidebar-trigger");

if (sidebar) {
    if (sessionStorage.getItem("sidebarOpen") === "true") {
        sidebar.classList.add("is-open");
    }

    sidebar.addEventListener("mouseenter", function() {
        sidebar.classList.add("is-open");
        sessionStorage.setItem("sidebarOpen", "true");
    });

    sidebar.addEventListener("mouseleave", function() {
        sidebar.classList.remove("is-open");
        sessionStorage.removeItem("sidebarOpen");
    });
}

if (sidebar && trigger) {
    trigger.addEventListener("mouseenter", function() {
        sidebar.classList.add("is-open");
        sessionStorage.setItem("sidebarOpen", "true");
    });
}