function reloadButton() {
    document.querySelectorAll('.reload-button').forEach(button => {
        button.disabled = true
        button.onclick = function() {
            location.reload()
        }
        document.querySelectorAll('.profile-field').forEach(field => {
            field.onkeyup = () => {
                button.disabled = false;
            }
            /*field.onkeydown = () => {
                button.disabled = false;
            }*/
        })
    })
}

document.addEventListener("DOMContentLoaded", function() {
    console.log("profile.js");
    reloadButton();
})