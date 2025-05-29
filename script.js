const backendUrl = "https://grant-app-backend.onrender.com";

document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");
    if (forms.length > 0) {
        const form = forms[0];
        form.addEventListener("submit", async (e) => {
            e.preventDefault();

            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            const path = window.location.pathname;
            const formName = path.substring(path.lastIndexOf("/") + 1).replace(".html", "");

            const res = await fetch(`${backendUrl}/${formName}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });

            const msg = document.getElementById("statusMessage") || document.createElement("p");
            msg.id = "statusMessage";
            document.body.appendChild(msg);

            if (res.ok) {
                const blob = await res.blob();
                const link = document.createElement("a");
                link.href = window.URL.createObjectURL(blob);
                link.download = `${formName}.docx`;
                link.click();
                msg.textContent = "Download ready.";
            } else {
                msg.textContent = "Submission failed.";
            }
        });
    }
});