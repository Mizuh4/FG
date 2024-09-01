console.log('Hello, World!')

function addRecipe() {
    document.querySelectorAll('.add-recipe').forEach(button => {
        button.onclick = function() {
            var recipeId = this.dataset.recipe
            var action = this.dataset.action
            console.log(`recipeId: ${recipeId}, action: ${action}`);
            
            console.log('USER: ', user)
            if (user === 'AnonymousUser') {
                console.log('Not logged in.')
            } else {
                console.log('User is logged in, sending data...')
            }
            
        }
    })
}

document.addEventListener("DOMContentLoaded", function() {
    console.log("ContentLoaded");
    addRecipe();
})