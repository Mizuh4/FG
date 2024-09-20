document.addEventListener("DOMContentLoaded", function() {
    console.log('recipe.js hi')
    
    var i = 0;
    document.querySelectorAll(".carousel-indicators-btn").forEach(btn => {
        btn.classList.remove('active')
        document.querySelector(".carousel-indicators-btn").classList.add('active')
        console.log(i)
        btn.setAttribute("data-bs-slide-to", `${i}`)
        i++

    })

    // Get the modal
    document.querySelectorAll(".carousel-item").forEach(item => {
        item.classList.remove('active')
        document.querySelector(".carousel-item").classList.add('active')
        
        // Get the image and insert it inside the modal - use its "alt" text as a caption
        var modal = item.querySelector(".myModal");
        var img = item.querySelector(".myImg");
        var modalImg = item.querySelector(".img01");
        var captionText = item.querySelector(".caption");
        //console.log(img.src)
        //console.log(img.alt)

        img.onclick = () => {
            console.log(img.src)
            console.log(img.alt)
            document.querySelectorAll(".carousel-control-prev, .carousel-control-next, .carousel-indicators").forEach(button => {
                button.style.visibility = 'hidden'
            })
            modal.style.display = "block";
            modalImg.src = img.src;
            captionText.innerHTML = img.alt;
        }

        // Get the <span> element that closes the modal
        var span = item.getElementsByClassName("close")[0];

        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
        document.querySelectorAll(".carousel-control-prev, .carousel-control-next, .carousel-indicators").forEach(button => {
            button.style.visibility = 'visible'
        })
        modal.style.display = "none";
        
        }
    })
})
