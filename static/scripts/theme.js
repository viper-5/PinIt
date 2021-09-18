// you can use app's unique identifier here
const LOCAL_STORAGE_KEY = "toggle-bootstrap-theme";

const LOCAL_META_DATA = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));

// you can change this url as needed
const DARK_THEME_PATH = "https://cdn.jsdelivr.net/npm/bootswatch@5.1.0/dist/vapor/bootstrap.min.css";
const LIGHT_THEME_PATH = "https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css";

// const DARK_STYLE_LINK = document.getElementById("dark-theme-style");
const DARK_STYLE_LINK = document.getElementById("theme");
const THEME_TOGGLER = document.getElementById("theme-toggler");

var isDark = LOCAL_META_DATA && LOCAL_META_DATA.isDark;
const lightColors = [
    '#f28b82', '#fbbc04', '#fff475', '#ccff90',
    '#a7ffeb', '#cbf0f8', '#aecbfa', '#d7aefb',
    '#fdcfe8', '#e6c9a8', '#e8eaed', '#ffffff'
];
const darkColors = [
    '#202124', '#5c2b29', '#614a19', '#635d19',
    '#345920', '#16504b', '#2d555e', '#1e3a5f',
    '#42275e', '#5b2245', '#442f19', '#3c3f43'
]

// check if user has already selected dark theme earlier
if (isDark) {
    enableDarkTheme();
} else {
    disableDarkTheme();
}

/**
 * Apart from toggling themes, this will also store user's theme preference in local storage.
 * So when user visits next time, we can load the same theme.
 */
function toggleTheme() {
    isDark = !isDark;
    if (isDark) {
        enableDarkTheme();
        xncolorpicker.destroy();

        colorPicker();
    } else {
        disableDarkTheme();
        xncolorpicker.destroy()
        colorPicker();
    }
    const META = {
        isDark
    };
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(META));
}

function enableDarkTheme() {
    DARK_STYLE_LINK.setAttribute("href", DARK_THEME_PATH);
    THEME_TOGGLER.innerHTML = "🌙 Dark";
    $('h2').addClass('cyberTextColor');
}

function disableDarkTheme() {
    DARK_STYLE_LINK.setAttribute("href", LIGHT_THEME_PATH);
    THEME_TOGGLER.innerHTML = "🌞 Light";
    $('h2').removeClass('cyberTextColor');
}
console.log(darkColors);