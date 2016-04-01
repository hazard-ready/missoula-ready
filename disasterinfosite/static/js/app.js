$( document ).ready(function() {
  $(document).foundation();

  // convenience function to extract url parameters
  function getURLParameter(name) {
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null) {
       return null;
    } else {
       return results[1] || 0;
    }
  }

  // grab the position, if possible
  var query_lat = getURLParameter('lat');
  var query_lng = getURLParameter('lng');

  // set up the map
  var map = L.map('map');
  if (query_lat && query_lng) {
    zoom = 14;
    map.setView([query_lat, query_lng], zoom);
  } else { // use the data bounds if we don't have a position in the query string
    map.fitBounds(mapBounds);
  }
  map.scrollWheelZoom.disable();

  var osmUrl='//{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png';
  var osmAttrib='Map data © <a href="//openstreetmap.org">OpenStreetMap</a> contributors';
  var layer = new L.TileLayer(osmUrl, {attribution: osmAttrib}).addTo(map);
  layer.setOpacity(0.6);

  $.ajax({
    type: "POST",
    url: "static/img/boundary.geojson",
    dataType: "json",
    success: function(boundaryShape) {
      var boundaryStyle = {
        "color": "rgb(253, 141, 60)",
        "weight": 4,
        "opacity": 1,
        "fillColor": "#ffffff",
        "fillOpacity": 0.7
      };
      var boundaryLayer = L.geoJson(boundaryShape, {
        style: boundaryStyle
      }).addTo(map);
    }
  });

  document.getElementById('map').style.cursor='default';
  if (query_lat && query_lng) {
    var icon = new L.Icon.Default;
    icon.options.iconUrl = "static/img/marker-icon.png";
    var marker = L.marker([query_lat, query_lng], {
      icon: icon,
      clickable: false,
      keyboard: false
    }).addTo(map);
    layer.setOpacity(1);
  }

  // Make a click on the map submit the location
  map.on('click', function(e) {
    location_query_text = "";
    $("#location-text").val(location_query_text);  // clear query text
    submitLocation(e.latlng.lat, e.latlng.lng);
  });

  // grab and set any previously entered query text
  var loc = getURLParameter('loc');
  var location_query_text = (loc) ? decodeURIComponent(loc) : query_lat + "," + query_lng;
  if (!query_lat || !query_lng)
    location_query_text = "";
  $("#location-text").val(location_query_text);

  // // hitting enter key in the textfield will trigger submit
  $("#location-text").keydown(function(event) {
    if (event.keyCode == 13) {
      $('#location-submit').trigger('click');
      return false;
    }
  });

  // submit location text
  $("#location-submit").click(function() {
    // grab the query value, ignoring it if it's empty
    location_query_text = $("#location-text").val();
    if (location_query_text.length == 0) return;
    disableForm();

    // request geocoding from google CLIENT SIDE!
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': location_query_text}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        var lat = results[0].geometry.location.lat();
        var lon = results[0].geometry.location.lng();
        submitLocation(lat,lon);
      } else {
        $(".geocode-error-message").html($('p').text("We had a problem finding that location."));
      }
    });
  });

  // auto location
  $(".auto-location-submit").click(function() {
    location_query_text = "";
    disableForm();
    var geoOptions = { timeout: 8000 };
    var geoSuccess = function(position) {
      var lat = position.coords.latitude;
      var lng = position.coords.longitude;
      // success! onwards to view the content
      submitLocation(lat, lng);
    };
    var geoError = function(error) {
      console.log('Error finding your location: ' + error.message);
      enableForm();
    };
    navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
  });

  // during api calls, disable the form
  function disableForm() {
    $("#location-text").prop("disabled", true);
    $("#location-submit").addClass("disabled");
    $(".auto-location-submit").addClass("disabled");
    $(".loading").show();
  }

  // if a search fails or a restart, enable the form
  function enableForm() {
    $("#location-text").prop("disabled", false);
    $("#location-submit").removeClass("disabled");
    $(".auto-location-submit").removeClass("disabled");
    $(".loading").hide();
  }

  function submitLocation(lat,lng) {
    // reload the page with the lat,lng
    document.location =  encodeURI(document.location.hash + "?lat=" + lat + "&lng=" + lng + "&loc=" + location_query_text);
  }

  // Set up slick photo slideshow
  function loadGallery() {
    var currentSlideElement = $('.disaster-content.active .past-photos');
    currentSlideElement.slick({
      slidesToShow: 1,
      lazyLoad: 'progressive'
    });
    return currentSlideElement;
  }

  // Initialize the slide gallery on the open disaster tab
  var slideContainer = loadGallery();

  // Open a new image gallery when a new tab is opened
  $('.disaster-tabs').on('toggled', function () {
    slideContainer.slick('unslick');
    slideContainer = loadGallery();
  });

  // Signup forms

  $("#button--signup").click(function() {
    $("#user-button-container").hide();
    $("#user-signup-container").show();
  });


  $("#button--login").click(function() {
    $("#user-button-container").hide();
    $("#user-login-container").show();
  });

  $(".button--cancel").click(function() {
    $("#user-signup-container").hide();
    $("#user-login-container").hide();
    $("#user-button-container").show();
  });

  function setValueOnFocus(el, value) {
    el.focus(function() {
      if(el.val() === "") {
        el.val(value);
      }
    });
  }

  function requiredFocus(el) {
    el.focus(function() {
      el.removeAttr('placeholder');
      el.css({
        'border-color': '#ccc'
      });
    });
  }

  function requiredBlur(el) {
    el.blur(function() {
      if(el.val() === "") {
        el.attr('placeholder', 'Required.');
        el.css({
          'border-color': '#f03b20'
        });
      }
    });
  }

  requiredFocus($("#user-signup__username"));
  requiredFocus($("#user-signup__password"));
  requiredBlur($("#user-signup__username"));
  requiredBlur($("#user-signup__password"));
  setValueOnFocus($("#user-signup__state"), "MT");
  setValueOnFocus($("#user-signup__zip"), "598");

  var sendAjaxAuthRequest = function(url, data, error, success) {
    var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajaxSetup({
      crossDomain: false,
      beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    });
    $.ajax({
      type: "POST",
      url: url,
      data: data,
      error: error,
      success: success
    });
  };

  $("#user-signup__submit").click(function() {
    var username = $('#user-signup__username').val();
    var password = $('#user-signup__password').val();
    var address1 = $('#user-signup__address1').val();
    var address2 = $('#user-signup__address2').val();
    var city = $('#user-signup__city').val();
    var state = $('#user-signup__state').val();
    var zip = $('#user-signup__zip').val();

    sendAjaxAuthRequest(
      "/accounts/create_user/",
      {
        username: username,
        password: password,
        address1: address1,
        address2: address2,
        city: city,
        state: state,
        zip_code: zip,
        next: "/"
      },
      function(err) {
        console.log(err.responseText);
      },
      function(){
        $("#user-signup-container").hide();
        $("#user-signup-result-container").show();
    });
  });

  $("#user-login__submit").click(function() {
    var username = $('#user-login__username').val();
    var password = $('#user-login__password').val();
    sendAjaxAuthRequest(
      "/accounts/login/",
      {
        username: username,
        password: password,
        next: "/"
      },
      function() {
        $("#user-login-container").hide();
        $("#user-info-container--invalid").show();
      },
      function() {
        $("#user-login-container").hide();
        $("#user-info-container").show();
      });
  });

  $("#button--logout").click(function() {
    sendAjaxAuthRequest(
      "/accounts/logout/",
      { next: "/" },
      function() {
        // todo: show an error?
      },
      function() {
        $("#user-button-container--logged-in").hide();
        $("#user-button-container").show();
      }
    );
  });

});
