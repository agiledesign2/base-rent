(function($) {

	'use strict';

  /* Alert Boxes
  * ------------------------------------------------------ */
  var clAlertBoxes = function() {

    $('.messages').on('click', '.close', function() {
      $(this).parent().fadeOut(500);
    }); 

  };

  /* Initialize
  * ------------------------------------------------------ */
  (function ssInit() {
        
    clAlertBoxes();

  })();

})(jQuery);