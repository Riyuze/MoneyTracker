const usernameField = document.querySelector('#usernameField');
const emailField = document.querySelector('#emailField');

const usernameFeedbackArea = document.querySelector('.username-invalid-feedback');
const emailFeedbackArea = document.querySelector('.email-invalid-feedback');

const usernameSuccessOutput =  document.querySelector('.usernameSuccessOutput');
const emailSuccessOutput =  document.querySelector('.emailSuccessOutput');

const passwordField = document.querySelector('#passwordField');

const showPasswordToggle = document.querySelector('.showPasswordToggle');

usernameField.addEventListener('keyup', (e) => {
    const usernameValue = e.target.value;

    usernameField.classList.remove("is-invalid");
    usernameFeedbackArea.style.display = "none";

    if (usernameValue.length > 0) {
        usernameSuccessOutput.style.display = "block";
        usernameSuccessOutput.textContent =  `Checking ${usernameValue}`;

        fetch('/authentication/validate-username', {
            body: JSON.stringify({ username: usernameValue }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            usernameSuccessOutput.style.display = "none";
            if (data.username_error) {
                usernameField.classList.add("is-invalid");
                usernameFeedbackArea.style.display = "block";
                usernameFeedbackArea.innerHTML = `<p>${data.username_error}</p>`;
            }
        });
    }
});

emailField.addEventListener('keyup', (e) => {
    const emailValue = e.target.value;

    emailField.classList.remove("is-invalid");
    emailFeedbackArea.style.display = "none";

    if (emailValue.length > 0) {
        emailSuccessOutput.style.display = "block";
        emailSuccessOutput.textContent =  `Checking ${emailValue}`;
        fetch('/authentication/validate-email', {
            body: JSON.stringify({ email: emailValue }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            emailSuccessOutput.style.display = "none";
            if (data.email_error) {
                emailField.classList.add("is-invalid");
                emailFeedbackArea.style.display = "block";
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
            }
        });
    }
});


const handleToggleInput = (e) => {
    if (passwordField.type === "password")
    {
        passwordField.setAttribute("type", "text");
    }
    else
    {
        passwordField.setAttribute("type", "password");
    }
};

showPasswordToggle.addEventListener("click", handleToggleInput);