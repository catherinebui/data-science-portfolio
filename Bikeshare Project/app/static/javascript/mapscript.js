// function showImg() {var day; var startstation; }
$('#Member').addClass("active");
$('#MON').addClass("active");
$('#Massachusetts').selected = true;
$('#6').selected = true;
showImg();
// $('#Parking').addClass("active");
// $('button.map_day').click(function (){
//   $(this).addClass("active");
//   $(this).css('border', '1px solid red');
// });

$(window).load(function() {
  $('button.map_day').click(function() {
  $('button.map_day').removeClass("active");
  $('button.map_day').css('border', 'none');
  $(this).addClass("active");
  $(this).css('border', '3px solid #008CBA');
  showImg();
  });
});

$(window).load(function() {
  $('button.MemberType').click(function() {
  // $('button.MemberType').removeClass("active");
  if ($('button.MemberType').hasClass("active")) {
    if($(this).hasClass("active")) {
      $(this).removeClass("active");
      showImg();
    }
    else {
      $('button.MemberType').removeClass("active");
      $(this).addClass("active");
      showImg();
    }
  }
  else
  {
  $(this).addClass("active");
  showImg();
  // $(this).css('background-color', '#008CBA');
  // $(this).css('color', 'white');

  }
  });
});

$(window).load(function() {
  $('#miles').change(function() {
  showImg();
  });
});

$(window).load(function() {
  $('#startstationlist').change(function() {
  showImg();
  });
});







//creating a function that pull up the image based on active Variables

function showImg(){
  var day = '';
  var start = '';
  var distance = '';
  var member = '';

  var daydict = {
    'MON': 0,
    'TUE': 1,
    'WED': 2,
    'THUR': 3,
    'FRI': 4,
    'SAT': 5,
    'SUN': 6
  }

  var distdict = {
    '1 mile': 1,
    '2 miles': 2,
    '3 miles': 3,
    '4 miles': 4,
    '5 miles': 5,
    '6 miles': 6
    }

  $('button.map_day.active').each(function(){
    day = $(this).attr('id');
    // document.getElementById("mapboxlink").textContent= $(this).attr('id')
  });




  $('button.MemberType.active').each(function(){
    member = $(this).attr('id');
    // document.getElementById("mapboxlink").textContent= $(this).attr('id')
  });


  // get value of the distance
  distance = document.getElementById("miles").value;

  // get value of the start station
  start= document.getElementById("startstationlist").value;

  if (member == '') {
  var imgstring = start + '_'+ daydict[day] + '_'+ distdict[distance] + '.png';
  // document.getElementById("mapboxlink").textContent += imgstring;
  // document.getElementById("mapboximg").src = "{{ url_for('static', filename = 'data/REPLACE') }}".replace("REPLACE", imgstring)
  document.getElementById("mapboximg").src  = "/static/data/" + imgstring;
  }
  else {
  var imgstring = start + '_'+ daydict[day] + '_'+ distdict[distance] + '_' + member + '.png';
  // document.getElementById("mapboxlink").textContent += imgstring;
  document.getElementById("mapboximg").src  = "/static/data/" + imgstring;
    // document.getElementById("mapboximg").src = "{{ url_for('static', filename = 'data/REPLACE') }}".replace("REPLACE", imgstring)
  }


}
