function balse(){
    $("button").prop("disabled",true);
    $("body").addClass("shaking");
    $.ajax({
        url: "/balse",
        type: 'get'
    }).done(function(r){
        $("html").text(r);
    });
}
