"use strict"

function loadNextExercise() {
            // Fetch the next exercise data
            fetch('/session/nextExercise')
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        // Update the image source and exercise name
                        let exerciseImage = document.getElementById('exerciseImage');

                        exerciseImage.src = data.src;
                        exerciseImage.alt = "Western music notation describing " + data.title;
                        exerciseImage.title = data.title;
                        let exerciseDescription = document.getElementById("exerciseDescription");
                        exerciseDescription.innerHTML = data.description
                        let title = document.getElementById("exerciseTitle")
                        title.innerHTML = data.title
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
