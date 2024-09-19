function multifield(){
    document.querySelectorAll('.multifield-container').forEach(container => {
        Sortable.create(container, {animation: 150});
    })

    // Simple list
    //Sortable.create(uploadList, { /* options */ });
}
    
function addField() {
    document.querySelectorAll('.multifield-container').forEach(container => {
        //var fields = container.children
        //for (var field of fields) {
            ['keypress'].forEach(evt => 
                container.addEventListener(evt, function(event) {
                    if (event.key === "Enter" && event.target.value.length > 0 /*&& container.childElementCount < 10*/) {
                        event.preventDefault();
                        //alert('ENTER!!')
                        //console.log(field.outerHTML)
        
                        // Create a string representing the element
                        const newField = container.querySelector('.input-group').outerHTML

                        // Create a new DOMParser
                        const parser = new DOMParser();
        
                        // Parse the element string
                        const doc = parser.parseFromString(newField, 'text/html');
        
                        // Access the parsed element
                        const element = doc.body.firstChild;
        
                        // Now you can manipulate or append the element to the document
                        container.appendChild(element)
                        console.log('Successfully Added a new field.')
                        container.lastElementChild.children[0].innerHTML = ""
                        container.lastElementChild.children[0].setAttribute("value", "")
                        console.log("INNERHTML CLEARED")
                        container.lastElementChild.children[0].focus()
                        deleteField(container);
                        textareaExpand();
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
            console.log('expand')
        //}
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
    multifield();
    addField();
})