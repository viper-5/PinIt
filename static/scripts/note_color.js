document.addEventListener('DOMContentLoaded', function () {
    colorPicker();
}, false);

var xncolorpicker

// Function to create the colorPicker
function colorPicker() {
    // change the background of the form to default color
    document.getElementsByClassName('new-note-form')[0].style.backgroundColor = isDark ? "#202124" : "#ffffff";

    // Create the color picker
    xncolorpicker = new XNColorPicker({
        selector: "#colorpicker",
        showPalette: false,
        showhistorycolor: false,
        format: "rgba",
        lang: "en",
        color: isDark ? "#202124" : "#ffffff",
        colorTypeOption: "single",
        canMove: false,

        // determine whether to show preset colors
        showprecolor: true,
        onCancel: function (color) {
            console.log("cancel", color);
        },
        onChange: function (color) {
            console.log("change", color);
        },
        onConfirm: function (color) {
            console.log("confirm", color);
            let elem = document.getElementsByClassName('new-note-form')[0];
            console.log(typeof (color.color.hex), color.color.hex);
            elem.style.backgroundColor = color.color.hex;
        },
        // customize your colors here
        prevcolors: (isDark ? darkColors : lightColors)
    });
    // Add border and shadow to the colorPicker div
    document.getElementsByClassName('fcolorpicker-curbox')[0].classList.add('border');
    document.getElementsByClassName('fcolorpicker-curbox')[0].classList.add(isDark ? 'myShadowDark' : 'myShadowLight');
    console.log(
        "new colorpicker initialized",
        window.getComputedStyle(document.getElementsByClassName(
            'new-note-form'
        )[0], null).getPropertyValue(
            "background-color"
        )
    );
    // Add click event listener to the color picker so that 
    // the input box showing the value of the color is disabled,
    // this ensures that user cannot change the color outside the pallete.
    target = document.getElementsByClassName('fcolorpicker-curbox')[0];
    target.addEventListener("click", function (event) {
        // select the inputbox to be disabled
        ipBox = document.querySelector(".current-color-value > input:nth-child(1)");
        ipBox.disabled = true;
        // A few CSS effects because the padding and 
        // the box position is irregular and it bugs me
        document.querySelector(".current-color-value").style.padding = "0 0";
        ipBox.style.height = "23px";
        ipBox.style.width = "100%";
        ipBox.style.padding = "1px 0";
        ipBox.style.textAlign = "center";
    })

}