(function($) {
  "use strict";

  $(function() {
    var target_provision = window.location.hash.substr(1).split('?')[0];

    if( $('#' + target_provision + '-text') ) {
      var $details = $('details');
      $details.removeAttr('open');

      $('#' + target_provision + '-text')
        .parents('details')
        .attr('open', 'true');
    }
  });

}(jQuery));