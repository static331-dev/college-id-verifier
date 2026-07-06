const verifyBtn = document.getElementById("verifyBtn");
const imageInput = document.getElementById("imageInput");
const result = document.getElementById("result");

verifyBtn.addEventListener("click", async () => {

    if (imageInput.files.length === 0) {
        alert("Please select an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", imageInput.files[0]);

    try {

        const response = await fetch("http://127.0.0.1:8000/verify", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        
        console.log(data);

        result.innerHTML = `
            <p><strong>Prediction:</strong> ${data.prediction}</p>
            <p><strong>Reconstruction Error:</strong> ${data.reconstruction_error}</p>
        `;

    } catch (error) {

        console.error(error);

        result.innerHTML = "Error connecting to backend.";

    }

});