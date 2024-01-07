(function () {
    const darkMode = window.matchMedia("(prefers-color-scheme: dark)");

    if (darkMode.matches) {
        document.documentElement.setAttribute("data-bs-theme", "dark");
    }

    darkMode.addEventListener("change", function (e) {
        if (e.matches) {
            document.documentElement.setAttribute("data-bs-theme", "dark");
        } else {
            document.documentElement.removeAttribute("data-bs-theme");
        }
    });
})();
