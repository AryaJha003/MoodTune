// =========================================
// MoodTune - Frontend Logic
// =========================================


// -----------------------------------------
// Get recommendations
// -----------------------------------------

async function getRecommendations() {

    const moodText =
        document.getElementById("moodText").value.trim();

    const language =
        document.getElementById("language").value;

    const genre =
        document.getElementById("genre").value;

    const button =
        document.getElementById("recommendButton");

    const buttonText =
        document.getElementById("buttonText");

    const spinner =
        document.getElementById("loadingSpinner");

    const resultsSection =
        document.getElementById("resultsSection");

    const songsContainer =
        document.getElementById("songsContainer");

    const errorMessage =
        document.getElementById("errorMessage");

    const detectedMood =
        document.getElementById("detectedMood");


    // -----------------------------------------
    // Validate input
    // -----------------------------------------

    if (!moodText) {

        showError(
            "Please tell MoodTune how you are feeling."
        );

        return;
    }


    // -----------------------------------------
    // Reset UI
    // -----------------------------------------

    errorMessage.classList.add("hidden");

    resultsSection.classList.add("hidden");

    songsContainer.innerHTML = "";


    // -----------------------------------------
    // Loading state
    // -----------------------------------------

    button.disabled = true;

    buttonText.textContent =
        "Finding your music...";

    spinner.classList.remove("hidden");


    try {

        // -----------------------------------------
        // Send request to Flask
        // -----------------------------------------

        const response = await fetch(
            "/recommend",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    text: moodText,
                    language: language,
                    genre: genre
                })
            }
        );


        const data =
            await response.json();


        // -----------------------------------------
        // Handle backend error
        // -----------------------------------------

        if (!response.ok || !data.success) {

            throw new Error(
                data.error ||
                "Something went wrong."
            );
        }


        // -----------------------------------------
        // Display detected mood
        // -----------------------------------------

        detectedMood.textContent =
            data.emotion;


        // -----------------------------------------
        // Display recommendations
        // -----------------------------------------

        displaySongs(
            data.songs
        );


        resultsSection.classList.remove(
            "hidden"
        );


        // Scroll to results

        resultsSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });


    } catch (error) {

        console.error(error);

        showError(
            error.message ||
            "Unable to get recommendations."
        );

    } finally {

        // -----------------------------------------
        // Reset button
        // -----------------------------------------

        button.disabled = false;

        buttonText.textContent =
            "✨ Find My Music";

        spinner.classList.add("hidden");
    }
}



// -----------------------------------------
// Display songs
// -----------------------------------------

function displaySongs(songs) {

    const container =
        document.getElementById(
            "songsContainer"
        );


    container.innerHTML = "";


    // No songs

    if (!songs || songs.length === 0) {

        container.innerHTML = `
            <div class="error-message">
                No songs found for these preferences.
                Try another language or genre.
            </div>
        `;

        return;
    }


    // Create song cards

    songs.forEach(
        (song, index) => {

            const card =
                document.createElement(
                    "div"
                );

            card.className =
                "song-card";


            card.innerHTML = `

                <div class="song-number">
                    #${index + 1}
                </div>

                <div class="song-name">
                    ${escapeHTML(
                        song.track_name
                    )}
                </div>

                <div class="artist-name">
                    ${escapeHTML(
                        song.artist
                    )}
                </div>

                <div class="song-details">

                    <span class="badge">
                        🌍 ${escapeHTML(
                            song.language
                        )}
                    </span>

                    <span class="badge">
                    🎵 Style: ${escapeHTML(
                    song.style
                    )}
                    </span>

                    <span class="badge">
                        ⭐ ${song.popularity}
                    </span>

                </div>

                <div class="match-score">
                    ${song.match_score}% mood match
                </div>

                <div class="song-meta">
    <span>📅 Released: ${song.release_date ? song.release_date.slice(-4) : "Unknown"}</span>
</div>

            `;


            container.appendChild(
                card
            );
        }
    );
}


// -----------------------------------------
// Show error
// -----------------------------------------

function showError(message) {

    const errorMessage =
        document.getElementById(
            "errorMessage"
        );

    errorMessage.textContent =
        message;

    errorMessage.classList.remove(
        "hidden"
    );

    errorMessage.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
}


// -----------------------------------------
// Escape HTML
// -----------------------------------------

function escapeHTML(value) {

    const div =
        document.createElement(
            "div"
        );

    div.textContent =
        value ?? "";

    return div.innerHTML;
}


function scrollToMood() {
    const moodInput = document.getElementById("moodText");

    if (moodInput) {
        moodInput.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

        setTimeout(() => {
            moodInput.focus();
        }, 500);
    }
}