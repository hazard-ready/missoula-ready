// MMP Top Site Structure
// Montana State Library
// Stacy Bruhn
// 1/20/2016
// Top load javascript for MMP Site

var searchSiteString = window.location.href.toLowerCase();
if (searchSiteString == "http://mtmemory.org/") {
    window.location.href = "http://montanamemory.org/";
}

$("body").prepend("<div class='spinnerDiv'><div class='spinnerDivInner'><center><img src='http://mslsrc.mt.gov/images/banners/montana_memory_projectSpinner.jpg' /></center></div></div>")
