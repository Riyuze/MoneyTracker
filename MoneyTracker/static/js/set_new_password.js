const passwordField = document.querySelector('#passwordField');
const confirmpasswordField = document.querySelector('#confirmpasswordField');

const showPasswordToggle = document.querySelector('.showPasswordToggle');

const handleToggleInput = (e) => {
    if (passwordField.type === "password")
    {
        passwordField.setAttribute("type", "text");
        confirmpasswordField.setAttribute("type", "text");
    }
    else
    {
        passwordField.setAttribute("type", "password");
        confirmpasswordField.setAttribute("type", "password");
    }
};

showPasswordToggle.addEventListener("click", handleToggleInput);
