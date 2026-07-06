const verifyBtn = document.getElementById("verifyBtn");
const imageInput = document.getElementById("imageInput");
const result = document.getElementById("result");
const preview = document.getElementById("preview");

// Show image preview
imageInput.addEventListener("change", () => {

    const file = imageInput.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
    }

});

verifyBtn.addEventListener("click", async () => {

    if (imageInput.files.length === 0) {
        alert("Please select an image first!");
        return;
    }

    // Disable button while verifying
    verifyBtn.disabled = true;
    verifyBtn.innerText = "Verifying...";

    const formData = new FormData();
    formData.append("file", imageInput.files[0]);

    try {

        const response = await fetch("http://127.0.0.1:8000/verify", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        let color = "green";
        let icon = "✅";

        if (data.prediction.includes("Suspicious")) {
            color = "red";
            icon = "❌";
        }

        result.innerHTML = `
            <p style="color:${color}; font-size:22px;">
                ${icon} ${data.prediction}
            </p>

            <p>
                <strong>Reconstruction Error:</strong>
                ${data.reconstruction_error}
            </p>
        `;

    } catch (error) {

        console.error(error);

        result.innerHTML = `
            <p style="color:red;">
                Error connecting to backend.
            </p>
        `;

    }

    // Enable button again
    verifyBtn.disabled = false;
    verifyBtn.innerText = "Verify ID";

});