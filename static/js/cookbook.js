function toCookbook() {
    document.querySelectorAll('.add-recipe, .remove-recipe').forEach(button => {
        button.onclick = function() {
            var recipeId = this.dataset.recipe
            var action = this.dataset.action
            console.log(`recipeId: ${recipeId}, action: ${action}`);
            
            console.log('USER: ', user)
            if (user === 'AnonymousUser') {
                console.log('Not logged in.')
            } else {
                updateCookbook(recipeId, action)
            }
        }
    })
}

function updateCookbook(recipeId, action) {
    console.log('User is logged in, sending data...')

    var url = '/update_cookbook/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'recipeId': recipeId, 'action': action})
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log('data:', data)
        location.reload()
    })
}

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
            field.onkeydown = () => {
                button.disabled = false;
            }
        })
    })
}

document.addEventListener("DOMContentLoaded", function() {
    console.log("ContentLoaded");
    toCookbook();
    reloadButton();
    console.log('test')
})