const passwordField = document.querySelector('#passwordField');

const showPasswordToggle = document.querySelector('.showPasswordToggle');

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