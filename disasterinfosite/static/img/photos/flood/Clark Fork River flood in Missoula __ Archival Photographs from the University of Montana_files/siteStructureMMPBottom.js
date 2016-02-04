// MMP Bottom Site Structure
// Montana State Library
// Stacy Bruhn
// 1/20/2016
// Bottom load javascript for MMP Site

var searchSiteString = window.location.href.toLowerCase();

if (searchSiteString.indexOf("fullbrowser") > -1) {

}
else {
    $("#headerWrapper").hide();
    $("#nav_top").hide();
    $("#search").hide();
    $("#adv_search").hide();
    $("#cdmFooterWrapper").hide();
    if ($("#helpdocs_div").length > 0) {

    }
    else {
        $("<div id='template-page-wrapper' class='mmpCMDStructure'><div class='container'><div class='row'><div class='col-md-2' id='msl-page-nav-content'><div id='msl-nav-wrapper'><div id='msl-nav-mobile-button' class='hidden'><img id='msl-nav-mobile-button-image' src='http://mslsrc.mt.gov/images/icons/topMenuMobile.jpg'></div><div id='msl-print-heading'>Montana State Library</div><a id='msl-nav-logo-link' href='http://montanamemory.org'><img id='msl-nav-logo' class='img-responsive' src='http://mslsrc.mt.gov/images/mmpABR.jpg' aria-hidden='true' alt='Montana State Library Link to Home' aria-flowto='msl-nav-ul-block'></a><div id='msl-nav-mobile-wrapper'><div id='msl-nav-ul-wrapper' class=''><div class='msl-nav-functions-block' aria-hidden='true'><a class='msl-nav-function-expandAll'>Expand All</a> | <a class='msl-nav-function-collapseAll'>Collapse All</a></div><div id='msl-nav-ul-block'><ul id='msl-nav-ul' role='navigation' aria-label='Site Navigation'></ul></div><div class='msl-nav-functions-block' aria-hidden='true'><a class='msl-nav-function-expandAll'>Expand All</a> | <a class='msl-nav-function-collapseAll'>Collapse All</a></div></div></div></div></div><div class='col-md-10' id='msl-content-wrapper'><div id='msl-content' class='container'><div class='row'><div class='col-md-12'><div id='msl-page-home-top-banner-title'><a href='/home'>MONTANA MEMORY PROJECT</a></div><div id='msl-search-div' role='search'><div id='msl-search-bar' class=''>Search: What are you looking for? <span class='glyphicon glyphicon-chevron-right'></span><span class='glyphicon glyphicon-chevron-down hidden'></span></div><div id='msl-search-form' class='container'><div id='msl-search-form-types' class='row'></div><div id='msl-search-form-links-div' role='tablist' aria-label='Search Navigation'><div id='msl-search-form-links'></div></div></div></div></div><div class='row'><div id='MainContent_PageRepeater_mslpagecontentcenter_0' class='msl-page-content-centerColumn'><div class='row'><div class='col-md-12' id='msl-page-content'><div id='msl-page-misc-nav'><table class='miscTable'><tr><td id='mmpFavoritesDiv'></td><td id='mmpSpacerTD'>&nbsp;</td><td id='mmpResultsNavDiv'></td></tr></table></div><div id='msl-page-content-editable' role='main'><h1 class='searchResultsH1'>Search Results</h1></div></div></div></div></div></div></div></div></div></div><div id='template-footer-wrapper' role='contentinfo' class=''><div id='pageFooter' class='row'><img id='msl-page-footer-logo' class='img-responsive' aria-hidden='true' src='http://mslsrc.mt.gov/images/msl_white.png'><div id='msl-page-footer-content'><p><span class='msl-page-footer-content-span'>1515 E 6th Avenue</span><span class='msl-page-footer-content-span'>Helena, Montana 59620</span></p><p><span class='msl-page-footer-content-span'>Phone: (406) 444-3115</span><span class='msl-page-footer-content-span'>Toll Free: (800) 338-5087</span><span class='msl-page-footer-content-span'>TTY:(406) 444-4799</span><span class='msl-page-footer-content-span'>Email:&nbsp;&nbsp;<a href='http://mslapps.mt.gov/About_the_Library/about_Staff.aspx'>View Directory</a></span></p><p><span class='msl-page-footer-content-span'>HOURS: Monday-Friday 8am - 5pm</span></p><p id='msl-page-footer-copyright'>© 2016 MONTANA STATE LIBRARY ALL RIGHTS RESERVED.</p></div></div></div>").insertBefore($("#top_content"));
    }
    $("#breadcrumb_top_content img").after("<span class='spacerSpan'> /</span>");
    
    //$("#top_content").prepend("<div id='template-page-wrapper' class='mmpCMDStructure'><div class='container'><div class='row'><div class='col-md-2' id='msl-page-nav-content'><div id='msl-nav-wrapper'><div id='msl-nav-mobile-button' class='hidden'><img id='msl-nav-mobile-button-image' src='http://mslsrc.mt.gov/images/icons/topMenuMobile.jpg'></div><div id='msl-print-heading'>Montana State Library</div><a id='msl-nav-logo-link' href='http://montanamemory.org'><img id='msl-nav-logo' class='img-responsive' src='http://mslsrc.mt.gov/images/mmpABR.jpg' aria-hidden='true' alt='Montana State Library Link to Home' aria-flowto='msl-nav-ul-block'></a><div id='msl-nav-mobile-wrapper'><div id='msl-nav-ul-wrapper' class=''><div class='msl-nav-functions-block' aria-hidden='true'><a class='msl-nav-function-expandAll'>Expand All</a> | <a class='msl-nav-function-collapseAll'>Collapse All</a></div><div id='msl-nav-ul-block'><ul id='msl-nav-ul' role='navigation' aria-label='Site Navigation'></ul></div><div class='msl-nav-functions-block' aria-hidden='true'><a class='msl-nav-function-expandAll'>Expand All</a> | <a class='msl-nav-function-collapseAll'>Collapse All</a></div></div></div></div></div><div class='col-md-10' id='msl-content-wrapper'><div id='msl-content' class='container'><div class='row'><div class='col-md-12'><div id='msl-page-home-top-banner-title'><a href='/home'>MONTANA MEMORY PROJECT</a></div><div id='msl-search-div' role='search'><div id='msl-search-bar' class=''>Search: What are you looking for? <span class='glyphicon glyphicon-chevron-right'></span><span class='glyphicon glyphicon-chevron-down hidden'></span></div><div id='msl-search-form' class='container'><div id='msl-search-form-types' class='row'></div><div id='msl-search-form-links-div' role='tablist' aria-label='Search Navigation'><div id='msl-search-form-links'></div></div></div></div></div><div class='row'><div id='MainContent_PageRepeater_mslpagecontentcenter_0' class='msl-page-content-centerColumn'><div class='row'><div class='col-md-12' id='msl-page-content'><div id='msl-page-content-editable' role='main'><h1 class='searchResultsH1'>Search Results</h1></div></div></div></div></div></div></div></div></div></div><div id='template-footer-wrapper' role='contentinfo' class=''><div id='pageFooter' class='row'><img id='msl-page-footer-logo' class='img-responsive' aria-hidden='true' src='http://mslsrc.mt.gov/images/msl_white.png'><div id='msl-page-footer-content'><p><span class='msl-page-footer-content-span'>1515 E 6th Avenue</span><span class='msl-page-footer-content-span'>Helena, Montana 59620</span></p><p><span class='msl-page-footer-content-span'>Phone: (406) 444-3115</span><span class='msl-page-footer-content-span'>Toll Free: (800) 338-5087</span><span class='msl-page-footer-content-span'>TTY:(406) 444-4799</span><span class='msl-page-footer-content-span'>Email:&nbsp;&nbsp;<a href='http://mslapps.mt.gov/About_the_Library/about_Staff.aspx'>View Directory</a></span></p><p><span class='msl-page-footer-content-span'>HOURS: Monday-Friday 8am - 5pm</span></p><p id='msl-page-footer-copyright'>© 2016 MONTANA STATE LIBRARY ALL RIGHTS RESERVED.</p></div></div></div>");
    //if ($("#results_tn_wrapper").length > 0) {
    //    $("#results_tn_wrapper").appendTo("#msl-page-content-editable");
    //}
    //else if($("#idx_wrapper").length > 0)
    //{
    //    $("#idx_wrapper").appendTo("#msl-page-content-editable");
    //}
    //else {
    //    //$("#msl-page-content-editable").html("<div id='itemDetails'></div>");
    //    //$("#itemDetails").addClass("negativeRowPadding");
    //    //$("#breadcrumb_top").appendTo("#itemDetails");
    //    //$("#link_bar").appendTo("#itemDetails");
    //    //$("#image_title").appendTo("#itemDetails");
    //    //$("#title_desc_bar").appendTo("#itemDetails");
    //    //$("#tabs").appendTo("#itemDetails");
    //    //$("#details").appendTo("#itemDetails");
    //}
}


$("a[href='/cdm/']").each(function () {
    $(this).attr("href", "http://montanamemory.org/");
});

$("a[href*='/cdm/landingpage/collection/']").each(function () {
    var newUrl = $(this).attr("href").replace("/cdm/landingpage/collection/", "/cdm/search/collection/");
    $(this).attr("href", newUrl);
});





var mainMenuArray = new Array();
//mainMenuArray[0] = [level1_sort, "level1_name", "level1_link", level1_visible,
//                        [
//                            [level2_sort, "level2_name", "level2_link", level2_visible,],
//                            [level2_sort, "level2_name", "level2_link", level2_visible,
//                                [
//                                    [level3_sort, "level3_name", "level3_link", level3_visible,],
//                                    [level3_sort, "level3_name", "level3_link", level3_visible,
//                                        [
//                                            [level4_sort, "level4_name", "level4_link", level4_visible,],
//                                            [level4_sort, "level4_name", "level4_link", level4_visible,]
//                                        ]
//                                    ]
//                                ]
//                            ]
//                      ]
//];

mainMenuArray[0] = [0, "HOME", "http://montanamemory.org/", 0, true, []];
mainMenuArray[1] = [1, "ARTWORK", "http://montanamemory.org/artwork", 0, true, []];

mainMenuArray[2] = [1, "AUDIO", "http://montanamemory.org/audio", 0, true, []];

mainMenuArray[3] = [2, "PHOTOGRAPHS", "http://montanamemory.org/photographs", 0, true,
                    [
                        [1, "All", "http://montanamemory.org/photographs/all", 0, true, []],
                        [2, "Agriculture & Homesteading", "http://montanamemory.org/photographs/agriculturehomesteading", 0, true, []],
                        [3, "City History", "http://montanamemory.org/photographs/cityhistory", 0, true, []],
                        [4, "County History", "http://montanamemory.org/photographs/countyhistory", 0, true, []],
                        [5, "Military", "http://montanamemory.org/photographs/military", 0, true, []],
                        [6, "Mining", "http://montanamemory.org/photographs/mining", 0, true, []],
                        [7, "Native American", "http://montanamemory.org/photographs/nativeamericans", 0, true, []],
                        [8, "Science & Technology", "http://montanamemory.org/photographs/sciencetechnology", 0, true, []]
                    ]
];

mainMenuArray[4] = [3, "PRINT MATERIALS", "http://montanamemory.org/printmaterials", 0, true,
                [
                    [1, "Books", "http://montanamemory.org/printmaterials/books", 0, true,
					    [
                            [1, "All", "http://montanamemory.org/printmaterials/books/all", 0, true, []],
                            [2, "City History", "http://montanamemory.org/printmaterials/books/cityhistory", 0, true, []],
						    [3, "County History", "http://montanamemory.org/printmaterials/books/countyhistory", 0, true, []],
                            [4, "Mining", "http://montanamemory.org/printmaterials/books/mining", 0, true, []]
					    ]
                    ],
                    [2, "Documents", "http://montanamemory.org/printmaterials/documents", 0, true, [
                        [1, "All", "http://montanamemory.org/printmaterials/documents/all", 0, true, []],
                        [2, "Agriculture & Homesteading", "http://montanamemory.org/printmaterials/documents/agriculturehomesteading", 0, true, []],
                        [3, "City History", "http://montanamemory.org/printmaterials/documents/cityhistory", 0, true, []],
                        [4, "County History", "http://montanamemory.org/printmaterials/documents/countyhistory", 0, true, []],

                        [5, "Government Records", "http://montanamemory.org/printmaterials/documents/governmentrecords", 0, true, []],
                        [6, "Hunting & Conservation", "http://montanamemory.org/printmaterials/documents/huntingconservation", 0, true, []],
                        [7, "Journals & Correspondence", "http://montanamemory.org/printmaterials/documents/journalscorrespondence", 0, true, []],
                        [8, "Military", "http://montanamemory.org/printmaterials/documents/military", 0, true, []],
                        [9, "Native American", "http://montanamemory.org/printmaterials/documents/nativeamericans", 0, true, []],
                        [10, "Science & Technology", "http://montanamemory.org/printmaterials/documents/sciencetechnology", 0, true, []]
                    ]],
                    [4, "Maps", "http://montanamemory.org/printmaterials/maps", 0, true, []],
                    [5, "Newspapers and Periodicals", "http://montanamemory.org/newspapers", 0, true, []],
                    [6, "Yearbooks", "http://montanamemory.org/printmaterials/yearbooks", 0, true, []]

                ]
];

mainMenuArray[5] = [4, "COLLECTIONS", "http://montanamemory.org/collections", 0, true, []];
mainMenuArray[6] = [5, "CONTRIBUTORS", "http://montanamemory.org/contributors", 0, true, []];
mainMenuArray[7] = [6, "EDUCATIONAL RESOURCES", "http://montanamemory.org/educationalresources", 0, true, []];
mainMenuArray[8] = [7, "COLLECTION MAP", "http://montanamemory.org/map", 0, true, []];
mainMenuArray[9] = [8, "INSTRUCTIONAL VIDEOS", "http://montanamemory.org/instructionalvideos", 0, true, []];
mainMenuArray[10] = [9, "PARTNERS", "http://montanamemory.org/partners", 0, true, []];
mainMenuArray[11] = [10, "SEARCH", "http://montanamemory.org/search", 0, true, []];

$(document).ready(function () {
    if ($("#testNavDiv").length > 0) {
        var tableNavString = "<table>";
        var linkName;
        var linkURL;
        var linkVisible;
        var linkLevel;
        for (var i = 0; i < mainMenuArray.length; i++) {

            linkName = mainMenuArray[i][1];
            linkURL = mainMenuArray[i][2];
            linkVisible = mainMenuArray[i][4];
            linkLevel = 1;
            tableNavString += CreateTableNavRow(linkName, linkURL, linkVisible, linkLevel);
            var mainMenuArray1 = mainMenuArray[i][5];
            for (var j = 0; j < mainMenuArray1.length; j++) {
                linkName = mainMenuArray1[j][1];
                linkURL = mainMenuArray1[j][2];
                linkVisible = mainMenuArray1[j][4];
                linkLevel = 2;
                tableNavString += CreateTableNavRow(linkName, linkURL, linkVisible, linkLevel);

                var mainMenuArray2 = mainMenuArray1[j][5];
                for (var k = 0; k < mainMenuArray2.length; k++) {
                    linkName = mainMenuArray2[k][1];
                    linkURL = mainMenuArray2[k][2];
                    linkVisible = mainMenuArray2[k][4];
                    linkLevel = 3;
                    tableNavString += CreateTableNavRow(linkName, linkURL, linkVisible, linkLevel);

                    var mainMenuArray3 = mainMenuArray2[k][5];
                    for (var l = 0; l < mainMenuArray3.length; l++) {
                        linkName = mainMenuArray3[l][1];
                        linkURL = mainMenuArray3[l][2];
                        linkVisible = mainMenuArray3[l][4];
                        linkLevel = 4;
                        tableNavString += CreateTableNavRow(linkName, linkURL, linkVisible, linkLevel);

                        var mainMenuArray4 = mainMenuArray3[l][5];
                        for (var m = 0; m < mainMenuArray4.length; m++) {
                            linkName = mainMenuArray4[m][1];
                            linkURL = mainMenuArray4[m][2];
                            linkVisible = mainMenuArray4[m][4];
                            linkLevel = 5;
                            tableNavString += CreateTableNavRow(linkName, linkURL, linkVisible, linkLevel);

                            var mainMenuArray5 = mainMenuArray4[m][5];
                            for (var n = 0; n < mainMenuArray5.length; n++) {
                                linkName = mainMenuArray5[n][1];
                                linkURL = mainMenuArray5[n][2];
                                linkVisible = mainMenuArray5[n][4];
                                linkLevel = 1;
                                tableNavString += CreateTableNavRow(linkName, linkURL, linkVisible, linkLevel);
                            }

                        }

                    }

                }

            }
        }

        tableNavString += "</table>";
        $("#testNavDiv").html(tableNavString);
    }


});

function CreateTableNavRow(linkName, linkURL, linkVisible, linkLevel) {
    var levelCount = 5;
    var rowString = "<tr>";
    var tdBeginCount = linkLevel - 1;
    for (var i = 0; i < tdBeginCount; i++) {
        rowString += "<td></td>";
    }
    rowString += "<td>" + linkName + "</td>";
    var tdEndCount = levelCount - linkLevel;
    for (var i = 0; i < tdEndCount; i++) {
        rowString += "<td></td>";
    }


    rowString += "<td>" + linkURL + "</td><td>" + linkVisible + "</td><td>";

    rowString += "</tr>";
    return rowString;
}



// MSL Search Script
// Montana State Library
// Stacy Bruhn
// 11/17/2015
// Creates customized search block for all MSL sites

// Array Pattern
//siteSearchArray[0] = [siteURLArray, searchDefaultOpen, [searchTypeArray], [secondarySearchTypeArray]];
var siteSearchArray = [];

siteSearchArray[0] = [["montanamemory.org", "mslsrc.mt.gov/mmptest", "mtmemory.org"], true, ["MMPCollection", "MWDLCollection", "DPLACollection", "ChroniclingAmericaCollection", "WomensHistoryCollection"], []];

var mslSearchFormTypes = document.getElementById("msl-search-form-types");
var mslSearchFormLinks = document.getElementById("msl-search-form-links");
var mslSearchFormSecondaryLinks = document.getElementById("msl-search-form-secondary-links");

for (var i = 0; i < siteSearchArray.length; i++) {
    var currentSite = false;
    var searchUrlArray = new Array();
    searchUrlArray = siteSearchArray[i][0];
    for (var k = 0; k < searchUrlArray.length; k++) {
        if (searchSiteString.indexOf(searchUrlArray[k]) > -1) {
            currentSite = true;
        }
    }
    if (currentSite) {
        if (siteSearchArray[i][1]) {
            $("#msl-search-bar").removeClass("closed");
            $("#msl-search-form").removeClass("hidden");
        }
        var searchTypeArray = new Array();
        searchTypeArray = siteSearchArray[i][2];
        for (var j = 0; j < searchTypeArray.length; j++) {
            var searchTypeDiv = document.createElement("div");
            searchTypeDiv.setAttribute("id", "searchTypeDiv" + searchTypeArray[j]);
            if (j === 0) {
                searchTypeDiv.setAttribute("class", "searchTypeDiv");
                searchTypeDiv.setAttribute("aria-hidden", "false");
            }
            else {
                searchTypeDiv.setAttribute("class", "searchTypeDiv hidden");
                searchTypeDiv.setAttribute("aria-hidden", "true");
            }
            searchTypeDiv.setAttribute("role", "tabpanel");
            searchTypeDiv.setAttribute("aria-labelledby", "searchLink" + searchTypeArray[j]);
            var searchInputsDiv = document.createElement("div");
            searchInputsDiv.setAttribute("class", "searchInputsDiv input-group");

            var searchRelatedLinks = document.createElement("div");
            searchRelatedLinks.setAttribute("class", "searchRelatedLinks");

            searchTypeDiv.appendChild(searchInputsDiv);
            searchTypeDiv.appendChild(searchRelatedLinks);
            mslSearchFormTypes.appendChild(searchTypeDiv);

            eval(searchTypeArray[j] + "(1)");
        }

        var secondarySearchTypeArray = new Array();
        secondarySearchTypeArray = siteSearchArray[i][3];
        for (var k = 0; k < secondarySearchTypeArray.length; k++) {
            if (k === 0) {
                $("#msl-search-form-secondary-links").html("<div id=\"searchAdditionalOptionsDiv\">For more resources:</div>");
            }
            var searchTypeDiv = document.createElement("div");
            searchTypeDiv.setAttribute("id", "searchTypeDiv" + secondarySearchTypeArray[k]);
            searchTypeDiv.setAttribute("class", "searchTypeDiv hidden");

            var searchInputsDiv = document.createElement("div");
            searchInputsDiv.setAttribute("class", "searchInputsDiv input-group");

            var searchRelatedLinks = document.createElement("div");
            searchRelatedLinks.setAttribute("class", "searchRelatedLinks");

            searchTypeDiv.appendChild(searchInputsDiv);
            searchTypeDiv.appendChild(searchRelatedLinks);
            mslSearchFormTypes.appendChild(searchTypeDiv);

            eval(secondarySearchTypeArray[k] + "(2)");
        }
        if ($("#searchAdditionalOptionsDiv").length == 0) {
            $("#msl-search-form-secondary-links").remove();
        }
    }
}





function MMPCollection(searchLinkRanking) {
    var searchName = "MMPCollection";

    var searchIn = false;
    if ($("h1.searchResultsHeading").length > 0) {
        var titleHeading = $("h1.searchResultsHeading").html();
        if (titleHeading.indexOf("You've searched:") > -1 || titleHeading.indexOf("Browsing items in:") > -1) {
            searchIn = true;
        }
    }
    
    if (searchIn == true) {
        var MMPSearchInDiv = document.createElement("div");
        MMPSearchInDiv.setAttribute("id", "MMPSearchInDiv");
        var MMPSearchInCheckBox = document.createElement("input");
        MMPSearchInCheckBox.setAttribute("id", "MMPSearchInCheckBox");
        MMPSearchInCheckBox.setAttribute("class", "searchInCheckBox");
        MMPSearchInCheckBox.setAttribute("type", "checkbox");
        MMPSearchInDiv.appendChild(MMPSearchInCheckBox);
        var MMPSearchInTextNode = document.createTextNode(" Search Within Results");
        MMPSearchInDiv.appendChild(MMPSearchInTextNode);
        searchInputsDiv.appendChild(MMPSearchInDiv);
    }

    var MMPTextBox = document.createElement("input");
    MMPTextBox.setAttribute("id", "MMPCollectionTextBox");
    MMPTextBox.setAttribute("type", "text");
    MMPTextBox.setAttribute("class", "form-control siteSearchInput");
    MMPTextBox.setAttribute("placeholder", "Search Montana Memory Project…");
    MMPTextBox.setAttribute("data-value", "MMPSearchButton");
    searchInputsDiv.appendChild(MMPTextBox);

    var MMPSiteSearchButtonSpan = document.createElement("span");
    MMPSiteSearchButtonSpan.setAttribute("class", "input-group-btn");
    searchInputsDiv.appendChild(MMPSiteSearchButtonSpan);

    var MMPSearchButton = document.createElement("input");
    MMPSearchButton.setAttribute("id", "MMPSearchButton");
    MMPSearchButton.setAttribute("type", "button");
    MMPSearchButton.setAttribute("class", "btn btn-default");
    MMPSearchButton.setAttribute("value", "Search");
    MMPSiteSearchButtonSpan.appendChild(MMPSearchButton);

    var relatedLink1 = document.createElement("a");
    relatedLink1.setAttribute("target", "_blank");
    relatedLink1.setAttribute("href", "http://montanamemory.org/search");

    relatedLink1.innerHTML = "Advanced Search";
    searchRelatedLinks.appendChild(relatedLink1);


    var searchLink = document.createElement("div");
    searchLink.setAttribute("id", "searchLink" + searchName);
    searchLink.setAttribute("role", "tab");
    searchLink.setAttribute("aria-controls", "searchTypeDiv" + searchName);
    searchLink.setAttribute("data-toggle", "tooltip");
    searchLink.setAttribute("data-placement", "bottom");
    //searchLink.setAttribute("title", "Temporary Filler Text to describe the Montana Memory Project");

    if (j === 0 && searchLinkRanking == 1) {
        searchLink.setAttribute("class", "searchLink selected");
        searchLink.setAttribute("aria-selected", "true");
    }
    else {
        searchLink.setAttribute("class", "searchLink");
        searchLink.setAttribute("aria-selected", "false");
    }
    searchLink.innerHTML = "Montana Memory Project";
    searchLink.setAttribute("aria-label", "Montana Memory Project");
    if (searchLinkRanking == 1) {
        mslSearchFormLinks.appendChild(searchLink);
    }
    else if (searchLinkRanking == 2) {
        mslSearchFormSecondaryLinks.appendChild(searchLink);
    }

}


function DPLACollection(searchLinkRanking) {
    var searchName = "DPLACollection";

    var DPLATextBox = document.createElement("input");
    DPLATextBox.setAttribute("id", "DPLATextBox");
    DPLATextBox.setAttribute("type", "text");
    DPLATextBox.setAttribute("class", "form-control siteSearchInput");
    DPLATextBox.setAttribute("placeholder", "Search the Digital Public Library of America…");
    DPLATextBox.setAttribute("data-value", "DPLASearchButton");
    searchInputsDiv.appendChild(DPLATextBox);

    var DPLACollectionSearchButtonSpan = document.createElement("span");
    DPLACollectionSearchButtonSpan.setAttribute("class", "input-group-btn");
    searchInputsDiv.appendChild(DPLACollectionSearchButtonSpan);

    var DPLASearchButton = document.createElement("input");
    DPLASearchButton.setAttribute("id", "DPLASearchButton");
    DPLASearchButton.setAttribute("type", "button");
    DPLASearchButton.setAttribute("class", "btn btn-default");
    DPLASearchButton.setAttribute("value", "Search");
    DPLACollectionSearchButtonSpan.appendChild(DPLASearchButton);

    var relatedLink1 = document.createElement("a");
    relatedLink1.setAttribute("target", "_blank");
    relatedLink1.setAttribute("href", "http://dp.la/");
    relatedLink1.innerHTML = "Digital Public Library of America Home Page";
    searchRelatedLinks.appendChild(relatedLink1);

    var searchLink = document.createElement("div");
    searchLink.setAttribute("id", "searchLink" + searchName);
    searchLink.setAttribute("role", "tab");
    searchLink.setAttribute("aria-controls", "searchTypeDiv" + searchName);
    if (j === 0 && searchLinkRanking == 1) {
        searchLink.setAttribute("class", "searchLink selected");
        searchLink.setAttribute("aria-selected", "true");
    }
    else {
        searchLink.setAttribute("class", "searchLink");
        searchLink.setAttribute("aria-selected", "false");
    }
    searchLink.innerHTML = "Digital Public Library of America";
    searchLink.setAttribute("aria-label", "Digital Public Library of America");
    if (searchLinkRanking == 1) {
        mslSearchFormLinks.appendChild(searchLink);
    }
    else if (searchLinkRanking == 2) {
        mslSearchFormSecondaryLinks.appendChild(searchLink);
    }

}


function MWDLCollection(searchLinkRanking) {
    var searchName = "MWDLCollection";

    var MWDLTextBox = document.createElement("input");
    MWDLTextBox.setAttribute("id", "MWDLTextBox");
    MWDLTextBox.setAttribute("type", "text");
    MWDLTextBox.setAttribute("class", "form-control siteSearchInput");
    MWDLTextBox.setAttribute("placeholder", "Search the Mountain West Digital Library…");
    MWDLTextBox.setAttribute("data-value", "MWDLSearchButton");
    searchInputsDiv.appendChild(MWDLTextBox);

    var MWDLCollectionSearchButtonSpan = document.createElement("span");
    MWDLCollectionSearchButtonSpan.setAttribute("class", "input-group-btn");
    searchInputsDiv.appendChild(MWDLCollectionSearchButtonSpan);

    var MWDLSearchButton = document.createElement("input");
    MWDLSearchButton.setAttribute("id", "MWDLSearchButton");
    MWDLSearchButton.setAttribute("type", "button");
    MWDLSearchButton.setAttribute("class", "btn btn-default");
    MWDLSearchButton.setAttribute("value", "Search");
    MWDLCollectionSearchButtonSpan.appendChild(MWDLSearchButton);

    var relatedLink1 = document.createElement("a");
    relatedLink1.setAttribute("target", "_blank");
    relatedLink1.setAttribute("href", "http://www.mwdl.org/");
    relatedLink1.innerHTML = "Mountain West Digital Library Home Page";
    searchRelatedLinks.appendChild(relatedLink1);

    var searchLink = document.createElement("div");
    searchLink.setAttribute("id", "searchLink" + searchName);
    searchLink.setAttribute("role", "tab");
    searchLink.setAttribute("aria-controls", "searchTypeDiv" + searchName);
    if (j === 0 && searchLinkRanking == 1) {
        searchLink.setAttribute("class", "searchLink selected");
        searchLink.setAttribute("aria-selected", "true");
    }
    else {
        searchLink.setAttribute("class", "searchLink");
        searchLink.setAttribute("aria-selected", "false");
    }
    searchLink.innerHTML = "Mountain West Digital Library";
    searchLink.setAttribute("aria-label", "Mountain West Digital Library");
    if (searchLinkRanking == 1) {
        mslSearchFormLinks.appendChild(searchLink);
    }
    else if (searchLinkRanking == 2) {
        mslSearchFormSecondaryLinks.appendChild(searchLink);
    }

}


function ChroniclingAmericaCollection(searchLinkRanking) {
    var searchName = "ChroniclingAmericaCollection";

    var ChroniclingAmericaTextBox = document.createElement("input");
    ChroniclingAmericaTextBox.setAttribute("id", "ChroniclingAmericaTextBox");
    ChroniclingAmericaTextBox.setAttribute("type", "text");
    ChroniclingAmericaTextBox.setAttribute("class", "form-control siteSearchInput");
    ChroniclingAmericaTextBox.setAttribute("placeholder", "Search Chronicling America…");
    ChroniclingAmericaTextBox.setAttribute("data-value", "ChroniclingAmericaSearchButton");
    searchInputsDiv.appendChild(ChroniclingAmericaTextBox);

    var ChroniclingAmericaCollectionSearchButtonSpan = document.createElement("span");
    ChroniclingAmericaCollectionSearchButtonSpan.setAttribute("class", "input-group-btn");
    searchInputsDiv.appendChild(ChroniclingAmericaCollectionSearchButtonSpan);

    var ChroniclingAmericaSearchButton = document.createElement("input");
    ChroniclingAmericaSearchButton.setAttribute("id", "ChroniclingAmericaSearchButton");
    ChroniclingAmericaSearchButton.setAttribute("type", "button");
    ChroniclingAmericaSearchButton.setAttribute("class", "btn btn-default");
    ChroniclingAmericaSearchButton.setAttribute("value", "Search");
    ChroniclingAmericaCollectionSearchButtonSpan.appendChild(ChroniclingAmericaSearchButton);

    var relatedLink1 = document.createElement("a");
    relatedLink1.setAttribute("target", "_blank");
    relatedLink1.setAttribute("href", "http://chroniclingamerica.loc.gov/");
    relatedLink1.innerHTML = "Chronicling America Home Page";
    searchRelatedLinks.appendChild(relatedLink1);

    var relatedLink2 = document.createElement("a");
    relatedLink2.setAttribute("target", "_blank");
    relatedLink2.setAttribute("href", "http://chroniclingamerica.loc.gov/newspapers/?state=Montana&ethnicity=&language=");
    relatedLink2.innerHTML = "Montana Newspapers in Chronicling America";
    searchRelatedLinks.appendChild(relatedLink2);


    var searchLink = document.createElement("div");
    searchLink.setAttribute("id", "searchLink" + searchName);
    searchLink.setAttribute("role", "tab");
    searchLink.setAttribute("aria-controls", "searchTypeDiv" + searchName);
    if (j === 0 && searchLinkRanking == 1) {
        searchLink.setAttribute("class", "searchLink selected");
        searchLink.setAttribute("aria-selected", "true");
    }
    else {
        searchLink.setAttribute("class", "searchLink");
        searchLink.setAttribute("aria-selected", "false");
    }
    searchLink.innerHTML = "Chronicling America";
    searchLink.setAttribute("aria-label", "Chronicling America");
    if (searchLinkRanking == 1) {
        mslSearchFormLinks.appendChild(searchLink);
    }
    else if (searchLinkRanking == 2) {
        mslSearchFormSecondaryLinks.appendChild(searchLink);
    }

}


function WomensHistoryCollection(searchLinkRanking) {
    var searchName = "WomensHistoryCollection";

    var WomensHistoryTextBox = document.createElement("input");
    WomensHistoryTextBox.setAttribute("id", "WomensHistoryTextBox");
    WomensHistoryTextBox.setAttribute("type", "text");
    WomensHistoryTextBox.setAttribute("class", "form-control siteSearchInput");
    WomensHistoryTextBox.setAttribute("placeholder", "Search Women's History Matters…");
    WomensHistoryTextBox.setAttribute("data-value", "WomensHistorySearchButton");
    searchInputsDiv.appendChild(WomensHistoryTextBox);

    var WomensHistoryCollectionSearchButtonSpan = document.createElement("span");
    WomensHistoryCollectionSearchButtonSpan.setAttribute("class", "input-group-btn");
    searchInputsDiv.appendChild(WomensHistoryCollectionSearchButtonSpan);

    var WomensHistorySearchButton = document.createElement("input");
    WomensHistorySearchButton.setAttribute("id", "WomensHistorySearchButton");
    WomensHistorySearchButton.setAttribute("type", "button");
    WomensHistorySearchButton.setAttribute("class", "btn btn-default");
    WomensHistorySearchButton.setAttribute("value", "Search");
    WomensHistoryCollectionSearchButtonSpan.appendChild(WomensHistorySearchButton);

    var relatedLink1 = document.createElement("a");
    relatedLink1.setAttribute("target", "_blank");
    relatedLink1.setAttribute("href", "http://montanawomenshistory.org/");
    relatedLink1.innerHTML = "Women's History Matters Home Page";
    searchRelatedLinks.appendChild(relatedLink1);


    var searchLink = document.createElement("div");
    searchLink.setAttribute("id", "searchLink" + searchName);
    searchLink.setAttribute("role", "tab");
    searchLink.setAttribute("aria-controls", "searchTypeDiv" + searchName);
    if (j === 0 && searchLinkRanking == 1) {
        searchLink.setAttribute("class", "searchLink selected");
        searchLink.setAttribute("aria-selected", "true");
    }
    else {
        searchLink.setAttribute("class", "searchLink");
        searchLink.setAttribute("aria-selected", "false");
    }
    searchLink.innerHTML = "Women's History Matters";
    searchLink.setAttribute("aria-label", "Women's History Matters");
    if (searchLinkRanking == 1) {
        mslSearchFormLinks.appendChild(searchLink);
    }
    else if (searchLinkRanking == 2) {
        mslSearchFormSecondaryLinks.appendChild(searchLink);
    }

}

$('.siteSearchInput').keypress(function (e) {
    if (e.which == 13) {
        var relatedButton = $(this).attr("data-value");
        $("#" + relatedButton).click();

        return false;    //<---- Add this line
    }
});

$(".searchLink").bind("click", function () {
    var searchName = $(this).attr("id").replace("searchLink", "");
    $(".searchLink").removeClass("selected");
    $(".searchLink").attr("aria-selected", "false");
    $(".searchTypeDiv").addClass("hidden");
    $(".searchTypeDiv").attr("aria-hidden", "true");
    $("#searchLink" + searchName).addClass("selected");
    $("#searchLink" + searchName).attr("aria-selected", "true");
    $("#searchTypeDiv" + searchName).removeClass("hidden");
    $("#searchTypeDiv" + searchName).attr("aria-hidden", "false");
    $("#searchTypeDiv" + searchName + " .siteSearchInput").focus();
    console.log(searchName);
});



$("#MMPSearchButton").on("click", function () {
    
    var MMPTextBoxString = $("#MMPCollectionTextBox").val();
    var coreUrl = "";
    if ($("#mmpCollectionField").length > 0) {
        var mmpCollectionFieldValue = $("#mmpCollectionField").val();
        if (mmpCollectionFieldValue.length > 0) {
            coreUrl = "http://mtmemory.org/cdm/search/collection/" + mmpCollectionFieldValue + "/searchterm/" + MMPTextBoxString + "/field/all/mode/exact/conn/and/order/title";
        }
    }
    if (coreUrl.length == 0) {
        if ($("#MMPSearchInCheckBox").prop("checked")) {
            var searchtermIndex = 0;
            var fieldIndex = 0;
            var modeIndex = 0;
            var connIndex = 0;
            var orderIndex = 0;
            var newSearchSiteString = searchSiteString;
            if (newSearchSiteString.charAt(newSearchSiteString.length - 1) == "/") {
                newSearchSiteString = newSearchSiteString.slice(0, -1)
            }
            var splitURLArray = newSearchSiteString.split("/");
            for (var i = 0; i < splitURLArray.length; i++) {
                if (splitURLArray[i] == "searchterm") {
                    searchtermIndex = i + 1;
                }
                else if (splitURLArray[i] == "field") {
                    fieldIndex = i + 1;
                }
                else if (splitURLArray[i] == "mode") {
                    modeIndex = i + 1;
                }
                else if (splitURLArray[i] == "conn") {
                    connIndex = i + 1;
                }
                else if (splitURLArray[i] == "order") {
                    orderIndex = i + 1;
                }
            }
            for (var j = 0; j < splitURLArray.length; j++) {
                if (j == searchtermIndex && searchtermIndex != 0) {
                    coreUrl += splitURLArray[j] + "!" + MMPTextBoxString + "/";
                }
                else if (j == fieldIndex && fieldIndex != 0) {
                    coreUrl += splitURLArray[j] + "!all" + "/";
                }
                else if (j == modeIndex & modeIndex != 0) {
                    coreUrl += splitURLArray[j] + "!exact" + "/";
                }
                else if (j == connIndex & connIndex != 0) {
                    coreUrl += splitURLArray[j] + "!and" + "/";
                }
                else {
                    coreUrl += splitURLArray[j] + "/";
                }
            }
            if (coreUrl.indexOf("/searchterm/") == -1) {
                coreUrl += "searchterm/" + MMPTextBoxString + "/field/all/mode/exact/conn/and/";
            }
            else {
                if (coreUrl.indexOf("/field/") == -1) {
                    coreUrl += "field/all!all/";
                }
                if (coreUrl.indexOf("/mode/") == -1) {
                    coreUrl += "mode/exact!exact/";
                }
                if (coreUrl.indexOf("/conn/") == -1) {
                    coreUrl += "conn/and!and/";
                }
            }
            if (coreUrl.indexOf("/order/") == -1) {
                coreUrl += "order/title/";
            }

        }
        else {
            coreUrl = "http://mtmemory.org/cdm/search/searchterm/" + MMPTextBoxString + "/order/title";
        }
    }
    window.open(coreUrl, '_blank');

});

$("#DPLASearchButton").on("click", function () {
    var DPLATextBoxString = $("#DPLATextBox").val();
    var coreUrl = "http://dp.la/search?utf8=%E2%9C%93&q=" + DPLATextBoxString;
    window.open(coreUrl, '_blank');
});


$("#MWDLSearchButton").on("click", function () {
    var MWDLTextBoxString = $("#MWDLTextBox").val();
    var coreUrl = "http://utah-primoprod.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?fn=search&ct=search&initialSearch=true&mode=Basic&tab=default_tab&indx=1&dum=true&srt=rank&vid=MWDL&frbg=&vl%28freeText0%29=" + MWDLTextBoxString + "&scp.scps=scope%3A%28mw%29&vl%28334075669UI1%29=all_items&vl%281UI0%29=contains";
    window.open(coreUrl, '_blank');
});

$("#ChroniclingAmericaSearchButton").on("click", function () {
    var ChroniclingAmericaTextBoxString = $("#ChroniclingAmericaTextBox").val();
    var coreUrl = "http://chroniclingamerica.loc.gov/search/pages/results/?state=Montana&date1=1836&date2=1922&proxtext=" + ChroniclingAmericaTextBoxString + "&x=15&y=3&dateFilterType=yearRange&rows=20&searchType=basic";
    window.open(coreUrl, '_blank');
});

$("#WomensHistorySearchButton").on("click", function () {
    var WomensHistoryTextBoxString = $("#WomensHistoryTextBox").val();
    var coreUrl = "http://montanawomenshistory.org/?s=" + WomensHistoryTextBoxString + "&submit=Search";
    window.open(coreUrl, '_blank');
});


$("#msl-search-bar").bind("click", function () {
    if ($("#msl-page-title").length > 0) {
        var CollectionTitleValue = $("#msl-page-title").html();
        var MMPCollectionTextBoxValue = "Search Montana Memory Project: " + CollectionTitleValue + "..."
        $("#MMPCollectionTextBox").attr("placeholder", MMPCollectionTextBoxValue);
    }

    $("#msl-search-form").toggleClass("hidden");
    if ($("#msl-search-form").attr("class").indexOf("hidden") > -1) {
        $("#msl-search-bar .glyphicon.glyphicon-chevron-right").removeClass("hidden");
        $("#msl-search-bar .glyphicon.glyphicon-chevron-down").addClass("hidden");
        $("#msl-search-bar").addClass("closed");
    }
    else {
        $("#msl-search-bar .glyphicon.glyphicon-chevron-right").addClass("hidden");
        $("#msl-search-bar .glyphicon.glyphicon-chevron-down").removeClass("hidden");
        $("#msl-search-bar").removeClass("closed");
    }
    $("#uqueryTextBox").focus();
});


if ($("#MainContent_PageRepeater_SearchDefaultHiddenField_0").val() == "true") {
    $("#msl-search-bar").removeClass("closed");
    $("#msl-search-form").removeClass("hidden");
}

if (searchSiteString.toLowerCase().indexOf("intranet") > -1) {
    $("#msl-search-bar").addClass("closed");
    $("#msl-search-form").addClass("hidden");

}








// MMP Photo Strip
var siteLocation = window.location.href;
if (siteLocation.indexOf("montanamemory.org") > -1) {
    $("#msl-nav-logo").attr("src", "http://mslsrc.mt.gov/images/mmpABR.jpg");
    $("#msl-nav-logo-link").attr("href", "http://montanamemory.org");
    $("#template-header-wrapper").remove();
    $("#template-footer").remove();
}

if ($("#template-header-wrapper").length == 0) {
    $("#msl-page-wrapper").addClass("noStateTemplate");
}

// Left navigation
// Loop through array in Main Menu javascript to create site-wide navigation
// Script creates label, expanding panels, and icons
var msl_nav_ul = document.createElement("ul");
msl_nav_ul.setAttribute("id", "msl-nav-ul");
msl_nav_ul.setAttribute("role", "navigation");
msl_nav_ul.setAttribute("aria-label", "Site Navigation");

// Level 1
for (var i = 0; i < mainMenuArray.length; i++) {
    var li1 = document.createElement("li");
    if (mainMenuArray[i][4]) {
        li1.setAttribute("class", "home");
    }
    else {
        li1.setAttribute("class", "home hidden");
    }
    var li2Array = mainMenuArray[i][5];
    var li1LinkDiv = document.createElement("div");
    if (mainMenuArray[i][4]) {
        li1LinkDiv.setAttribute("class", "navLinkDiv level1");
    }
    else {
        li1LinkDiv.setAttribute("class", "navLinkDiv level1 hidden");
    }
    var li1Link = document.createElement("a");
    li1Link.setAttribute("href", mainMenuArray[i][2].toLowerCase());
    li1Link.setAttribute("data-value", mainMenuArray[i][2]);
    li1Link.innerHTML = mainMenuArray[i][1];
    li1LinkDiv.appendChild(li1Link);
    li1.appendChild(li1LinkDiv);

    var li1GlyphiconDiv = document.createElement("div");
    li1GlyphiconDiv.setAttribute("class", "navGlyphiconDiv");
    var li1Expander = document.createElement("span");
    li1Expander.setAttribute("class", "glyphicon glyphicon-chevron-right");
    li1GlyphiconDiv.appendChild(li1Expander);
    var li1Minimizer = document.createElement("span");
    li1Minimizer.setAttribute("class", "glyphicon glyphicon-chevron-down hidden");
    li1GlyphiconDiv.appendChild(li1Minimizer);
    li1.appendChild(li1GlyphiconDiv);

    // Level 2
    if (li2Array.length > 0) {
        if (mainMenuArray[i][4]) {
            li1.setAttribute("class", "expandableLI topLevelNav home");
        }
        else {
            li1.setAttribute("class", "expandableLI topLevelNav home hidden");
        }
        var li1UL = document.createElement("ul");
        li1UL.setAttribute("class", "hidden");
        for (var j = 0; j < li2Array.length; j++) {

            var li2 = document.createElement("li");
            var li3Array = li2Array[j][5];
            var li2LinkDiv = document.createElement("div");
            if (li2Array[j][4]) {
                li2LinkDiv.setAttribute("class", "navLinkDiv level2");
            }
            else {
                li2LinkDiv.setAttribute("class", "navLinkDiv level2 hidden");
            }
            var li2Link = document.createElement("a");
            li2Link.setAttribute("href", li2Array[j][2].toLowerCase());
            li2Link.setAttribute("data-value", li2Array[j][2]);
            li2Link.innerHTML = li2Array[j][1];
            li2LinkDiv.appendChild(li2Link);
            li2.appendChild(li2LinkDiv);
            var li2GlyphiconDiv = document.createElement("div");
            li2GlyphiconDiv.setAttribute("class", "navGlyphiconDiv");
            var li2Expander = document.createElement("span");
            li2Expander.setAttribute("class", "glyphicon glyphicon-chevron-right");
            li2GlyphiconDiv.appendChild(li2Expander);
            var li2Minimizer = document.createElement("span");
            li2Minimizer.setAttribute("class", "glyphicon glyphicon-chevron-down hidden");
            li2GlyphiconDiv.appendChild(li2Minimizer);
            li2.appendChild(li2GlyphiconDiv);

            // Level 3
            if (li3Array.length > 0) {
                if (li2Array[j][4]) {
                    li2.setAttribute("class", "expandableLI");
                }
                else {
                    li2.setAttribute("class", "expandableLI hidden");
                }
                var li2UL = document.createElement("ul");
                li2UL.setAttribute("class", "hidden");
                for (var k = 0; k < li3Array.length; k++) {
                    var li3 = document.createElement("li");
                    var li4Array = li3Array[k][5];
                    var li3LinkDiv = document.createElement("div");
                    if (li3Array[k][4]) {
                        li3LinkDiv.setAttribute("class", "navLinkDiv level3");
                    }
                    else {
                        li3LinkDiv.setAttribute("class", "navLinkDiv level3 hidden");
                    }
                    var li3Link = document.createElement("a");
                    li3Link.setAttribute("href", li3Array[k][2].toLowerCase());
                    li3Link.setAttribute("data-value", li3Array[k][2]);
                    li3Link.innerHTML = li3Array[k][1];
                    li3LinkDiv.appendChild(li3Link);
                    li3.appendChild(li3LinkDiv);
                    var li3GlyphiconDiv = document.createElement("div");
                    li3GlyphiconDiv.setAttribute("class", "navGlyphiconDiv");
                    var li3Expander = document.createElement("span");
                    li3Expander.setAttribute("class", "glyphicon glyphicon-chevron-right");
                    li3GlyphiconDiv.appendChild(li3Expander);
                    var li3Minimizer = document.createElement("span");
                    li3Minimizer.setAttribute("class", "glyphicon glyphicon-chevron-down hidden");
                    li3GlyphiconDiv.appendChild(li3Minimizer);
                    li3.appendChild(li3GlyphiconDiv);

                    // Level 4
                    if (li4Array.length > 0) {
                        if (li3Array[k][4]) {
                            li3.setAttribute("class", "expandableLI");
                        }
                        else {
                            li3.setAttribute("class", "expandableLI hidden");
                        }

                        var li3UL = document.createElement("ul");
                        li3UL.setAttribute("class", "hidden");
                        for (var m = 0; m < li4Array.length; m++) {
                            var li4 = document.createElement("li");
                            var li5Array = li4Array[m][5];
                            var li4LinkDiv = document.createElement("div");
                            if (li4Array[m][4]) {
                                li4LinkDiv.setAttribute("class", "navLinkDiv level4");
                            }
                            else {
                                li4LinkDiv.setAttribute("class", "navLinkDiv level4 hidden");
                            }
                            var li4Link = document.createElement("a");
                            li4Link.setAttribute("href", li4Array[m][2].toLowerCase());
                            li4Link.setAttribute("data-value", li4Array[m][2]);
                            li4Link.innerHTML = li4Array[m][1];
                            li4LinkDiv.appendChild(li4Link);
                            li4.appendChild(li4LinkDiv);
                            var li4GlyphiconDiv = document.createElement("div");
                            li4GlyphiconDiv.setAttribute("class", "navGlyphiconDiv");
                            var li4Expander = document.createElement("span");
                            li4Expander.setAttribute("class", "glyphicon glyphicon-chevron-right");
                            li4GlyphiconDiv.appendChild(li4Expander);
                            var li4Minimizer = document.createElement("span");
                            li4Minimizer.setAttribute("class", "glyphicon glyphicon-chevron-down hidden");
                            li4GlyphiconDiv.appendChild(li4Minimizer);
                            li4.appendChild(li4GlyphiconDiv);

                            // Level 5
                            if (li5Array.length > 0) {
                                if (li4Array[m][4]) {
                                    li4.setAttribute("class", "expandableLI");
                                }
                                else {
                                    li4.setAttribute("class", "expandableLI hidden");
                                }
                                var li4UL = document.createElement("ul");
                                li4UL.setAttribute("class", "hidden");
                                for (var n = 0; n < li5Array.length; n++) {
                                    var li5 = document.createElement("li");
                                    var li5LinkDiv = document.createElement("div");
                                    if (li5Array[n][4]) {
                                        li5LinkDiv.setAttribute("class", "navLinkDiv level5");
                                    }
                                    else {
                                        li5LinkDiv.setAttribute("class", "navLinkDiv level5 hidden");
                                    }
                                    var li5Link = document.createElement("a");
                                    li5Link.setAttribute("href", li5Array[n][2].toLowerCase());
                                    li5Link.setAttribute("data-value", li5Array[n][2]);
                                    li5Link.innerHTML = li5Array[n][1];
                                    li5LinkDiv.appendChild(li5Link);
                                    li5.appendChild(li5LinkDiv);
                                    var li5GlyphiconDiv = document.createElement("div");
                                    li5GlyphiconDiv.setAttribute("class", "navGlyphiconDiv");
                                    var li5Expander = document.createElement("span");
                                    li5Expander.setAttribute("class", "glyphicon glyphicon-chevron-right");
                                    li5GlyphiconDiv.appendChild(li5Expander);
                                    var li5Minimizer = document.createElement("span");
                                    li5Minimizer.setAttribute("class", "glyphicon glyphicon-chevron-down hidden");
                                    li5GlyphiconDiv.appendChild(li5Minimizer);
                                    li5.appendChild(li5GlyphiconDiv);
                                    li5.setAttribute("class", "staticLI");
                                    li4UL.appendChild(li5);
                                }
                                li4.appendChild(li4UL);
                            }
                            else {
                                li4.setAttribute("class", "staticLI");
                            }
                            li3UL.appendChild(li4);
                        }
                        li3.appendChild(li3UL);
                    }
                    else {
                        li3.setAttribute("class", "staticLI");
                    }
                    li2UL.appendChild(li3);
                }
                li2.appendChild(li2UL);
            }
            else {
                li2.setAttribute("class", "staticLI");
            }
            li1UL.appendChild(li2);
        }
        li1.appendChild(li1UL);
    }
    else {
        li1.setAttribute("class", "staticLI");
    }

    msl_nav_ul.appendChild(li1);
}

// Append navigation structure to existing div
var msl_nav_ul_block = document.getElementById("msl-nav-ul-block");
msl_nav_ul_block.appendChild(msl_nav_ul);

// Bind element click functionality
$(".expandableLI .glyphicon-chevron-right").bind("click", function () {
    affixWidth();
    $(this).addClass("hidden");
    $(this).siblings(".glyphicon-chevron-down").removeClass("hidden");
    $(this).parent().siblings("ul").removeClass("hidden");
});

$(".expandableLI .glyphicon-chevron-down").bind("click", function () {
    affixWidth();
    $(this).addClass("hidden");
    $(this).siblings(".glyphicon-chevron-right").removeClass("hidden");
    $(this).parent().siblings("ul").addClass("hidden");
});

$(".msl-nav-function-expandAll").bind("click", function () {
    $("#msl-nav-ul").find(".glyphicon-chevron-right").click();
});

$(".msl-nav-function-collapseAll").bind("click", function () {
    $("#msl-nav-ul").find(".glyphicon-chevron-down").click();
});


// Add current page highlighting to the menu where applicable
var siteString = window.location.href.toLowerCase().replace("/home/", "/").replace(".aspx", "").split('?')[0];

// Site string matches existing link
$(".navLinkDiv a").each(function () {
    var href = $(this).attr("href").replace(".aspx", "");
    if (siteString == href || $(this).html() == "SEARCH") {
        $(this).parent().parent().addClass("currentPage");
        $(this).parentsUntil("#msl-nav-ul", ".expandableLI").each(function () {
            $(this).addClass("currentPage");
            $(this).children(".navGlyphiconDiv").children(".glyphicon-chevron-right").click();
        });
    }
});

// Site string does not match existing link, find the closest match
// Hidden elements are included
if ($(".currentPage").length === 0) {
    var folderPathArray = new Array();
    $(".navLinkDiv a").each(function () {
        var folderValue = $(this).attr("data-value");
        if (folderValue !== "") {
            var tempArray = new Array();
            tempArray.push(folderValue);
            tempArray.push(folderValue.length);
            folderPathArray.push(tempArray);
        }
    });

    folderPathArray = folderPathArray.sort(function (a, b) {
        return b[1] > a[1];
    });

    // Loop through the individual folders in the site string to find a match
    var splitArray = siteString.split("/");
    var loopingString = siteString.toLowerCase();
    for (var i = 0; i < splitArray.length; i++) {
        for (var j = 0; j < folderPathArray.length; j++) {
            if (loopingString == folderPathArray[j][0].toLowerCase() || (loopingString + "/") == folderPathArray[j][0].toLowerCase()) {
                $(".navLinkDiv a[data-value='" + folderPathArray[j][0] + "']").each(function () {
                    $(this).parent().parent().addClass("currentPage");
                    $(this).parentsUntil("#msl-nav-ul", ".expandableLI").each(function () {
                        $(this).addClass("currentPageAncestor");
                        $(this).children(".navGlyphiconDiv").children(".glyphicon-chevron-right").click();
                    });
                });
                break;
            }
        }
        var lastIndex = loopingString.lastIndexOf("/");
        loopingString = loopingString.substring(0, lastIndex);
    }
}


// Breadcrumbs
// Utilize the previously calculated current page to set the breadcrumbs
$("li.currentPage > .navLinkDiv a, li.currentPageAncestor > .navLinkDiv a").each(function () {
    var linkHTML = $(this).html();
    if (linkHTML == "AppPages") {
    }
    else {
        var breadcrumbLI = document.createElement("li");
        if ($(this).attr("href") == siteString) {
            breadcrumbLI.setAttribute("class", "breadcrumbCurrentPage");
            breadcrumbLI.innerHTML = toTitleCase($(this).html());
        }
        else {
            var breadcrumbLink = document.createElement("a");
            breadcrumbLink.setAttribute("href", $(this).attr("href"));
            breadcrumbLink.innerHTML = toTitleCase($(this).html());
            breadcrumbLI.appendChild(breadcrumbLink);
        }
        $("#msl-page-content-breadcrumb").append(breadcrumbLI);
    }
});

$("#msl-page-content-breadcrumb li a").first().not(".breadcrumbCurentPage").html("Home");

if ($(".breadcrumbCurrentPage").length === 0) {
    var breadcrumbLI = document.createElement("li");
    breadcrumbLI.setAttribute("class", "breadcrumbCurrentPage");
    var h1Heading = toTitleCase($("#msl-page-content-editable h1").first().html());
    var h2Heading = toTitleCase($("#msl-page-content-editable h2").first().html());
    if ($("#msl-page-content-editable h2").length > 0) {
        breadcrumbLI.innerHTML = h1Heading + " - " + h2Heading;
    }
    else {
        breadcrumbLI.innerHTML = h1Heading;
    }
    $("#msl-page-content-breadcrumb").append(breadcrumbLI);
}

if ($("#msl-page-content-breadcrumb li a").html() != "Home") {
    $("#msl-page-content-breadcrumb").prepend("<li><a href=\"" + $("#msl-page-home-top-banner-title a").attr("href") + "\">Home</a></li>");
}

// Set the text size onclick event; individually controlled to assure appropriate resizing
$(".textSizeLink").bind("click", function () {
    var size = $(this).attr("class").split(' ')[0].replace("textResizerLink", "");
    $("#msl-search-bar").removeClass("textResizer75");
    $("#msl-search-bar").removeClass("textResizer100");
    $("#msl-search-bar").removeClass("textResizer125");
    $("#msl-search-bar").removeClass("textResizer150");
    $("#msl-search-bar").addClass("textResizer" + size);
    $("#msl-search-form").removeClass("textResizer75");
    $("#msl-search-form").removeClass("textResizer100");
    $("#msl-search-form").removeClass("textResizer125");
    $("#msl-search-form").removeClass("textResizer150");
    $("#msl-search-form").addClass("textResizer" + size);
    $("#msl-content").removeClass("textResizer75");
    $("#msl-content").removeClass("textResizer100");
    $("#msl-content").removeClass("textResizer125");
    $("#msl-content").removeClass("textResizer150");
    $("#msl-content").addClass("textResizer" + size);
    $(".textSizeLink").removeClass("selected");
    $("#msl-nav-ul-wrapper").removeClass("textResizer75");
    $("#msl-nav-ul-wrapper").removeClass("textResizer100");
    $("#msl-nav-ul-wrapper").removeClass("textResizer125");
    $("#msl-nav-ul-wrapper").removeClass("textResizer150");
    $("#msl-nav-ul-wrapper").addClass("textResizer" + size);
    $(this).addClass("selected");
});

// Trigger screen layout adjustments on resizing
$(window).resize(function () {
    ScreenWidthLayout();
});

// Set mobile vs. desktop element switching
$("#msl-nav-mobile-button").bind("click", function () {
    $("#msl-nav-ul-wrapper").toggleClass("hidden");
});

if ($("#msl-page-navigation-above").length === 0) {
    $("h1").first().after("<div id='msl-page-navigation-above'></div>");
}

if ($("#msl-page-navigation-below").length === 0) {
    $("#msl-page-history-div").before("<div id='msl-page-navigation-below'></div>");
}


// Manual Navigation
if ($("#mslManualNavigation").length > 0) {
    var currentLinkID = $("#mslManualNavigation div a[href='" + siteString + "'").parent().attr("id");    
    $("#mslManualNavigation .childItem").hide();
    $("#" + currentLinkID).show();

    $("#mslManualNavigation div").each(function () {
        var liClassString = $(this).attr("class");
        var count = CountOccurrences(liClassString, "parent", false);
        $(this).addClass("level" + count);

    });

    var liClassString = $("#" + currentLinkID).attr("class");
    $("[class='" + liClassString + "']").show();


    var levelClassString = $("#" + currentLinkID).attr("class");
    var levelClassArray = levelClassString.split(' ');
    var currentLevel;
    for (var j = 0; j < levelClassArray.length; j++) {
        if (levelClassArray[j].indexOf("level") > -1) {
            currentLevel = levelClassArray[j].replace("level", "");
        }
        else if (levelClassArray[j].indexOf("parent") > -1) {
            var parentID = levelClassArray[j].replace("parentItem_", "");
            $("#" + parentID).show();
            $("#" + parentID).addClass("currentPage");

            var parentLevelClassString = $("#" + parentID).attr("class");
            var parentLevelClassArray = parentLevelClassString.split(' ');
            var parentCurrentLevel;
            for (var k = 0; k < parentLevelClassArray.length; k++) {
                if (parentLevelClassArray[k].indexOf("level") > -1) {
                    parentCurrentLevel = parentLevelClassArray[k].replace("level", "");
                }
            }

            var parentChildLevel = Number(parentCurrentLevel) + 1;
            $("#mslManualNavigation .childItem.parentItem_" + parentID + ".level" + parentChildLevel).show();




        }
    }




    var childLevel = Number(currentLevel) + 1;
    $("#mslManualNavigation .childItem.parentItem_" + currentLinkID + ".level" + childLevel).show();


    $("#" + currentLinkID).addClass("currentPage");

}

//$('[data-toggle="tooltip"]').tooltip();
//$('.dropdown-toggle').dropdown();


function CountOccurrences(string, subString, allowOverlapping) {

    string += "";
    subString += "";
    if (subString.length <= 0) return (string.length + 1);

    var n = 0,
        pos = 0,
        step = allowOverlapping ? 1 : subString.length;

    while (true) {
        pos = string.indexOf(subString, pos);
        if (pos >= 0) {
            ++n;
            pos += step;
        } else break;
    }
    return n;
}


function ScreenWidthLayout() {
    if ($(window).width() < 990) {
        //$(".glyphicon-chevron-down").click();
        $("#msl-text-resizer").appendTo("#msl-page-navigation-above");
        $(".msl-infoContent-above").appendTo("#msl-page-navigation-above");
        $(".msl-infoContent-content").appendTo("#msl-page-navigation-above");
        $(".msl-infoContent-below").appendTo("#msl-page-navigation-below");
        $("#msl-nav-logo-link").insertAfter("#msl-nav-mobile-wrapper:not(.fullWidth)");
        $("#msl-nav-mobile-wrapper.fullWidth").insertAfter("#msl-nav-mobile-button");
        $("#msl-nav-mobile-button").removeClass("hidden");
        $("#msl-nav-ul-wrapper").addClass("hidden");
        $("#msl-nav-full-wrapper").addClass("hidden");
        $("#msl-page-top-search-block").insertAfter("#msl-page-top-logo-block");
    }
    else {
        $(".currentPageAncestor > .navGlyphiconDiv > .glyphicon-chevron-right").click();
        $("#msl-text-resizer").appendTo("#msl-content-rightNav");
        $(".msl-infoContent-above").appendTo("#msl-content-rightNav");
        $(".msl-infoContent-content").appendTo("#msl-content-rightNav");
        $(".msl-infoContent-below").appendTo("#msl-content-rightNav");
        $("#msl-nav-mobile-wrapper:not(.fullWidth)").insertAfter("#msl-nav-logo-link");
        $("#msl-nav-mobile-wrapper.fullWidth").appendTo("#msl-nav-wrapper");
        $("#msl-nav-full-wrapper").removeClass("hidden");
        $("#msl-nav-mobile-button").addClass("hidden");
        $("#msl-nav-ul-wrapper").removeClass("hidden");
        $("#msl-page-top-logo-block").insertAfter("#msl-page-top-search-block");
    }
}


function sortFunction(a, b) {
    if (a[0] === b[0]) {
        return 0;
    }
    else {
        return (a[0] < b[0]) ? -1 : 1;
    }
}

function affixWidth() {
    // ensure the affix element maintains it width
    var affix = $('.affix');
    var width = affix.width();
    affix.width(width);
}


// 
$(document).ready(function () {
    ScreenWidthLayout();

    $(".expandableLI").each(function () {
        var notHiddenChildren = $(this).find(".staticLI .navLinkDiv").not(".hidden").length;
        if (notHiddenChildren === 0) {
            $(this).children(".navGlyphiconDiv").addClass("hidden");
        }
    });

    $(".navLinkDiv.hidden").parent().addClass("hidden");

    affixWidth();
    var siteString = window.location.href.toLowerCase();
    if (siteString.indexOf("default_adminprod") > -1) {
        $("body").prepend("<div class=\"adminProdDiv\">DRAFT View!  To make updates to this page publicly available, you must 'Sync Public Tables' in the Content Management Application.");
    }


    $('#msl-nav-full-button').on('click', function (e) {
        $(".msl-full-page-block .collapse").toggleClass("in");
    });


    if ($(".expandCollapseDiv a").length > 0) {


        $(".expandCollapseDiv a").bind("click", function () {
            var parentID = $(this).parent().attr("id");
            var divID = parentID.replace("Navigation", "");
            $("#" + divID).toggleClass("hidden");
            if ($("#" + divID).hasClass("hidden")) {
                $(this).html("(Expand)");
            }
            else {
                $(this).html("(Collapse)");
            }
        });
    }
    if ($(".helpDivLink").length > 0) {


        $(".helpDivLink").bind("click", function () {
            $(".helpDivContent").not($(this).next()).addClass("hidden");
            $(this).next().toggleClass("hidden");

        });
    }

    $(".helpDivContentClose").bind("click", function () {
        $(this).parent().addClass("hidden");

    });


    $(".showDiv").bind("click", function () {
        var targetDiv = $(this).attr("data-value");
        $("#" + targetDiv).removeClass("hidden");
    });

    $(".hideDiv").bind("click", function () {
        var targetDiv = $(this).attr("data-value");
        $("#" + targetDiv).addClass("hidden");
    });


});

function toTitleCase(str) {
    //return str.replace(/\w\S*/g, function (txt) { return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase(); });
    return str;
}


$(document).ready(function () {

    $(".co-monograph-item-wrapper").bind("click", function () {
        $(this).parent().toggleClass("co-monograph-expanded");
        var nextStyle = $(this).next().css("display");
        if (nextStyle == "block") {
            $(this).next().css("display", "");

        }
        else {
            $(this).next().css("display", "block");

        }

    });

    if ($("#toolbar_fit").length > 0) {
        $("#toolbar_fit").click();
    }
    $("body").addClass("isVisible");
    if (searchSiteString.indexOf("fullbrowser") > -1) {

    }
    else {
        if ($("#breadcrumb_top").length == 0) {
            $("<ol id=\"msl-page-content-breadcrumb\" class=\"breadcrumb\"><li><a href=\"http://montanamemory.org/\">Home</a></li><li class=\"breadcrumbCurrentPage\">Search Results</li></ol>").insertBefore(".searchResultsH1");
        }
        else {
            $("#breadcrumb_top").insertBefore(".searchResultsH1");
        }
        if ($("#helpdocs_div").length > 0) {
        }
        else {
            $("#nav_top_right .nav").appendTo("#mmpFavoritesDiv");
            if ($("#results_box").length > 0) {
                $("#results_box").appendTo("#mmpResultsNavDiv");
                $("#results_box").removeClass("results_box");
            }
            else {
                $("#mmpResultsNavDiv").hide();
            }
            $("#top_content").appendTo("#msl-page-content-editable");
        }


    }
})