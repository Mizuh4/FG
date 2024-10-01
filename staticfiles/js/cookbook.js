function toCookbook() {
    document.querySelectorAll('.add-recipe, .remove-recipe').forEach(button => {
        button.onclick = function() {
            var recipeId = this.dataset.recipe
            var action = this.dataset.action
            console.log(`recipeId: ${recipeId}, action: ${action}`);
            
            console.log('USER: ', user)
            if (user === 'AnonymousUser') {
                console.log('Not logged in.')
                window.location.href = '/login/';
            } else {
                console.log('Logged in.')
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
        alert('Hello, World')
    })
}

document.addEventListener("DOMContentLoaded", function() {
    console.log("cookbook.js");
    toCookbook();
})