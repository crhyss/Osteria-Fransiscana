const visibilityBtn = document.getElementById("visibilityBtn")

visibilityBtn.addEventListener("click", toggleVisibility)

function toggleVisibility(){
    const passwordInput = document.getElementById("pass")
    const icon = document.getElementById("visibilityIcon")
    if (passwordInput.type === "password"){
        passwordInput.type = "text"
        icon.innerText = "visibility_off"
    } else {
        passwordInput.type = "password"
        icon.innerText = "visibility"
    }
    
}