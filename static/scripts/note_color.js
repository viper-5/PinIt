document.addEventListener('DOMContentLoaded', function () {
    colorPicker();
}, false);

var xncolorpicker

function colorPicker() {
    document.getElementsByClassName('new-note-form')[0].style.backgroundColor = isDark ? "#202124" : "#ffffff";

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
    target = document.getElementsByClassName('fcolorpicker-curbox')[0];
    target.addEventListener("click", function (event) {
        ipBox = document.querySelector(".current-color-value > input:nth-child(1)");
        console.log(ipBox);
        ipBox.disabled = true;
        ipBox.style.height = "23px";
        ipBox.style.width = "100%";
        ipBox.style.padding = "1px 0";
        ipBox.style.textAlign = "center";
        document.querySelector(".current-color-value").style.padding = "0 0";


    })

}