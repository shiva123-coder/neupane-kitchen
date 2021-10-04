// scroll icon only visible once screen is scroll down to over 100px
$(window).scroll(function(){
    var screenHeight = $(window).scrollTop();
    if (screenHeight > 100) {
        $('#scroll-icon').fadeIn();
    } else {
        $('#scroll-icon').fadeOut(2000);
    }
});

// once click on scroll icon, page scroll back to the top
$('#scroll-icon').click(function(e){
    window.scrollTo(0,0)
});


// sort option from the select box
$('#sort-selection').change(function() {
    let sort_selector = $(this);
    let currentUrl = new URL(window.location);
    let selectedVal = sort_selector.val();

    if(selectedVal != "reset"){
        let sort = selectedVal.split("_")[0];
        let direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});





