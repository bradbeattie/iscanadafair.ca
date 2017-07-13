$("[data-reveal-after]").addClass("reveal")
$(document).on("click", "button[data-reveal-trigger]", function() {
    var trigger = $(this).data("reveal-trigger")
    $(this).parents(".jumbotron").removeClass("jumbotron").addClass("well")
    $("[data-reveal-trigger="+trigger+"]").remove()
    $("[data-reveal-after="+trigger+"]").addClass("revealed")
    $.post("?" + trigger, function(data) {});
})
$(document).on("click", "a", function () {
    if (this.hostname && this.hostname !== window.location.hostname) {
        $(this).prop("target", "_blank")
    }
})
