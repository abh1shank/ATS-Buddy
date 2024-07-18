document.addEventListener("DOMContentLoaded", function() {
    const formElements = document.querySelectorAll("input[type='file'], input[type='text'], input[type='submit']");
    formElements.forEach(element => {
        element.addEventListener("focus", () => {
            element.style.transition = "all 0.3s ease-in-out";
            element.style.transform = "scale(1.05)";
        });

        element.addEventListener("blur", () => {
            element.style.transform = "scale(1)";
        });
    });

    // Add responsive navigation
    const container = document.querySelector(".container");
    if (window.innerWidth < 600) {
        container.style.padding = "10px";
    }

    window.addEventListener("resize", () => {
        if (window.innerWidth < 600) {
            container.style.padding = "10px";
        } else {
            container.style.padding = "20px";
        }
    });

    const responseDiv = document.querySelector(".response");
    if (responseDiv) {
        responseDiv.scrollIntoView({ behavior: 'smooth' });
    }
});
