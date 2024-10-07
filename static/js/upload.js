function sortableMultifield(){
    document.querySelectorAll('.multifield-container').forEach(container => {
        Sortable.create(container, {animation: 150});
    })
}
    
function addField() {
    document.querySelectorAll('.multifield-container').forEach(container => {
        ['keypress'].forEach(evt => 
            container.addEventListener(evt, function(event) {
                
                if (event.key === "Enter" && event.target.value.length > 0 /*&& container.childElementCount < 10*/) {
                    if (container.classList.contains('tag-fields') && container.childElementCount > 9 ) {
                        event.preventDefault();
                    } else if (container.classList.contains('step-fields') && container.childElementCount > 19 ) {
                        event.preventDefault();
                    } else if (container.classList.contains('ingredient-fields') && container.childElementCount > 29 ) {
                        event.preventDefault();
                    } else {
                        event.preventDefault();
        
                        // Create a string representing the element
                        const newField = container.querySelector('.input-group').outerHTML
    
                        // Create a new DOMParser
                        const parser = new DOMParser();
        
                        // Parse the element string
                        const doc = parser.parseFromString(newField, 'text/html');
        
                        // Access the parsed element
                        const element = doc.body.firstChild;
        
                        // Manipulate or append the element to the document
                        container.appendChild(element)
                        //console.log('Successfully Added a new field.')
                        container.lastElementChild.children[0].innerHTML = ""
                        container.lastElementChild.children[0].setAttribute("value", "")
                        //console.log("INNERHTML CLEARED")
                        container.lastElementChild.children[0].focus()
                        deleteField(container);
                        textareaExpand();
                    }
                }
                
                else if (event.key === "Enter" && event.target.value.length === 0) {
                    event.preventDefault();
                }
                else if (event.key === "Enter" && !(container.childElementCount < 10)) {
                    event.preventDefault();
                    console.log('heheboi')
                }
            }, false)
        )
        deleteField(container);
        textareaExpand()
    })
}

function deleteField(container) {
    buttons = container.querySelectorAll('.delete-button').forEach(button => {
        button.onclick = function() {
            const field = this.parentElement.previousElementSibling.value.length
            console.log(container.childElementCount)
            if (container.childElementCount > 1) {
                this.parentElement.parentElement.remove()
            }
        }
    })
}

function textareaExpand() {
    document.querySelectorAll('textarea').forEach(textareaEle => {
        textareaEle.style.height = 'auto';
        textareaEle.style.height = `${textareaEle.scrollHeight}px`;
        textareaEle.addEventListener('input', () => {
            // Code to be executed when user types in textarea
            textareaEle.style.height = 'auto';
            textareaEle.style.height = `${textareaEle.scrollHeight}px`;
            console.log("ahsushad")
        });
    })
}

document.addEventListener('DOMContentLoaded', function() {
    console.log("upload.js");
    sortableMultifield();
    addField();
})