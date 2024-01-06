(function () {
    const darkMode = window.matchMedia("(prefers-color-scheme: dark)");

    if (darkMode.matches) {
        document.body.setAttribute("data-bs-theme", "dark");
    }

    darkMode.addEventListener("change", function (e) {
        if (e.matches) {
            document.body.setAttribute("data-bs-theme", "dark");
        } else {
            document.body.removeAttribute("data-bs-theme");
        }
    });
})();
